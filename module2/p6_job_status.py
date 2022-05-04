import csv
def job_data(your_csv_file):
    your_file = open(your_csv_file, 'r')
    reader = list(csv.reader(your_file))
    all_jobs = []
    all_job_ids = []
    for row in reader[1:]:
        job = {'id': row[1], 'status':row[2]}
        if job.get('status') == 'started':
            job['start_time'] = row[0]

        if job.get('id') in all_job_ids:
            for x_job in all_jobs:
                if x_job.get('id') == job.get('id'):
                    x_job['status'] = job.get('status')
                    if job.get('status').lower() == 'completed':
                        x_job.update({"end_time": row[0]})
                    break

        else:
            all_jobs.append(job)
            all_job_ids.append(job.get('id'))
    print(all_jobs)
if __name__ == "__main__":
    job_data("module2_3 - Sheet1.csv")