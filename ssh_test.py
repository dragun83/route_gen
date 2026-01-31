import paramiko

host='192.168.56.102'
tcpport='22'
user='ocp-adm'
pasw='Qwe12345'
command = '/file print'

c = paramiko.SSHClient()
c.load_system_host_keys()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(host, port=tcpport, username=user, password=pasw)
stdin, stdout, stderr = c.exec_commnd(command)
print(stdout.read().decode())
