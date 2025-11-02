import yaml

with open('data.yml', 'r') as file:
    data = yaml.safe_load(file) #Converting a YAML file to a Python dictionary
    print(data)

switchname = data['hostname']

print(f"contact: {data['snmp']['contact']}")

for vlan in data['vlans']:
    vlan_id = vlan['id']
    vlan_name = vlan['name']
    print(f"VLAN ID: {vlan_id}, VLAN Name: {vlan_name}")

for readonly in data['snmp']['ro']:
    print(readonly)

data['snmp']['location'] = 'Krakow' #Modifying a value in the dictionary

with open('yaml-from-dict.yml', 'w') as file:
    yaml.dump(data, file) #Converting a Python dictionary back to a YAML file