import os
import csv

candidates = []
votes = []
percent = []
#open file
csvpath = os.path.join("Resources","election_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
#calc total votes
    for row in csvreader:
        votes.append(row[2])
totalvotes = len(votes)

#list of candidates that received votes
for row in votes:
    if row in candidates:
        continue
    else:
        candidates.append(row)


#look for candidate name in votes list and count how many
#first in candidates list
khanvotes = votes.count(candidates[0])
#second in candidates list
correyvotes = votes.count(candidates[1])
#3rd in candidates list
livotes = votes.count(candidates[2])
#4th in candidates list
otooleyvotes = votes.count(candidates[3])
#total number of votes for each candidate
khanpercent = format(100 * khanvotes / totalvotes, '.3f')
correypercent = format(100 * correyvotes / totalvotes, '.3f')
lipercent = format(100 * livotes / totalvotes, '.3f')
otooleypercent = format(100 * otooleyvotes / totalvotes, '.3f')

#winner of election (who received most votes from list?)
winner = max(candidates, key = votes.count)

#print and save it to text file
print(f'''
Election results
----------------
Total Votes: {totalvotes}
----------------
{candidates[0]}: {khanpercent}% ({khanvotes})
{candidates[1]}: {correypercent}% ({correyvotes})
{candidates[2]}: {lipercent}% ({livotes})
{candidates[3]}: {otooleypercent}% ({otooleyvotes})
----------------
Winner: {winner}
----------------
''')
#open text and save it down
txt_path = os.path.join("analysis", "pypolltxt.txt")
with open(txt_path, "w") as textfile:
    textfile.write(f'''
    Election results
    ----------------
    Total Votes: {totalvotes}
    ----------------
    {candidates[0]}: {khanpercent}% ({khanvotes})
    {candidates[1]}: {correypercent}% ({correyvotes})
    {candidates[2]}: {lipercent}% ({livotes})
    {candidates[3]}: {otooleypercent}% ({otooleyvotes})
    ----------------
    Winner: {winner}
    ----------------
    ''')