#!/usr/bin/python3
import argparse
def set_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest='Filename', required=True, help="Path to file")
    parser.add_argument('-g',  dest='Gate', required=True, help="Gateway ip address\name")
    parser.add_argument('-c', dest='Comm',required=True,   help = "Comment for routes identification")
    return parser
parser = set_parser()
args = parser.parse_args()
f = open(args.Filename, "r")
for ln in f:
    print('/ip route add dst-address=' + ln.rstrip() +' gateway='+args.Gate+' comment=\"' + args.Comm + '\"' )
