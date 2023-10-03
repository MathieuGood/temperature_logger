#!/bin/bash
while true; do

    # Secret Key
    key='key'

    # Token
    token='token'
    
    # CSV file for log
    csv_file='your_temp_log.csv'
    
    # Launch program with python interpreter
    python3 switchbot_temp_logger.py $key $token $csv_file
    
    # Wait for 60 seconds before next API call
    sleep 60

done