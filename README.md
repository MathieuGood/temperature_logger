# Switchbot Temperature Logger

## What it does

This is a script I wrote to log the temperature and humidity data from my Switchbot sensors.

It is using the Switchbot API to get the data from all the sensors (Outdoor Meter and Hub2) and logging it into a csv file.

The CSV file looks like this 
```csv
2023-10-03 23:42:52.255775,Living Room,23.9,56
2023-10-03 23:42:52.255775,Backyard,14.5,77
2023-10-03 23:42:52.255775,Bedroom,23.3,61
2023-10-03 23:42:52.255775,Kitchen,22.8,59
```

[Switchbot API Github Documentation](https://github.com/OpenWonderLabs/SwitchBotAPI)