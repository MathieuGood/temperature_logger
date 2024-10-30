# 🌡️ Switchbot Temperature Logger

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## What it does

This Python app logs temperature and humidity data from a Switchbot sensors to a database.

Instructions to get API key and token are in [Switchbot API Documentation](https://github.com/OpenWonderLabs/SwitchBotAPI)

![App running](doc/temperature_logger_animation.gif)

## How to use

1. Clone the repository

```bash
git clone https://github.com/MathieuGood/temperature_logger.git
```

2. Create a virtual environment and activate it

```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required packages

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory of the project and add the following variables (an example file is provided in the doc folder)

```bash
# Switchbot API credentials
SWITCHBOT_API_KEY="your_api_key"
SWITCHBOT_TOKEN="your_token"

# Database connection string
DATABASE_URI="postgresql+psycopg2://user:password@host:port/database_name"

# Number of seconds between each request to the Switchbot API
REQUEST_INTERVAL=60

# Activate verbose SQL logging
VERBOSE_SQL_LOGGING=False
```

5. Run the app

```bash
python src/main.py
```


## Create a docker image

Containerizing the app is a handy way to deploy it on a server. Do not forget to provide the required environment variables in the `docker run` command.

1. Build the image

```bash
# For Synology NAS
docker buildx build --platform linux/amd64 -t temperature_logger:latest .
# For current platform
docker build -t temperature_logger .
```

2. Save it to a tar file

```bash
docker save -o docker_images/temp-logger.tar temperature_logger:latest
```