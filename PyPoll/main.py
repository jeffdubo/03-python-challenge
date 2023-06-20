import os
import csv

election_csv = os.path.join('Resources', 'election_data.csv')

# Lists to store information
votes = [] 
candidates = []
candidate_votes = []
candidate_percent_votes = []
analysis_lines = []

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header row
    next(csvreader, None)

    for row in csvreader:
        # Store name of candidate for each vote
        votes.append(row[2])
        
        # Check if candidate is in list, add if not
        if row[2] not in candidates:
            candidates.append(row[2])
    
    # Store total # of votes
    total_votes = len(votes)    

    # Track highest number of votes
    winner_votes = 0

    # Loop through all candidates
    for candidate in candidates:
        # Get the number of votes for current candidate
        count_votes = votes.count(candidate)
        
        # Store numbber of votes
        candidate_votes.append(count_votes)

        # Calcuate and store % of total votes, round to 3 decimal places
        candidate_percent_votes.append(round(count_votes / total_votes * 100, 3))
        
        # Store votes and name if votes are greater than current winning votes
        if count_votes > winner_votes:
            winner_votes = count_votes
            winner_name = candidate
          
# Zip up lists to easily store and print indivdual candidate info
candidate_results = zip(candidates, candidate_votes, candidate_percent_votes)

# Store title and total votes in list, add blank lines for display
analysis_lines.append("Election Results")
analysis_lines.append(" ")
analysis_lines.append("----------------------------")
analysis_lines.append("")
analysis_lines.append(f"Total Votes: {total_votes}")
analysis_lines.append("")
analysis_lines.append("----------------------------")
analysis_lines.append("")

# Store individual candiate info for printout and export 
for row in candidate_results:
    analysis_lines.append(f"{row[0]}: {row[2]}% ({row[1]})")
    analysis_lines.append("")

# Store winner in list
analysis_lines.append("----------------------------")
analysis_lines.append("")
analysis_lines.append(f"Winner: {winner_name}")
analysis_lines.append("")
analysis_lines.append("----------------------------")

# Print analysis to terminal
for line in analysis_lines:
    print(line)
 
# Zip to export to file
analysis = zip(analysis_lines)

# Export results to txt file
output_path = os.path.join('analysis', 'analysis.txt')

with open(output_path, 'w', newline='') as outfile:
    csvwriter = csv.writer(outfile)

    for line in analysis:
        # If a blank/empty row, write it manually as writing the line creates "" in the file
        if line[0] == "":
            csvwriter.writerow("")
        else:
            csvwriter.writerow(line)