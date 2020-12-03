# Election_Analysis

## Overview of Election Audit
Here we have a Python script to audit a Colorado local congressional election and report the voting breakdown by county and candidate.
The script reads a CSV file [election_results.csv](Resources/election_results.csv) of format `Ballot ID,County,Candidate` and tallies
the number of votes by county and candidate. It then reports the total number of votes cast, the breakdown by county and candidate,
the largest county turnout, and the winner of the election to the terminal and output file [election_results.txt](analysis/election_results.txt).

### Resources
- Data source: [election_results.csv](Resources/election_results.csv)
- Software: Python 3.7.6, Visual Studio Code, 1.51.1

## Election-Audit Results
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
