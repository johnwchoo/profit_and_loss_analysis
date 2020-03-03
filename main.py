

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period


import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# parameters
total_months = 0
months_changes = []
changes = []
greatest_increase = ["",0] # date & number
greatest_decrease = ["",99999999] # date & number 9999999 is represents the limit of decrease
total = 0

with open(csvpath, newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')

	
	header = next(csvreader) 
	first_row = next(csvreader)


# ----------------------------------------------------------------
	total_months = total_months + 1
	total = total + int(first_row[1])
	previous_month = int(first_row[1])

	for row in csvreader:
		total_months = total_months + 1
		total = total + int(row[1]) # not called first_row becasue it's already "used"
		change = int(row[1]) - previous_month # current_month - previous_month
		previous_month = int(row[1]) # Apr-2010 doesn't have anything that comes before it to subtract from
		changes = changes + [change]
		months_changes = months_changes + [row[0]] # [] around row[0] because it's a list within a list(?)
		
		if change > greatest_increase[1]: 
			greatest_increase[0] = row[0]	#equate it to the first row. Once it changes,take the current row and subtract it from the previous row
			greatest_increase[1] = change

		if change < greatest_decrease[1]:
			greatest_decrease[0] = row[0]
			greatest_decrease[1] = change



# --- Financial Analysis ------------------------------------------------------------
print('')
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: {sum(changes)/len(changes)}')
print(f'Greatest increase in Profits: {greatest_increase}')
print(f'Greatest decrease in Profits: {greatest_decrease}')


#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)
