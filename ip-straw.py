#!/usr/bin/env python3
import os, json, sys, time
from colored import fg, attr
import requests
import pyfiglet
#Colors
GR = fg('green')
RE = fg('red')
YE = fg('yellow')
DIM = attr('dim')
BOL = attr('bold')
PU = fg('orange_4b')
RES = attr('reset')
LOAD = BOL + YE + '*' + RES

print(DIM + PU + pyfiglet.figlet_format('IP - Straw') + RES)
print('----- By github.com/jamesarems   (c) 2020\n\n')

def botscout(ip):
    print('\n[' + LOAD + '] Scanning botscout + ABUSE (botscout.com) ')
    link = "https://iplists.firehol.org/files/botscout_30d.ipset"
    val = requests.get(link).text
    if ip in val:
        print( RE + '+++ Found' + RES )
    sblam(ip)

def sblam(ip):
    print('\n[' + LOAD + '] Scanning Sblam + ABUSE (sblam.com) ')
    link = "https://iplists.firehol.org/files/sblam.ipset"
    val = requests.get(link).text
    if ip in val:
        print( RE + '+++ Found' + RES )
    stopForum(ip)

def stopForum(ip):
    print('\n[' + LOAD + '] Scanning StopForum + ABUSE (stopforumspam.com) ')
    link = "https://iplists.firehol.org/files/stopforumspam_30d.ipset"
    val = requests.get(link).text
    if ip in val:
        print( RE + '+++ Found' + RES )
    sockProxy(ip)

def sockProxy(ip):
    print('\n[' + LOAD + '] Scanning SockProxy + Proxy ')
    link = "https://iplists.firehol.org/files/socks_proxy_30d.ipset"
    val = requests.get(link).text
    if ip in val:
        print( RE + '+++ Found' + RES )
    badBot(ip)

def badBot(ip):
    print('\n[' + LOAD + '] Scanning BadBots + ATTACKS ')
    link = "https://iplists.firehol.org/files/bi_badbots_0_1d.ipset"
    val = requests.get(link).text
    if ip in val:
        print( RE + '+++ Found' + RES )
    haleySSH(ip)

def haleySSH(ip):
    print('\n[' + LOAD + '] Scanning haleySSH + ATTACKS ')
    link = "https://iplists.firehol.org/files/haley_ssh.ipset"
    val = requests.get(link).text
    if ip in val:
        print( RE + '+++ Found' + RES )


try:
    print('[ ' + LOAD + ' ] Processing '+ GR + sys.argv[1] + RES + '\n')
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
        botscout(sys.argv[1])
    else:
        print('Sorry, No result found')
except:
    print('No value \n  - Usage : ' + YE + sys.argv[0] + ' ip-address' + RES)

