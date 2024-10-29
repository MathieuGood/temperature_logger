# Switchbot Temperature Logger
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)



## What it does

This Python app logs temperature and humidity data from a Switchbot sensors to a database.

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

4. Create a `.env` file in the root directory of the project and add the following variables
```bash
# Switchbot API credentials
SWITCHBOT_API_KEY=your_api_key
SWITCHBOT_TOKEN=your_token

# Database connection string
DATABASE_URI="postgresql+psycopg2://user:password@host:port/database_name"

# Number of seconds between each request to the Switchbot API
REQUEST_INTERVAL=60
```


Instructions to get API key and token are in [Switchbot API Documentation](https://github.com/OpenWonderLabs/SwitchBotAPI)
