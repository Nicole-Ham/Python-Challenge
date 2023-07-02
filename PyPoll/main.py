import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    
    names = {}
    rowcounter = 0

    for row in csvreader:
        rowcounter = rowcounter + 1
    
    print("Election Results")
    print("------------------")
    print(f"Total Votes:   {rowcounter:,}")
    print("------------------")
                            
# candidate_name1 = "Charles Casper Stockham"
#     candidate_name2 = "Raymon Anthony Doane"
#     candidate_name3 = "Diana DeGette"
#how would i do this if i dont know the names and it not possible to scroll thru data
    # def sum(total): 
    #     total_sum = 0
    #     for number in total:
    #         total_sum = total_sum + number
        
    #     print(total)


    # if candidate_name1 in names: 
    #     names[candidate_name1] = names[candidate_name1] +1
    # else: 
    #     names[candidate_name1] = 1

    # print(names)

# Use dictionary, the key - candidate name and votes
# If name for first time then you add to dictionary
# Figure out the percentages