import os
import csv

# Define path
election_csv = os.path.join("Resources", "election_data.csv")

# Read in the CSV file
with open(election_csv, "r") as infile:
    rows = csv.reader(infile)
    header = next(rows)

    # Define variables
    votes_cast_total = 0
    candidates_votes = {}  # Dictionary to store votes per candidate
    candidates_list = []   # List to store unique candidates

    # Loop through the data
    for row in rows:
        # Count total votes
        votes_cast_total += 1

        # Add candidate to the list of unique candidates
        candidate = row[2]
        if candidate not in candidates_list:
            candidates_list.append(candidate)

        # Update the dictionary with the total votes for each candidate
        if candidate in candidates_votes:
            candidates_votes[candidate] += 1
        else:
            candidates_votes[candidate] = 1

# Print the total votes
print(f"Total Votes: {votes_cast_total}")

# Print the unique list of candidates
print("List of Candidates:", candidates_list)

# Print the total votes for each candidate
print("Votes per Candidate:", candidates_votes)

# Calculate and print the percentage of votes for each candidate
print("Percentage of Votes:")
for candidate, votes in candidates_votes.items():
    
    percentage = round((votes / votes_cast_total) * 100, 3)
    print(f"{candidate}: {percentage}% ({votes})")

# Determine the winner based on the maximum votes
winner = max(candidates_votes, key=candidates_votes.get)
print(f"Winner: {winner}")



# Construct the output to text file
output = f"""
Election Results
-------------------------
Total Votes: {votes_cast_total}
-------------------------
"""

# Loop through the results and add each candidate's line
for candidate, votes in candidates_votes.items():
    percentage = round((votes / votes_cast_total) * 100, 3)
    output += f"{candidate}: {percentage}% ({votes})\n"

output += f"-------------------------\nWinner: {winner}\n"

print(output)

# Write the output to a text file
with open("Analysis/pypoll_analysis.txt", "w") as outfile:
    outfile.write(output)