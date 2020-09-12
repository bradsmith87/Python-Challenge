
import sys
import csv
import os

pl_changes = []
months = []

count_months = 0
# Net profit loss
net_pl = 0
#previous month profits/loss
pm_pl = 0
#current month profits/loss
cm_pl = 0
#profits/loss change
pl_change = 0


csvinput = os.path.join(os.path.dirname(sys.path[0]), "PyBank", "Resources", "budget_data.csv")


with open(csvinput, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    for row in csvreader:
        count_months += 1
        cm_pl = int(row[1])
        net_pl += cm_pl
       
        if (count_months == 1):
            pm_pl = cm_pl
          
        else:
            pl_change = cm_pl - pm_pl
            months.append(row[0])
            pl_changes.append(pl_change)
            pm_pl = cm_pl

sum_pl = sum(pl_changes)
a_pl = round(sum_pl / (count_months -1),2)

highest = max(pl_changes)
lowest = min(pl_changes)

high_index = pl_changes.index(highest)
low_index = pl_changes.index(lowest)

high = months[high_index]
low = months[low_index]

output = (
    f"financial Analysis\n"
    "-------------------------------\n"
    f"total months: {count_months}\n"
    f"Total: ${net_pl}\n"
    f"Average Change ${a_pl}\n"
    f"greatest Increase in profits: {high} (${max(pl_changes)})\n"
    f"greatest Decrease in profits: {low} (${min(pl_changes)})")

print(output)
Output_path = os.path.join(os.path.dirname(sys.path[0]), "PyBank", "Analysis", "Financial_Analysis.txt")
f = open(Output_path, "w")
f.write(output)
f.close()