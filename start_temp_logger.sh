#!/bin/bash
while true; do

    # Secret Key
    key='b57d2452e5f1e580dccde5ca5cad922'

    # Token
    token='af38398c2ef42575b6d5a85b464a3eabc8066b0c660d2d7981f862be094e6ecf61069abf984c04f9f6d02ee6667d4976'
    
    # CSV file for log
    csv_file='temp_log.csv'
    
    # Launch the program with the python interpreter
    python3 switchbot_temp_logger.py $key $token $csv_file
    
    # Wait for 60 seconds
    sleep 60

done