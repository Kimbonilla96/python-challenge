import os
import csv

csv_path = os.path.join('Resources', 'election_data.csv')

output_path = "result.txt"

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    data = list(csvreader)
    
    with open(output_path, 'w') as output_file:
        output_file.write("Election Results\n")
        output_file.write("------------------------------\n")
        total_votes = 0
        candidate_votes = {}
        
        for row in data:
            total_votes += 1
            candidate = row[2]  # Assuming column index 2 holds candidate names
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1
            
        output_file.write(f"Total Votes: {total_votes}\n")
        output_file.write("------------------------------\n")
    
        max_votes = 0
        winner = ""
    
        for candidate, votes in candidate_votes.items():
            total_percentage_of_votes = (votes / total_votes) * 100
            output_file.write(f'{candidate}: {total_percentage_of_votes:.3f}% ({votes})\n')
            
            if votes > max_votes:
                max_votes = votes
                winner = candidate 

        output_file.write("------------------------------\n")
        output_file.write(f"Winner: {winner}\n ")
    
        