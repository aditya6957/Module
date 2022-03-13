def permutation(lst):

	if len(lst) == 0:
		return []

	if len(lst) == 1:
		return [lst]

	l = []

	for i in range(len(lst)):
	    m = lst[i]
        # remLst = remaning list
	    remLst = lst[:i] + lst[i+1:]

	    for p in permutation(remLst):
		    l.append([m] + p)
	return l

YourList = list(input("array elements :").strip().split())
for p in permutation(YourList):
	print (p)