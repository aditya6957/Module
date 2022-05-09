import yaml
import json

## Create a variable to hold the data to import
os_list = {}

## Read the YAML file
with open("sample2[4053].yaml") as infile:
    os_list = yaml.load(infile, Loader=yaml.FullLoader)
    print(os_list)
    