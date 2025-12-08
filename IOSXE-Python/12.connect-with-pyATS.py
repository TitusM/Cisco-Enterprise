from pyats.topology import loader

# Load the testbed file
testbed = loader.load('testbed.yaml')

device = testbed.devices['SW-1']
# Connect to the device
device.connect()
print(f"Connected to {device.name} successfully!")
print("************************************************")

output = device.execute('show ip interface brief | in up')
#print(output)
print("************************************************")


config_commands = [
    'interface Hu1/0/1',
    'description Connected to SW-2',
    'no shutdown'
]
device.configure(config_commands)
print("Configuration applied successfully!")
print("************************************************")