import sys
import time
import hashlib
import hmac
import base64
import uuid
import requests
from datetime import datetime
from config.config import Config
from database.database import get_session
from models.device import Device
from models.record import Record
from sqlalchemy.orm import Session


def build_header(
    secret: str = Config.SECRET_KEY, token: str = Config.TOKEN
) -> dict[str, str]:
    header = {}
    nonce = uuid.uuid4()
    t = int(round(time.time() * 1000))
    string_to_sign = "{}{}{}".format(token, t, nonce)
    string_to_sign = bytes(string_to_sign, "utf-8")
    secret = bytes(secret, "utf-8")
    sign = base64.b64encode(
        hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest()
    )
    header["Authorization"] = token
    header["Content-Type"] = "application/json"
    header["charset"] = "utf8"
    header["t"] = str(t)
    header["sign"] = str(sign, "utf-8")
    header["nonce"] = str(nonce)
    return header


def switchbot_api_request(url, header):
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        print(response)
        response_message = (
            response.text.replace("{", "").replace("}", "").replace('"', "")
        )
        error_message = f"Error:{response.status_code} {response_message}"
        print(error_message)


def get_devices(header) -> dict[str, str]:
    device_list_url = "https://api.switch-bot.com/v1.0/devices"
    response_devices = switchbot_api_request(device_list_url, header)
    devices = {
        device["deviceId"]: device["deviceName"]
        for device in response_devices["body"]["deviceList"]
    }

    return devices


def get_device_record(device_id, header) -> Record:
    request_url = "https://api.switch-bot.com/v1.1/devices/" + device_id + "/status/"
    response = switchbot_api_request(request_url, header)
    temperature: str = response["body"]["temperature"]
    humidity: str = response["body"]["humidity"]
    return Record(device_id=device_id, timestamp=datetime.now(), temperature=temperature, humidity=humidity)


def update_devices(devices: dict[str, str], session : Session, header : dict[str, str]):
    for device_info in devices:
        device = Device(id=device_info, name=devices[device_info])
        if not session.query(Device).filter_by(id=device.id).first():
            session.add(device)
            print(f"Adding device: {device}")
    session.commit()
    session.close()

def main():
    header = build_header()
    session = get_session()

    devices = get_devices(header)
    update_devices(devices, session, header)


    for device_id in devices:
        device_record = get_device_record(device_id, header)
        session.add(device_record)

    session.commit()
    session.close()


if __name__ == "__main__":
    main()
