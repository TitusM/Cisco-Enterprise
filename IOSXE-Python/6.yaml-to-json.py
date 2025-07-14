import yaml #install pyyaml
import json

#load the contents of the file into a variable using the open() built-in method
yaml_data = open("inventory.yml", "r")

#use the yaml module safe_load() method to load the contents of the file and assign the output to a new variable named data:
data = yaml.safe_load(yaml_data)

#check the type of data
print(type(data)) #<class 'dict'>


#convert YAML to JSON.
print(json.dumps(data, indent=4))