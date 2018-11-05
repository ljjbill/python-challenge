import os
import csv

# Path to collect data from the Resources folder
pyPollCsv = os.path.join('..','..','UTAUS201810DATA2','Python','Homework','Instructions','PyPoll', 'Resources', 'election_data.csv')

# Read in the CSV file

with open(pyPollCsv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header
    header = next(csvreader)
    
    # Make a vote pool that will contain all the votes (candidates name)
    votes=[]
    # Make a list that will contain all the candidates' names
    candidates=[]
    # Make a list that will contain the total votes for each candidates, in the order of candidates list
    votecounter=[]
    # Make a list that will contain the % of total votes for each candidates, in the order of candidates list
    votepercent=[]
    
    # Read through each row of data after the header

    for row in csvreader:
        # add the name of each vote into the vote pool
        votes.append(row[2])

    # Add all the candidate name into the candidates list, each candidate only appears once in the candidates list
    for vote in votes:
        if vote in candidates:
            pass
        else:
            candidates.append(vote)
    # Get the numbers of candidates
    candidate_count=len(candidates)
    # Get the numbers of votes
    Total_votes=float(len(votes))
   
    # Get the total votes for each candidates, in the order of candidates list, add the total numbers into votecounter list
    for x in range(candidate_count):
        votecounter.append(int(votes.count(candidates[x])))
    # Get the percentage of total for each candidates, in the order of candidates/votecounter list, add the percentage into votepercent list
    for count in votecounter:
        percentage=round((count/Total_votes)*100,3)
        votepercent.append(percentage)
    
# get the index of winner in each list
    winne_index=votecounter.index(max(votecounter))
# print results in terminal
    print("Election Results\n-------------------------")
    print(f"Total Votes: {int(Total_votes)}")
    print("-------------------------")
    # print the result for each candiate, fetch the data from each of the candidates, votepercent and votecounter list
    for i in range(candidate_count):
        print(f"{candidates[i]}: {votepercent[i]}% ({votecounter[i]})")

    print("-------------------------")
    print(f"Winner: {candidates[winne_index]}")
    print("-------------------------")

 # print results to txt file   
with open("Output.txt", "w") as text_file:
    print("Election Results\n-------------------------", file=text_file)
    print(f"Total Votes: {int(Total_votes)}", file=text_file)
    print("-------------------------", file=text_file)

    for i in range(candidate_count):
        print(f"{candidates[i]}: {votepercent[i]}% ({votecounter[i]})", file=text_file)

    print("-------------------------", file=text_file)
    print(f"Winner: {candidates[winne_index]}", file=text_file)
    print("-------------------------", file=text_file)

        
        
    
   