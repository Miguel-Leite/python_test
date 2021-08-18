import csv

with open('data.csv','r') as csv_file:

    reader = csv.reader(csv_file)

    for row in reader:
        # print(row[0])
        print(row)