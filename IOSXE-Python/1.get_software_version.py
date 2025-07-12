
#A simple python script to get a cisco ios device software version
import netmiko

ip = '10.0.0.1'
username = 'cisco'
password = 'cisco'
device_type = 'cisco_ios'
port = '22'

net_connect = netmiko.ConnectHandler(
    ip = ip,
    device_type = device_type,
    username = username,
    password = password,
    port = port
)

show_version = net_connect.send_command('show version')

print(show_version)