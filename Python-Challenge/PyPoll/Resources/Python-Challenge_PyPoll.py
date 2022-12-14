import os
import csv

file = os.path.join("election_data.csv")

with open(file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    candidate_list = [candidate[2] for candidate in csvreader]

total_votes = len(candidate_list)
cand_info = [[candidate, candidate_list.count(candidate)] for candidate in set(candidate_list)]
cand_info = sorted(cand_info, key=lambda x: x[1], reverse = True)

print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")

for candidate in cand_info:
    percent_votes = (candidate[1] / total_votes) * 100
    print(f"{candidate[0]}: {percent_votes: 6.3f}% ({candidate[1]})")

print("-----------------------------")
print(f"Winner: {cand_info[0][0]}")
print("-----------------------------")
