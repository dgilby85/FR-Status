#!/usr/bin/env python3

import requests
import re
import time
from termcolor import colored
from os import system

# Setup dictionaries
URL_Dict = {
    5: "Account Services",
    16: "Central Bank",
    6: "Check 21",
    7: "Check Adjustments",
    4: "FedACH",
    8: "FedCash",
    1: "Fedwire Funds",
    2: "Fedwire Securities",
    3: "National Settlement"
}

# Set terminal clear (change to cls if windows) and create forever loop
value = True
system("clear")
# Loop get URL and parse for status info
while (value):
    final_data = {}
    
    for id, value in URL_Dict.items():
        response = requests.get(f'https://frbservices.org/app/status/message.do?sId={id}')
        if response:
            query = re.search('alt=".*"', response.text)
            data = query.group().split('"')
            final_data.update({value: data[1]})
        else:
            print(f'An error has occurred for {value}.')
    time.sleep(.25)
    system("clear")
    
    t = time.localtime()
    cur_time = time.strftime("%H:%M:%S %m/%d/%y", t)
    
    print('\t' + cur_time)
    for name, status in final_data.items():
        if status == "Normal Operations":
            word_space = len(name)
            new_position = 20 - word_space
            print(f'{name}' + ':' + (new_position * ' ') + colored(status, 'green'))
        else:
            word_space = len(name)
            new_position = 20 - word_space
            print(f'{name}' + ':' + (new_position * ' ') + colored(status, 'red'))
    time.sleep(60)
