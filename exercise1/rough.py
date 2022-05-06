input ='''device1   vlan1
				device2   vlan2
				device3   vlan1
				device2   vlan3
				device1   vlan4
				device2   vlan1
				device3   vlan6'''

initial_list = input.split()


def list_splitter(sample_list, n):
	# looping till length l
	for i in range(0, len(sample_list), n):
		yield sample_list[i:i + n]

final_list = list(list_splitter(initial_list, 2))

d = {}
for key, value in final_list:
   if key not in d.keys():
      d[key] = [key]
   d[key].append(value)
result = list(d.values())
print(d)
items = {}
for line in result:
    key, value = line[0], line[1:]
    items[key] = value
print(items)

# itemDict = {item[0]: item[1:] for item in items}

