#!/bin/bash
while true; do

    # Secret Key
    key='your_secret_key'

    # Token
    token='your_token'
    
    # CSV file for log
    csv_file='temp_log.csv'
    
    # Launch program with python interpreter
    python3 switchbot_temp_logger.py $key $token $csv_file
    
    # Wait for 60 seconds before next API call
    sleep 60

done