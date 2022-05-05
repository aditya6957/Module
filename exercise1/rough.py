# Python3 program to Convert a
# list to dictionary

def Convert(lst):
	res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
	return res_dct
		
# Driver code
lst1 = ['device1', 'vlan1', 'device2', 'vlan2', 'device3', 'vlan1', 'device2', 'vlan3', 'device1',
        'vlan4', 'device2', 'vlan1', 'device3', 'vlan6']
#lst = ['a', 1, 'b', 2, 'c', 3]

#print(Convert(lst1))

my_list = ['device1', 'vlan1', 'device2', 'vlan2', 'device3', 'vlan1', 'device2', 'vlan3', 'device1',
        'vlan4', 'device2', 'vlan1', 'device3', 'vlan6']

from collections import defaultdict
new_dict = defaultdict(list)
for (key, value) in my_list:
    new_dict[key].append(value)
print(new_dict)
