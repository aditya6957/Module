
import yaml
import json
json_data = {}
file_name = "sample2[4053]"
with open(file_name+".yaml", "r") as s, open(file_name+".json", "w") as d:
    try: 
        data1 = yaml.safe_load(s)
        json.dump(data1, d)
    except:
        print(f"There is some error in {file_name}.yaml file.")


    