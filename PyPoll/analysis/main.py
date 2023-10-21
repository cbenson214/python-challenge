# Import modules needed to read the csv file
import os
import csv

# Set variables for analysis and lists to store data
total_votes = 0
candidates = []
vote_tracker = [0, 0, 0]

# Store, open, and read the csv file
csvpath = os.path.join("..", "Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read header row
    csv_header = next(csvreader)
    
    # Reading the rows , for each row...
    for row in csvreader:

        # Count number of votes in data set
        total_votes = total_votes + 1

        # Gather unique candidate names
        candidates.append(row[2])
        candidates = list(set(candidates))
        

# Store, open, and read the csv file
csvpath = os.path.join("..", "Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read header row
    csv_header = next(csvreader)
    
    # Run through rows again, this time with the candidate list set so we can tally votes
    for row in csvreader:

        # compare each vote to the candidates list and adjust the corresponding votes list by adding 1
        if row[2] == candidates[0]:
            vote_tracker[0] += 1
        elif row[2] == candidates[1]:
            vote_tracker[1] += 1
        else:
            vote_tracker[2] += 1

# Calculate percentage of votes for each candidate
vote_percent1 = round((float(vote_tracker[0])/float(total_votes)) * 100, 3)
vote_percent2 = round((float(vote_tracker[1])/float(total_votes)) * 100, 3)
vote_percent3 = round((float(vote_tracker[2])/float(total_votes)) * 100, 3)

vote_percentage = [vote_percent1, vote_percent2, vote_percent3]

# Set winner based on popular vote
if vote_tracker[0] > vote_tracker[1] and vote_tracker[2]:
    winner = candidates[0]
if vote_tracker[1] > vote_tracker[0] and vote_tracker[2]:
    winner = candidates[1]
if vote_tracker[2] > vote_tracker[0] and vote_tracker[1]:
    winner = candidates[2]

# Output results to Terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print(candidates[0] + ": " + str(vote_percentage[0]) + "% (" + str(vote_tracker[0]) + ")")
print(candidates[1] + ": " + str(vote_percentage[1]) + "% (" + str(vote_tracker[1]) + ")")
print(candidates[2] + ": " + str(vote_percentage[2]) + "% (" + str(vote_tracker[2]) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

# Output results to txt file
txt = open("PyPoll.txt", "w")
print("Election Results", file=txt)
print("-------------------------", file=txt)
print("Total Votes: " + str(total_votes), file=txt)
print("-------------------------", file=txt)
print(candidates[0] + ": " + str(vote_percentage[0]) + "% (" + str(vote_tracker[0]) + ")", file=txt)
print(candidates[0] + ": " + str(vote_percentage[1]) + "% (" + str(vote_tracker[1]) + ")", file=txt)
print(candidates[0] + ": " + str(vote_percentage[2]) + "% (" + str(vote_tracker[2]) + ")", file=txt)
print("-------------------------", file=txt)
print("Winner: " + winner, file=txt)
print("-------------------------", file=txt)
