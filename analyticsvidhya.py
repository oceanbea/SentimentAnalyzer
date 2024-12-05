import csv
file = open('Dataset.csv')
type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
print (header)