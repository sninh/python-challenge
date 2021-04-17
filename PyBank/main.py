#open the file
import os

import csv
total = []
date = []
totalintchange =[]

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath, newline='') as csvfile:
#count months in column A and column B turn into integers and add it together
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        date.append(row[0])
        total.append(row[1])

#Get total number of months and the total profit loss 
datecount = len(list(date))   
totalint = [int(i) for i in total]
sumint = sum(totalint)

#calc month over month change
for row in range(1, len(totalint)):
    profitlosschange = totalint[row] - totalint[row - 1]
    totalintchange.append(profitlosschange)
#calc average of month over month change column
sumchange = sum(totalintchange)
lengthchange = len(totalintchange)
averagechange = round((sumchange/lengthchange), 2)
#min and max profit and loss
maxchange = max(totalintchange)
minchange = min(totalintchange)

#find the row that the min and max are in and return the value from the first column and add 1 
maxrow = totalintchange.index(maxchange)
minrow = totalintchange.index(minchange)

maxposition = date[maxrow + 1]
minposition = date[minrow + 1]

#print the info
homeworkinfo = print(f'''
Financial Analysis
------------------
Total Months {datecount}
Total: ${sumint}
Average  Change: ${averagechange}
Greatest Increase in Profits: {maxposition} ${maxchange}
Greatest Decrease in Profits: {minposition} ${minchange}''')

#open a txt file
txt_path = os.path.join("analysis", "pybanktxt.txt")
with open(txt_path, "w") as textfile:
    textfile.write(f'''
    Financial Analysis
    ------------------
    Total Months {datecount}
    Total: ${sumint}
    Average  Change: ${averagechange}
    Greatest Increase in Profits: {maxposition} ${maxchange}
    Greatest Decrease in Profits: {minposition} ${minchange}''')



