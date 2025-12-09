from pyats.topology import loader

# Load the testbed file
testbed = loader.load('testbed.yaml')

# Connect to all devices in the testbed
for device_name, device in testbed.devices.items():
    print(f"Connecting to {device.name}...")
    
    device.connect(log_stdout=False)
    
    print(f"Connected to {device.name} successfully!")
    print("************************************************")
    
    vlans = device.parse('show vlan')
    
    print("*****************VLANS from Parser***************************")
    
    if vlans==None:
        print("No Parser Data Found")
    else:
        print(vlans)

    print("=" * 80 + "\n")
    
    device.disconnect()