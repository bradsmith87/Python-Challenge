
import sys
import csv
import os


candidates = {}
percentages = {}
formatted_list=[]

winner_count = 0


csvinput = os.path.join(os.path.dirname(sys.path[0]), "Pypoll", "Resources", "election_data.csv")
with open(csvinput, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    

    csv_header = next(csvfile)

    for row in csvreader:
        
     
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1


value = candidates.values()
total = sum(value)
for key, value in candidates.items():
    percentages[key] = round((value/total)*100,2)

for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]
for key, value in percentages.items():
    formatted_list= (f"{key} : {value}")

output = ("Election Results\n-------------------------\n"
    f"Total Votes: {str(total)}\n-------------------------\n")
for key, value in candidates.items():
    output += (f"{key} : {percentages[key]}% ({value})\n")

output +=("-------------------------\n"
f"Winner: {winner}\n-------------------------\n")
print(output)

Output_path = os.path.join(os.path.dirname(sys.path[0]), "PyPoll", "Analysis", "Election_results.txt")
f = open(Output_path, "w")
f.write(output)
f.close()
