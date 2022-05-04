'''
Program for module 2, problem 1
'''

def csv_calculator(data_list, time_list):
    '''
    Function to find mean, max, min, time for a given list
    '''
    stripped_data_list = [elem.strip('%') for elem in data_list]
    mean = round(sum(float(t) for t in stripped_data_list)/len(stripped_data_list), 2)
    max_value = max(stripped_data_list)
    min_value = min(stripped_data_list)
    max_time = (data_list.index(max(data_list)))
    min_time = (data_list.index(min(data_list)))
    key = {"max_time": time_list[max_time],"min_time": time_list[min_time], "max": max_value ,
    "min": min_value, "mean": mean}
    return key

if __name__ == "__main__":
    time = []
    CPU_Util = []
    RAM_Util = []
    with open('module2_1 - Sheet1.csv') as csv_data_file:
        csv_data = csv_data_file.readlines()
        for row in csv_data[1:]:
            row=row.split(',')
            time.append(row[0])
            CPU_Util.append(row[1].strip())
            RAM_Util.append(row[2].strip())
        print("CPU_Util", csv_calculator(CPU_Util, time))
        print("RAM_Util",csv_calculator(RAM_Util, time))
