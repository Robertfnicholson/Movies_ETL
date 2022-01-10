# Load a json file
import json

with open("Users/rfnichol/OneDrive - COOPER TIRE & RUBBER COMPANY/Personal/Data Analytics Boot Camp/Module_8_ETL/Module_8_files/Movies_ETL/Test.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

product = jsonObject['product']
overall = jsonObject['overall']
text = jsonObject['text']

print(product)
print(overall)
print(text)    