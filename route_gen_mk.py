#!/usr/bin/python3
#RegExp цельнотянутый на проверку IP адреса "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
import socket
import re
import argparse
import paramiko
pattern = re.compile('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')
def set_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('Hostname', nargs='?', help="[HOSTNAME] FQDN name of site that you want to add on to route table")
    parser.add_argument('Gate', nargs='?',  help="[GATEWAY] IP address or name of gateway")
    parser.add_argument ('--ssh', dest='ssh',  help="SSH Hostname or Address")
    parser.add_argument ('--ssh-port', dest='ssh_port', default='22', help ="SSH port (default 22)")
    parser.add_argument ('--ssh-user', dest='ssh_user', help="SSH username")
    parser.add_argument ('--ssh-password', dest='ssh_pass', help="SSH password")
    parser.add_argument ('--file', dest='file',  help="Send result to file")
    return parser
    
def send_file(file,  text):
    f = open(file, 'r')
    f.write(text)
    f.close()
    return
def setup_ssh(server, tcpport, user, paswd):
    print('HOST :' + server)
    print('PORT :' + tcpport)
    print('USERNAME :' + user)
    print('PASSWORD :' + paswd)
    client = paramiko.SSHClient()
    if paswd is None:
        client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #ACHTUNG!!!!!!  не безопасная конструкция с точки зрения ИБ!!!!!!!!!! Должно обрабатываться через прерывания!!!
    if tcpport is None:
        tcpport = 22 
    client.connect(server, port=tcpport, username=user,  password=paswd)
    return client

def get_ipv4_addresses(hostname):
    ret=[]
    lst=[]
    ais = socket.getaddrinfo(args.Hostname,0,0,0,0)
    for result in ais:
        ret.append(result[-1][0])
    ret = list(set(ret))
    for ip in ret:
        if pattern.match(ip):
            lst.append(ip)
    return lst

#try:
parser = set_parser()
args = parser.parse_args()
if args.ssh:
    SSHClient = setup_ssh(args.ssh, args.ssh_port, args.ssh_user, args.ssh_pass )
    for ip in get_ipv4_addresses(args.Hostname):
        command = '/ip route add dst-address=' + ip + '/32 gateway=' + args.Gate +'comment=\"' + args.Hostname + '\"'
        print("SENDING: " + command)
        stdin,  stdout,  stderr = SSHClient.exec_command(command)
        out = stdout.read()
        print(out.decode())
    print("Closing SSH session...")
    SSHClient.close()
elif args.file:
    print('NOT READY YET!')
else:    
    print("Конечный :" + str(get_ipv4_addresses(args.Hostname)))
    for ip in get_ipv4_addresses(args.Hostname):
         print('/ip route add dst-address=' + ip + '/32 gateway='+ args.Gate + ' comment=\"' + args.Hostname + '\"')
#except Exception as e:
#   print('We get some Errors: ' + str(e))
