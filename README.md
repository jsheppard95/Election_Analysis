# Election_Analysis

## Overview of Election Audit
Here we have a Python script to audit a local Colorado congressional election
and report the voting breakdown by county and candidate. The script reads the
CSV file [election_results.csv](Resources/election_results.csv) of format
`Ballot ID,County,Candidate` and tallies the number of votes by county and
candidate. It then reports the total number of votes cast, the breakdown by
county and candidate, the largest county turnout, and the winner of the
election to the terminal and output file
[election_results.txt](analysis/election_results.txt).

### Resources
- Data source: [election_results.csv](Resources/election_results.csv)
- Software: Python 3.7.6, Visual Studio Code 1.51.1

## Election-Audit Results

### Methods
To perform this analysis, we loop through each row in the input file using
[`csv.reader`](https://docs.python.org/3/library/csv.html#csv.reader), adding
to the total vote count and acquiring the chosen candidate and voting county
with each iteration:
```
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1 

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
```
We then check if this is the first instance of each candidate and county and
if so, add it to the results dictionaries `candidate_votes` and `county_votes`
with initial counts of zero. We then increment the count for this and all
subsequent instances of the current row's `candidate_name` and `county_name`.
Finally, we loop through both results dictionaries to determine winner of the
election and the county casting the most votes. In the case of the candidates,
we first initialize the following variables:
```
winning_count = 0
winning_percentage = 0
winning_candidate = ""
```
We can then find the winner as follows:
```
for candidate_name in candidate_votes:
    # Retrieve vote count and percentage
    votes = candidate_votes.get(candidate_name)
    vote_percentage = float(votes) / float(total_votes) * 100

    # Write results votes and vote_percentage for candidate_name to
    # terminal and output file

    # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
```
We are then left with the `winning_count`, `winning_candidate`, and
`winning_percentage` set to the correct values from `candidate_votes` which we
then write to the terminal and output file
[election_results.txt](analysis/election_results.txt). The process is similar
for the county results.

### Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The county results were:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)
- The county with the largest voter turnout was:
    - Denver, with 82.8% of the vote and 306,055 votes
- The candidate results were
    - Charles Casper Stockham: 23.0% (85,213)
    - Diana DeGette: 73.8% (272,892)
    - Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 votes.

## Election-Audit Summary
Through this audit of a Colorado local congressional election, we find the
county with the largest voter turnout to be Denver providing 82.8% of the vote
for a total of 306,055 votes and the winner to be Diana DeGette with
73.8% of the vote for a total of 272,892 votes. This script is generalizable to
other election data sources following the same format as
[election_results.csv](Resources/election_results.csv) with the replacement of
the hard-coded input file name `election_results.csv` with an input parameter.
One method to do so would be to move the entire script within a function
`analyze_election_data` with input parameter `infile`, as shown below:
```
def analyze_election_data(infile):
    """
    Parameters
    ----------
    infile : str, file name of election results CSV file, placed in Resources
             directory
    """
```
We would then set our input file as:
```
file_to_load = os.path.join("Resources", infile)
```
and import/call the function from the Python interpreter as:
```
>>> from PyPoll_Challenge import analyze_election_data
>>> analyze_election_data(input_file.csv)
```
An alternative is to input the CSV file from the command line using
[`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv). This would
require the following addition:
```
import sys
args = sys.argv
```
We then have a list `args` whose first element is the script name and all
subsequent elements are those passed from the command line after the script
from left to right. We can thus set our input file as:
```
file_to_load = os.path.join("Resources", args[1])
```
and run the script from the command line:
```
$ python PyPoll_Challenge.py input_file.csv
```
Looking forward, we could further this analysis by considering the breakdown of
each candidate vote by county and plot the results to visualize potential
relationships between the two. This would be particularly useful for a more
general dataset with a wider distribution of counties in order to analyze
regional trends.
