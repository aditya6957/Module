'''
Program to add two dictionaries with common keys
'''
def dict_adder(dict_a, dict_b):
    '''
    defined function for dictionary addition
    '''
    for key in dict_b:
        if key in dict_a:
            dict_b[key] = dict_b[key] + dict_a[key]
        else:
            pass
    res = dict_a | dict_b
    print(res)

if __name__ == "__main__":
    d1 = {'a': 100, 'b': 200, 'c':300}
    d2 = {'a': 300, 'b': 200, 'd':400}
    dict_adder(d1, d2)
