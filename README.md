# Switchbot Temperature Logger
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)



## What it does

This is a script I wrote to log the temperature and humidity data from my Switchbot sensors.

It is using the Switchbot API to get the data from all the sensors (Outdoor Meter and Hub2) and logging it into a csv file every n seconds.

The CSV file looks like this 
```csv
2023-10-03 23:42:52.255775,Living Room,23.9,56
2023-10-03 23:42:52.255775,Backyard,14.5,77
2023-10-03 23:42:52.255775,Bedroom,23.3,61
2023-10-03 23:42:52.255775,Kitchen,22.8,59
```

## Starting the script

First, fill in your credentials in run_temp_logger.sh.
```bash
key='your_secret_key'
token='your_token'
```
Instructions to get API key and token are in [Switchbot API Documentation](https://github.com/OpenWonderLabs/SwitchBotAPI)

You can also customize the log file name and the interval in seconds between each API call.
```bash
csv_file='temp_log.csv'
sleep 60
```

On MacOSX and Linux, run the script with ```./run_temp_logger.sh```