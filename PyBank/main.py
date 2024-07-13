import os
import csv

# path to csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Initializing variables
total_months = 0
net_total = 0
previous_profit = None
changes = []
dates = []
greatest_increase = ("", 0)
greatest_decrease = ("", 0)

# Read the csv files
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        # Extract date and profit/loss
        date = row[0]
        profit = int(row[1])
        
        #Count total months and net total
        total_months += 1
        net_total += profit
        
        # Calculate changes in profit/loss
        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)
            dates.append(date)
            
            # Check for greatest increase
            if change > greatest_increase[1]:
                greatest_increase = (date, change)
            
            # Check for greatest decrease
            if change < greatest_decrease[1]:
                greatest_decrease = (date, change)
        
        # Update previous profit
        previous_profit = profit

# Calculate average change
average_change = sum(changes) / len(changes) if changes else 0

# Output the results
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output to the terminal
print(output)

# Write the output to a text file
output_file_path = 'financial_analysis.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write(output)