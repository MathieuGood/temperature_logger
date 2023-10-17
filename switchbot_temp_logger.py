import sys
import csv
import time
import hashlib
import hmac
import base64
import uuid
import requests
from datetime import datetime


def build_header(secret=sys.argv[1], token=sys.argv[2]):
    header = {}
    nonce = uuid.uuid4()
    t = int(round(time.time() * 1000))
    string_to_sign = '{}{}{}'.format(token, t, nonce)
    string_to_sign = bytes(string_to_sign, 'utf-8')
    secret = bytes(secret, 'utf-8')
    sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
    header['Authorization'] = token
    header['Content-Type'] = 'application/json'
    header['charset'] = 'utf8'
    header['t'] = str(t)
    header['sign'] = str(sign, 'utf-8')
    header['nonce'] = str(nonce)
    return header


def api_request(url, header):  
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        print(response)
        response_message = response.text.replace('{', '').replace('}', '').replace('"', '')
        error_message = f"Error:{response.status_code} {response_message}"
        write_log(sys.argv[3], [datetime.now(), error_message])
        time.sleep(60)
        return api_request(url, header)


def write_log(csv_file, content):
    with open(csv_file, 'a', newline='') as csv_data:
        writer = csv.writer(csv_data)
        writer.writerow(content)
 

def main():
    device_list_url = "https://api.switch-bot.com/v1.0/devices"
    device_status_url = "https://api.switch-bot.com/v1.1/devices/"
    header = build_header()
    response_devices = api_request(device_list_url, header)
    
    # Request devices list and append them to devices[]
    devices = []
    for device in response_devices['body']['deviceList']:
        devices.append([device['deviceName'], device['deviceId']])

    # Request each device status with deviceId from devices
    # Add all the temperature data in devices
    timestamp = datetime.now()
    print(f'\n{timestamp}')
    n = 0    
    for device in devices:
        response = api_request(device_status_url + device[1] + '/status/', header)
        devices[n].append(response['body']['temperature'])
        devices[n].append(response['body']['humidity'])
        print(device[3], '%  ', device[2], '° ', device[0])
        # write to csv >>>
        write_log(sys.argv[3], [timestamp, device[0], device[2], device[3]])
        n += 1


if __name__ == '__main__':
    main()