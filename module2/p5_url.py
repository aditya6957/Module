'''
Program to normalise URL and replace repeted numbers with *
'''
import re


def url_normaliser(url_list):
    '''
    Function to normalise URL
    '''
    normalised_url = []
    for num in url_list:
        pattern = r'\d'
        replacement = re.sub(pattern, '*', num)
        # re.sub(to_be_replaced, replaced_with, index in this case, can be any data type)
        normalised_url.append(replacement)
    return normalised_url



if __name__ == "__main__":
    with open('module2_2.txt') as url_data_file:
        url_data_str = url_data_file.read()
        url_data_list = url_data_str.split('\n')
        for i in url_normaliser(url_data_list):
            print(i)

# '''
# Use \d character set to match any single digit.
# Use \w character set to match any single word character.
# Use \s character set to match any whitespace.
# The \D, \W, \S character set are the inverse sets of \d, \w, and \s character set.
# Use the dot character set (.) to match any character but a new line.
# '''
