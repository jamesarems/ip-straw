#!/usr/bin/env python3
import os, json, sys, time
import requests
import pyfiglet
print(pyfiglet.figlet_format('IP - Straw'))
print('----- By github.com/jamesarems   (c) 2020\n\n')
try:
    print('(*) Processing '+ sys.argv[1] + '\n')
    res = requests.get('http://ip-api.com/json/'+ sys.argv[1]).json()
    if res['status'] == "success":
        print('Findings are,')
        print('COUNTRY : '+ res['country'])
        print('REGION : '+ res['region'])
        print('REGION NAME : '+ res['regionName'])
        print('CITY : '+ res['city'])
        print('ZIP : '+ res['zip'])
        print('ISP : '+ res['isp'])
        print('ZONE : '+ res['timezone'])
        print('ORGANIZATION : '+ res['org'])
    else:
        print('Sorry, No result found')
except:
    print('No value')