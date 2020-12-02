import csv
import os
# Data we need to retrieve:
# 1. Total number of votes cast
# 2. A Completer list of candidates who received votes
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load, 'r') as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read and print the header row
    headers = next(file_reader)
    print(headers)
    # Print each row in the csv file
#    for row in file_reader:
#        print(row)

with open(file_to_save, "w") as txt_file:
    # Write some data to file
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")