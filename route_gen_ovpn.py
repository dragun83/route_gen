#!/usr/bin/python3
#RegExp цельнотянутый на проверку IP адреса "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
import socket
import re
import argparse
pattern = re.compile('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')
def set_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('Hostname', nargs='?')
    return parser
try:
    ip_list = []
    parser = set_parser()
    args = parser.parse_args()
    ais = socket.getaddrinfo(args.Hostname,0,0,0,0)
    for result in ais:
        ip_list.append(result[-1][0])
    ip_list = list(set(ip_list))
    print (ip_list)
    for ip in ip_list:
        if pattern.match(ip):
            print('push \"route ' + ip + ' 255.255.255.255\"')
except Exception:
    print('We get some Errors! ')
