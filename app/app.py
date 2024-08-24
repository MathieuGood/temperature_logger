import csv
import time
import hashlib
import hmac
import base64
import uuid
import requests
from datetime import datetime
from flask import Flask, render_template
from config import Config

app = Flask(__name__)


def build_header(
    secret=Config.SECRET_KEY,
    token=Config.TOKEN,
):
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


def api_request(url, header):
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
        write_log("temp_log.csv", [datetime.now(), error_message])
        time.sleep(60)
        return api_request(url, header)


def write_log(csv_file, content):
    with open(csv_file, "a", newline="") as csv_data:
        writer = csv.writer(csv_data)
        writer.writerow(content)


def get_devices(header):
    device_list_url = "https://api.switch-bot.com/v1.0/devices"
    response_devices = api_request(device_list_url, header)
    print(response_devices)
    devices = []
    for device in response_devices["body"]["deviceList"]:
        devices.append([device["deviceName"], device["deviceId"]])
    return devices


def get_devices_status(devices, header):
    timestamp = datetime.now()
    print(f"\n{timestamp}")
    n = 0
    for device in devices:
        print(f"## Getting device {device[0]} status")
        device_status_url = "https://api.switch-bot.com/v1.1/devices/"
        response = api_request(device_status_url + device[1] + "/status/", header)
        temperature = response["body"]["temperature"]
        hygrometry = response["body"]["humidity"]
        devices[n].append(temperature)
        devices[n].append(hygrometry)

        devices.append([temperature])
        print(device[3], "%  ", device[2], "° ", device[0])
        write_log("temp_log.csv", [timestamp, device[0], device[2], device[3]])
        n += 1
    return devices


@app.route("/")
@app.route("/index")
def index():
    header = build_header()
    devices = get_devices(header)
    devices_status = get_devices_status(devices, header)

    return render_template(
        "index.html",
        name_salon=devices_status[0][0],
        temp_salon=devices_status[0][2],
        name_ext=devices_status[1][0],
        temp_ext=devices_status[1][2],
        name_cam=devices_status[2][0],
        temp_cam=devices_status[2][2],
        name_cl=devices_status[3][0],
        temp_cl=devices_status[3][2],
    )


if __name__ == "__main__":
    app.run(debug=True)
