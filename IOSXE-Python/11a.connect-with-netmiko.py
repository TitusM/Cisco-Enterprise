from netmiko import ConnectHandler

# Define the device to connect to
devices = [
    {'device_type': 'cisco_ios','host': '10.1.1.1','username': 'admin','password': 'devnet','secret':'devnet'},
    {'device_type': 'cisco_ios','host': '10.2.2.2','username': 'admin','password': 'devnet','secret':'devnet'},
]

commands = [
    'show interface status',
    'show vlan',
    'show ip interface brief | in up'
]

for device in devices:
    connection = ConnectHandler(**device)
    
    print(f"Connection to {device['host']} successfully established")
    print("*************************************************************")
  
    connection.enable()
    output = connection.send_command('show vlan brief | include 50')
    
    if not output:
        print(f"VLAN 50 not found on device {device['host']}")

    print("*************************************************************")
    
    for cmd in commands:
        print(f"Executing command: ** {cmd} ** on device {device['host']}")
        output = connection.send_command(cmd)
        print(output)
        print("-------------------------------------------------------------")
    
    connection.disconnect()