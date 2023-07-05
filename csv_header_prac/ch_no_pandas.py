#Here I'm renaming a csv file's headers without using pandas
import csv

with open('csv_raw.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

    new_headers = ['Header_1','Header_2','Header_3','Header_4','Header_5']
    rows[0] = new_headers

with open('changed_with_csv.csv', 'w') as file:
    writer = csv.writer(file)
    for i in rows:
        writer.writerow(i)