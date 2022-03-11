import os
import csv

#File Path CSV file in PyBankcsv

PyBankcsv = os.path.join("Resources","budget_data.csv")

# Lists 

profit = []
monthly_changes = []
date = []

# Variables
 
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

# Open the CSV using the set path PyBankcsv

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # month count
    for row in csvreader:    
      # Use count to count the number months in this dataset
      count = count + 1 

      # profits greatest increase vs. greatest decrease
      date.append(row[0])

      # Total Profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      #Average Change in Profit
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

      #Add Change to List
      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit

      #Average Change in Profits
      average_change_profits = (total_change_profits/count)
      
      #Highs vs. Lows in date changes
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
   





