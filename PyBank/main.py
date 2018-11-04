import os
import csv

# Path to collect data from the Resources folder
pybankCsv = os.path.join('..','..','UTAUS201810DATA2','Python','Homework','Instructions','PyBank', 'Resources', 'budget_data.csv')

# Read in the CSV file

with open(pybankCsv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header
    header = next(csvreader)
    
    # Make a list of all rows in csv file after header
    rows=[]
    # Start point to sum the total value
    netvalue=0
    # Start point of previous value profit/loss
    preivousvalue=0
    # Start point to sum the total monthly difference
    total_monthly_diff=0
    # Start point of max value of the list, make it small enough to make the sure first row value will replace this
    Max_value=-99999999999
    # Start point of min value of the list, make it big enough to make the sure first row value will replace this
    Min_value=99999999999
    # Read through each row of data after the header
    for row in csvreader:
        # add the value to list "rows"
        rows.append(row)
        # add the current value to netvalue
        netvalue=netvalue+int(row[1])
        # The greatest increase/decrease in profits (date and amount) over the entire period
        if int(row[1])>Max_value:
            Max_month=row[0]
            Max_value=int(row[1])
        elif int(row[1])<Min_value:
            Min_month=row[0]
            Min_value=int(row[1])
        

        # The monthly difference is the current value - previous month value
        monthly_diff=float(row[1])-preivousvalue
        # Sum of all the monthly differnce
        total_monthly_diff=total_monthly_diff+monthly_diff
        # Replace the previous value with current value so it can be used for the calculation from the next row
        preivousvalue=float(row[1])
        
        
    
    # The total net amount of "Profit/Losses" over the entire period
    total_net_amt=round(netvalue,0)
    # The total number of months included in the dataset
    total_num_month=len(rows)
    # The average change in "Profit/Losses" between months over the entire period (When we calculate the monthly diff, the first row was deducted by 0 so we need to deduct the total by the first row value itself)
    avg_change=round((total_monthly_diff-float(rows[0][1]))/(total_num_month-1),2)
    
    
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_num_month}")
    print(f"Total: ${total_net_amt}")
    print(f"Average  Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {Max_month} (${Max_value})")
    print(f"Greatest Decrease in Profits: {Min_month} (${Min_value})")

    with open("Output.txt", "w") as text_file:
        print(f"Financial Analysis\n----------------------------\nTotal Months: {total_num_month}\nTotal: ${total_net_amt}\nAverage  Change: ${avg_change}\nGreatest Increase in Profits: {Max_month} (${Max_value})\nGreatest Decrease in Profits: {Min_month} (${Min_value})", file=text_file)

