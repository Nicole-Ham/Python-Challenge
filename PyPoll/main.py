import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("Analysis", "election_analysis.txt")

candidate_votes = {}
candidate_names = []
rowcounter = 0

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        rowcounter = rowcounter + 1
        current_name = row[2]
        if current_name in candidate_names: 
            candidate_votes[current_name] = candidate_votes[current_name] +1
        else: 
            candidate_votes[current_name] = 1
            candidate_names.append(current_name)
    
print("Election Results")
print("------------------")
print(f"Total Votes:   {rowcounter:,}")
print("------------------")

winning_candidate = ""
winning_votes = 0
candidate_ouput = ""

for name in candidate_names:
    votes = candidate_votes[name] #using final tallies from block 1 - extracting the total number per candidate from the block before
    percentage = float(votes)/float(rowcounter) *100
    if votes > winning_votes: 
        winning_votes = votes
        winning_candidate = name
       
    candidate_output =f"{name}: {percentage:.2f}% {votes}"
    print(candidate_output)
      

print("------------------")
print(f"Winner:   {winning_candidate}")
print("------------------")

with open(output_path, "w") as txt_file: #w: write r: read (open function/method)
    txt_file.write(f"""    Election Results \n
    -------------------------------- \n
    Total Votes: {rowcounter:,}\n
    """)

    for name in candidate_names:
        votes = candidate_votes[name] #using final tallies from block 1 - extracting the total number per candidate from the block before
        percentage = float(votes)/float(rowcounter) *100
        if votes > winning_votes: 
            winning_votes = votes
            winning_candidate = name

        candidate_output =f"{name}: {percentage:.2f}% {votes}"
        txt_file.write(f"""{candidate_output}\n """)

    txt_file.write(f""" -------------------------------- \n     Winner: {winning_candidate}""")