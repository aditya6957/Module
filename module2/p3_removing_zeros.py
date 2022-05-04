'''
Program to remove leading zeros from a given ip address
'''

def leading_zero_remover(ip_address):
    '''
    Function to remove leading zeros from a given ip address
    '''
    ip_address = ip_address.split(".")
    new_ip = ""
    temp_ip = []
    for i in ip_address:
        temp_ip.append(str(int(i)))
    new_ip += ".".join(temp_ip)
    return new_ip

if __name__ == "__main__":
    ip_add = input("Enter your ip: ")
    print(leading_zero_remover(ip_add))
