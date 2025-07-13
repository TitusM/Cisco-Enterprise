import xmltodict
import json

with open("inventory.xml") as xml_file:
    xml = xmltodict.parse(xml_file.read())
    

print(json.dumps(xml, indent=4))

#Replace @ symbol infront of "name" & "attribute" objects - Option-1

print(json.dumps(xml, indent=4).replace("@", ""))

#Replace @ symbol infront of "name" & "attribute" objects - Option-2
with open("inventory.xml") as xml_file:
    xml_new = xmltodict.parse(xml_file.read(), attr_prefix='')
    
print(json.dumps(xml_new, indent=4))