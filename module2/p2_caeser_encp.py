'''
Program for Caeser Encription
'''
def encription(strin, shift_key, direction):
    """
    Function to encript the text
    """
    string = " "
    for char in (strin):
        if char == " ":
            string = string + char
        elif direction == 1:
            if char.isupper():
                string = string + chr((ord(char)+shift_key - 65)%26 + 65)
            else:
                string = string + chr((ord(char)+shift_key - 97)%26 + 97)
        elif direction == 2:
            if char.isupper():
                string = string + chr((ord(char)-shift_key - 65)%26 + 65)
            else:
                string = string + chr((ord(char)-shift_key - 97)%26 + 97)

    return string

if __name__ == "__main__":
    user_string = input("Enter your string: ")
    shift_direction = int(input("Enter shift direction:\n Press 1 for RIGHT\n press 2 for LEFT\n"))
    if shift_direction not in (1, 2):
        print("Error in direction")
    else:
        shift = int(input("Enter your shift value: "))
        print("Your encripted message is: ", encription(user_string, shift, shift_direction))
