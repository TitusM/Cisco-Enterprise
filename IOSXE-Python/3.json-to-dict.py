import json

vlan_ids = '{"name":"HR", "id":100}'
interfaces = '["Gig1","Gig2","Gig3"]'

#Confirm that variables are strings
print(type(vlan_ids))
print(type(interfaces))

#Convert objects to a format that Python supports

vlan_nums = json.loads(vlan_ids)
interface_names = json.loads(interfaces)


#Confirm that variables are dicts
print(type(vlan_nums))


#Confirm that variables are list
print(type(interface_names))


#Access values from the dictionary
print(vlan_nums["id"])
print(interface_names[0])