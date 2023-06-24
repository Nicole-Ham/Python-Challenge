import os
import csv

# file system path to open the data we will be pulling from, basically setting up a way for the two files to talk'
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    rowcounter = 0
# want to keep in with statement so python knows to keep using within the open file'
    for row in csvreader:
        print(row[0])
        rowcounter = rowcounter + 1

print(rowcounter)
