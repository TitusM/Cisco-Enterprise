#This script reads YAML data and displays it in JSON format
import os
import json
import yaml

if __name__ == "__main__":
    if os.path.exists('data.yml'):
        file_handler = open('data.yml','r')
        data = yaml.safe_load(file_handler)
        print(json.dumps(data, indent=4))
        
    else:
        print("Missing required file: data.yml")