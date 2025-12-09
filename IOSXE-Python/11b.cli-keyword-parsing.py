from netmiko import ConnectHandler

# Define the devices to connect to
devices = [
    {
        'device_type': 'cisco_ios',
        'host': '10.1.1.1',
        'username': 'admin',
        'password': 'devnet',
        'secret': 'devnet'
    },
    {
        'device_type': 'cisco_ios',
        'host': '10.2.2.2',
        'username': 'admin',
        'password': 'devnet',
        'secret': 'devnet'
    },
]

# Print header
print("\n" + "=" * 80)
print("NETWORK DEVICE INTERFACE STATUS CHECK".center(80))
print("=" * 80 + "\n")

for device in devices:
    connection = ConnectHandler(**device)

    print(f"\n{'=' * 80}")
    print(f"Device: {device['host']}")
    print(f"{'=' * 80}")
    print(f"Status: Connected successfully")
    print(f"{'-' * 80}")

    connection.enable()
    output = connection.send_command('show interface | in GigabitEthernet0/0')
    log_output = connection.send_command('show logging | include %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0')

    # Check interface status
    print(f"\nChecking GigabitEthernet0/0 status...")
    
    if "line protocol is up" in output:
        print(f"Result: GigabitEthernet0/0 is UP")
    else:
        print(f"Result: GigabitEthernet0/0 is DOWN")
        
    # Print log output related to interface status changes
    flap_count = log_output.count('changed state to down')
    print(f"\nLog Summary: GigabitEthernet0/0 changed state to down {flap_count} times.")

    print(f"\n{'-' * 80}")
    print(f"Connection to {device['host']} closed")
    print(f"{'=' * 80}\n")

    connection.disconnect()
