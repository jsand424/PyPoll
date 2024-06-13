import csv
import os

# Path to the CSV file
file_path = os.path.join("Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}

# Read the CSV file
with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    
    # Process each row
    for row in reader:
        total_votes += 1
        candidate = row['Candidate']
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate percentage of votes for each candidate
candidate_percentages = {}
for candidate, votes in candidates.items():
    candidate_percentages[candidate] = (votes / total_votes) * 100

# Determine the winner
winner = max(candidates, key=candidates.get)

# Print the results
print(f"Total Votes: {total_votes}")
print("Candidates who received votes:")
for candidate in candidates:
    print(candidate)
print("Percentage of votes each candidate won:")
for candidate, percentage in candidate_percentages.items():
    print(f"{candidate}: {percentage:.3f}%")
print("Total number of votes each candidate won:")
for candidate, votes in candidates.items():
    print(f"{candidate}: {votes}")
print(f"Winner of the election: {winner}")

output_file_path = os.path.join("Analysis/Election_Results.txt")
with open(output_file_path, mode='w') as file:
    file.write("Election Results\n")
    file.write("----------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("----------------------\n")
    for candidate, votes in candidates.items():
        percentage = candidate_percentages[candidate]
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("----------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("----------------------\n")
