#!/usr/bin/python3

#Запилим разбор JSON  вытащим оттуда адреса и зашлем их в конфиг роутера

#import paramico
#import re
#import argparse
import json
import requests

json_url = 'https://www.gstatic.com/ipranges/goog.json'

def get_google_v4addresses():
  ret = []
  resp = requests.get(json_url)
  for ip in resp.json().get('prefixes'):
    v4addr = ip.get('ipv4Prefix')
    if v4addr is not None:
      ret.append(v4addr)
  return ret

for g_address in get_google_v4addresses():
  print('/ip route add dst-address=' + g_address +' gateway=192.168.11.2 comment=\"google.com\"')

