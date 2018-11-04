import os
import csv

# Path to collect data from the Resources folder
pybankCsv = os.path.join('..','..','UTAUS201810DATA2','Python','Homework','Instructions','PyBank', 'Resources', 'budget_data.csv')

# Read in the CSV file

with open(pybankCsv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    

    rows=[]
    netvalue=0
    preivousvalue=0
    total_monthly_diff=0
    Max_value=-99999
    Min_value=99999
    # Read through each row of data after the header
    for row in csvreader:
        rows.append(row)
        netvalue=netvalue+float(row[1])
        # The greatest increase/decrease in profits (date and amount) over the entire period
        if int(row[1])>Max_value:
            Max_month=row[0]
            Max_value=int(row[1])
        elif int(row[1])<Min_value:
            Min_month=row[0]
            Min_value=int(row[1])
        


        monthly_diff=float(row[1])-preivousvalue
        total_monthly_diff=total_monthly_diff+monthly_diff
        preivousvalue=float(row[1])
        
        
    
    # The total net amount of "Profit/Losses" over the entire period
    total_net_amt=netvalue
    # The total number of months included in the dataset
    total_num_month=len(rows)
    # The average change in "Profit/Losses" between months over the entire period
    avg_change=(total_monthly_diff-float(rows[0][1]))/(total_num_month-1)
    
    
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_num_month}")
    print(f"Total: ${total_net_amt}")
    print(f"Average  Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {Max_month} (${Max_value})")
    print(f"Greatest Decrease in Profits: {Min_month} (${Min_value})")

    
