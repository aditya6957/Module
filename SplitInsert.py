def insert_sting_middle(str, word):
    print(str[:len(str)//2]+word+str[len(str)//2:])

yourstring = input("Enter your string: \n")
word = input("Enter what you want to insert: \n")
insert_sting_middle(yourstring, word)
