# Election_Analysis

## Project Overview
Here we have a Python script to audit an example local congressional election and perform the following tasks:

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data source: [election_results.csv](Resources/election_results.csv)
- Software: Python 3.7.6, Visual Studio Code, 1.51.1

## Summary
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Challenge Overview
Our data source is a CSV file with the following format:
```
Ballot ID,County,Candidate
```
We thus loop through each row in the file to aquire the total number of votes, the candidate options, and the number of votes cast for each candidate.
We then calculate the percentage of the popular vote and the total number of votes that each candidate received to determine the winner and output this result
to both the terminal and [election_analysis.txt](analysis/election_analysis.txt).

## Challenge Summary
We find the winner of the election was Diana DeGette with 73.8% of the vote (272,892 votes). This script is generalizeable to other election data sources
following the same format as [election_results.csv](Resources/election_results.csv) with the replacement of the hard-coded input file name with an input
parameter. This could be accomplished through a command line interface using [argparse](https://docs.python.org/3/library/argparse.html), `sys.argv`, or a simple
function call using the Python interpreter.
