#This script uses (inventory.xml) as input

import xml.etree.ElementTree as ET

tree = ET.parse('inventory.xml')

#To obtain all data that are assigned to the root key, you can use the getroot() method 
root_data = tree.getroot()

#print root key tag
print(root_data.tag)

#To see all children that belong to root_data
for child in root_data:
    print(child.tag, child.attrib)
    

#You can also find all serial numbers that are part of the production (prod) namespace by using the iter() method with the root_data variable, because it will iterate over all subchild elements 
for serial in root_data.iter("{https://www.cisco.com/ns/routers/prod}serial"):
    print(serial.text)
    
#To see which serial number belongs to which device
for device in root_data.findall("{https://www.cisco.com/ns/routers/prod}device"):
    name= device.attrib['name']
    serial= device.find('{https://www.cisco.com/ns/routers/prod}serial').text
    print(name, serial)

#Print all atributes related to the SNMP element
for snmp in root_data.iter("{https://www.cisco.com/ns/routers/dev}snmp"):
    print(snmp.attrib)