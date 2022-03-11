import os
import csv

#File Path CSV file in PyPollcsv

PyPollcsv = os.path.join("Resources","election_data.csv")

# Lists 

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# path
 
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Conduct the ask
    for row in csvreader:
        # Total Votes
        count = count + 1
        # Names to List
        candidatelist.append(row[2])
        # Set Unique Name from canidate list
    for x in set(candidatelist):
        unique_candidate.append(x)
        # votes / candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # % of votes / candidate
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    
#Output
 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(round(vote_percent[i],3)) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")





