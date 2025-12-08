from netmiko import ConnectHandler

# Define the device to connect to
device = {
    'device_type': 'cisco_ios',
    'host': '10.1.1.1',
    'username': 'admin',
    'password': 'devnet123',
    'secret' : 'devnet123',
}

connection = ConnectHandler(**device)
print("Connection successfully established")
print("*************************************************************")
print("*************************************************************")
connection.enable()
output = connection.send_command('show ip interface brief | in up')
print(output)

print("***************Configuring a VLAN and SVI *********************")
config_commands = [
    'vlan 100',
    'name SALES',
    'exit',
    'interface Vlan100',
    'ip address 192.168.100.1 255.255.255.0',
    'no shutdown'
]

output = connection.send_config_set(config_commands)
print(output)

print("***************Configuring a VLAN and SVI from a txt file*********************")
output = connection.send_config_from_file('vlan_svi.txt')
print(output)