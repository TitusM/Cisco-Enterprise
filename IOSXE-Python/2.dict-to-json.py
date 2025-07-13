import json

#Define a dictionary
facts = {
    "inventory": {
        "device": [
            {
                "name": "csr1kv1",
                "version": "16.09",
                "vendor": "cisco",
                "uptime": "2 days"
            }
        ]
    }
}

#Confirm that variables are dicts
print(type(facts))  # <class 'dict'>

#print(facts["inventory"]["device"][0]["vendor"])

#To convert the Python dictionary to a JSON formatted string - json.dumps()
facts_str = json.dumps(facts, indent=4)

print(facts_str)

#Confirm that variables are now strings
print(type(facts_str))  #<class 'str'>



