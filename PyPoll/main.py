import os
import csv

# Path to csv data
csvpath = os.path.join('Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read the csv files
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        # Extract candidate name
        candidate = row[2]
        
        # Count total votes
        total_votes += 1
        
        # Count votes per candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate percentage of votes each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Determine the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Create the output text
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"

output += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print the output to the terminal
print(output)

# Write the output to a text file
output_file_path = 'election_results.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write(output)