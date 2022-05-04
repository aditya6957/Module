def csv_2_dict(your_csv):
    import csv
    csv_file = open(your_csv, 'r')
    reader = csv.reader(csv_file)
    job_id = {}
    for row in reader:
        job_id[row[0]] = {'start_time':row[1],'status':row[2],'end_time':row[3],'duration':row[4]}
    return job_id[input('Enter the Job ID you want to search for: ')]
if __name__ == "__main__":
    print(csv_2_dict("p6_output.csv"))



