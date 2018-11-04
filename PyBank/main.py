import os
import csv

# Path to collect data from the Resources folder
pybankCsv = os.path.join('..','..','UTAUS201810DATA2','Python','Homework','Instructions','PyBank', 'Resources', 'budget_data.csv')

# Read in the CSV file

with open(pybankCsv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    print(header)

    rows=[]
    netvalue=0
    # Read through each row of data after the header
    for row in csvreader:
        rows.append(row)
        netvalue=netvalue+float(row[1])
    print(rows)
    # The total net amount of "Profit/Losses" over the entire period
    print(netvalue)
    # The total number of months included in the dataset
    print(len(rows))
    
