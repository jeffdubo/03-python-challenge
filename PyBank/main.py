import os
import csv
from pickle import EMPTY_LIST

budget_csv = os.path.join('Resources', 'budget_data.csv')

# Lists to store information 
month = []
profit_loss = []
change = []
analysis_lines = []

# Initialize variables to 0
previous_profit_loss = 0
total_profit_loss = 0

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header row  
    next(csvreader, None)

    for row in csvreader:
        # Store month in list
        month.append(row[0])
        
        # Store profit/loss in list
        profit_loss.append(row[1])

        # Calculate change in profit/loss from previous month
        change.append(int(row[1]) - previous_profit_loss)

        # Track total profit/lass
        total_profit_loss += int(row[1])

        # Update previous month profit/loss
        previous_profit_loss = int(row[1])

# Set first centry to 0 as there was no previous month to calculate change
change[0] = 0 

# Zip up data
budget_data = zip(month, profit_loss, change)

# Store number of months
total_months = len(month)

# Initialize variables to 0 
total_change = 0
max_increase = 0
max_decrease = 0

# Loop through all data
for entry in budget_data:
    total_change += entry[2]
    
    # Update greatest increase and month if current entry is greater than previous greatest
    if entry[2] > max_increase:
        max_increase = entry[2]
        month_max_increase = entry[0]
    
    # Update greatest decrease and month if current entry is less than previous greatest
    elif entry[2] < max_decrease:
        max_decrease = entry[2]
        month_max_decrease = entry[0]

# Calculate average change excluding the first row in the total number months 
average_change = round(total_change / (total_months - 1),2)

# Store analysis in list, add blank lines for display
analysis_lines.append("Financial Analysis")
analysis_lines.append("")
analysis_lines.append("----------------------------")
analysis_lines.append("")
analysis_lines.append(f"Total Months: {total_months}")
analysis_lines.append("")
analysis_lines.append(f"Total: ${total_profit_loss}")
analysis_lines.append("")
analysis_lines.append(f"Average Change: ${average_change}")
analysis_lines.append("")
analysis_lines.append(f"Greatest Increase in Profits: {month_max_increase} $({max_increase})")
analysis_lines.append("")
analysis_lines.append(f"Greatest Decrease in Profits: {month_max_decrease} $({max_decrease})")

# Print analysis to terminal
for line in analysis_lines:
    print(line)

# Zip to export to file
analysis = zip(analysis_lines)

# Export results to txt file
output_path = os.path.join("analysis", "analysis.txt")

with open(output_path, 'w', newline='') as outfile:
    csvwriter = csv.writer(outfile)

    for line in analysis:
        # If a blank/empty row, write it manually 
        if line[0] == "":
            csvwriter.writerow("")
        else:
            csvwriter.writerow(line)
        