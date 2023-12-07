import os
import csv


#define path
budget_csv = os.path.join("Resources","budget_data.csv")

# Read in the CSV file
with open(budget_csv, "r") as infile:
    rows = csv.reader(infile)
    header = next(rows)
 
    
    #define variables
    Jan_list = []
    total_months = 0
    total_profit = 0
    total_change = 0
    change_counter = 0
    greatest_increase = 0
    greatest_increase_month = ""
    greatest_decrease = 0
    greatest_decrease_month = ""

    Jan_list = next(rows)
    total_months = total_months + 1
    total_profit = total_profit + int(Jan_list[1])
    prev_profit = int(Jan_list[1])

    
    # Loop through the data
    for row in rows:
      total_months = total_months + 1
      total_profit = total_profit + int(row[1])
      change_counter += 1
      change = int(row[1]) - prev_profit
      total_change += change

      prev_profit = int(row[1])

      if change > greatest_increase:
         greatest_increase = change
         greatest_increase_month = row[0]

      if change < greatest_decrease:
        greatest_decrease = change
        greatest_decrease_month = row[0]

        
print(total_change / change_counter)


output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit}
Average Change: ${total_change / change_counter:.2f}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})
"""

print(output)

with open("Analysis/pybankanalysis.txt","w") as outfile:
    outfile.write(output)
