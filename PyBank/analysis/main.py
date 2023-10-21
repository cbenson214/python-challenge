# Import modules needed to read the csv file
import os
import csv

# Set variables for analysis and lists to store data
month_count = 0
total_profit_loss = 0
total_change = 0
base = 0
daily_max = 0
daily_min = 0
profit_loss_list = []
date_list = []

# Store, open, and read the csv file
csvpath = os.path.join("..", "Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read header row
    csv_header = next(csvreader)
    
    # Reading the rows now, for each row...
    for row in csvreader:

        # Count number of months in data set
        month_count = month_count + 1

        # Running total of profit_loss data
        total_profit_loss += int(row[1])

        # Capture monthly changes in P&L
        if base != 0:
            change = int(row[1]) - base
            profit_loss_list.append(change)
        
        # Running total of profit_loss changes
            total_change += change

        # Capture the overall max and min profit or loss and its relative date
            if int(change) > int(daily_max):
                daily_max = change
                max_date = row[0]
            if int(change) < int(daily_min):
                daily_min = change
                min_date = row[0]

        # Change base to current row
        base = int(row[1])            

#Find average profit/loss
average_pl = round(int(total_change) / len(profit_loss_list), 2)

# Output results to Terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(total_profit_loss))
print("Average Change: $" + str(average_pl))
print("Greatest Increase In Profits: " + str(max_date) + " ($" + str(daily_max) + ")")
print("Greatest Decrease In Profits: " + str(min_date) + " ($" + str(daily_min) + ")")

# Output results to txt file
txt = open("PyBank.txt", "w")
print("Financial Analysis", file=txt)
print("----------------------------", file=txt)
print("Total Months: " + str(month_count), file=txt)
print("Total: $" + str(total_profit_loss), file=txt)
print("Average Change: $" + str(average_pl), file=txt)
print("Greatest Increase In Profits: " + str(max_date) + " ($" + str(daily_max) + ")", file=txt)
print("Greatest Decrease In Profits: " + str(min_date) + " ($" + str(daily_min) + ")", file=txt)
txt.close()