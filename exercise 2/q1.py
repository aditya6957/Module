## convert-os.py
## Import the modules to handle JSON & YAML
import yaml
import json

## Create a variable to hold the data to import
os_list = {}

## Read the YAML file
with open("sample1[4051].yaml") as infile:
    os_list = yaml.load(infile, Loader=yaml.FullLoader)
    print(os_list)

#Open a file to write the JSON output. The 'w' makes the file writable
#with open("c:\temp\python_operating-systems.json", 'w') as outfile:
     # Marshall the JSON, setting "indent" makes the file more readable json.dump(os_list, outfile, indent=4) print("JSON file written.")