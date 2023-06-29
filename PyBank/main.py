import os
import csv

# file system path to open the data we will be pulling from, basically setting up a way for the two files to talk'
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    dictionary ={} 
    money = 0
    rowcounter = 0
    previous_value = 0
# want to keep inside with statement so python knows to keep using within the open file'
    for row in csvreader:
        rowcounter = rowcounter + 1
        money = money + int(row[1])

        if rowcounter != 1:
            profitloss = int(row[1]) - previous_value
            dictionary[row[0]] = profitloss
        previous_value = int(row[1])

print()
print("Financial Anaylsis")
print()
print("---------------------------------")
print()
print(f"Total Months: {rowcounter}")
print(f"Total: ${money:,}")
print(f"Average Change: ${sum(dictionary.values())/(rowcounter-1):.2f}") 
#-1 because we dont want to include the first line because its where it started

months_list = list(dictionary.keys())
profit_loss_list = list(dictionary.values())
lowest_value = min(profit_loss_list)
lowest_index = profit_loss_list.index(lowest_value)
lowest_month = months_list[lowest_index]
highest_value = max(profit_loss_list)
highest_index = profit_loss_list.index(highest_value)
highest_month = months_list[highest_index]

print(f"Greatest Increase in Profits: {highest_month} $({highest_value:,})")
print(f"Greatest Decrease in Profits: {lowest_month}  $({lowest_value:,})")
print()

file_to_output = os.path.join("analysis", "budget_analysis.txt")

with open(file_to_output, "w") as txt_file:
    txt_file.write(f"""    Financial Anaylsis \n
    -------------------------------- \n
    Total Months: {rowcounter}\n
    Total: ${money:,}\n
    Average Change: ${sum(dictionary.values())/(rowcounter-1):.2f}\n
    Greatest Increase in Profits: {highest_month} $({highest_value:,})\n
    Greatest Decrease in Profits: {lowest_month}  $({lowest_value:,})""")

