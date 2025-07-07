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


def build_headers(
    secret: str = Config.SECRET_KEY, token: str = Config.TOKEN
) -> dict[str, str]:
    headers = {}
    nonce = uuid.uuid4()
    t = int(round(time.time() * 1000))
    string_to_sign = "{}{}{}".format(token, t, nonce)
    string_to_sign = bytes(string_to_sign, "utf-8")
    secret_bytes = bytes(secret, "utf-8")
    sign = base64.b64encode(
        hmac.new(secret_bytes, msg=string_to_sign, digestmod=hashlib.sha256).digest()
    )
    headers["Authorization"] = token
    headers["Content-Type"] = "application/json"
    headers["charset"] = "utf8"
    headers["t"] = str(t)
    headers["sign"] = str(sign, "utf-8")
    headers["nonce"] = str(nonce)
    return headers


def switchbot_api_request(url) -> dict | None:
    response = requests.get(url, headers=build_headers())
    if response.status_code not in [100, 200]:
        print(f"Error in API request {url}. Response : {response}")
        return None
    return response.json()


def get_devices() -> dict[str, str] | None:
    device_list_url = "https://api.switch-bot.com/v1.0/devices"
    response = switchbot_api_request(device_list_url)
    if not response:
        return None
    devices = {
        device["deviceId"]: device["deviceName"]
        for device in response["body"]["deviceList"]
    }
    print(f"Found devices {devices}")
    return devices


def fetch_device_record(device_id) -> Record | None:
    request_url = "https://api.switch-bot.com/v1.1/devices/" + device_id + "/status/"
    response = switchbot_api_request(request_url)
    if not response:
        return None

    temperature: str = response["body"]["temperature"]
    humidity: str = response["body"]["humidity"]
    return Record(
        device_id=device_id,
        temperature=temperature,
        humidity=humidity,
    )


def add_devices_to_session(devices: dict[str, str], session: Session):
    for device_info in devices:
        device = Device(id=device_info, name=devices[device_info])
        if not session.query(Device).filter_by(id=device.id).first():
            session.add(device)
            print(f"Adding {device}")
    session.commit()
    session.close()


def fetch_and_save_records(devices, session):
    timestamp = datetime.now()
    for device_id in devices:
        device_record: Record | None = fetch_device_record(device_id)
        if not device_record:
            continue
        device_record.timestamp = timestamp
        session.add(device_record)
        session.commit()
        print(f"--> Adding {device_record}")
    session.close()


def main():
    session = get_session()
    devices = get_devices()

    if not devices:
        return

    add_devices_to_session(devices, session)

    while True:
        print(f"{datetime.now()} Requesting data")
        try:
            fetch_and_save_records(devices, session)
        except Exception as e:
            print(f"Error :\n{e}")
            if "Response[429]" in str(e):
                print("Too many requests, waiting 5 minutes before retrying")
                time.sleep(300)

        time.sleep(Config.REQUEST_INTERVAL)


if __name__ == "__main__":
    main()
