# Import modules
import os
import csv
import collections
from collections import Counter

# Define PyPoll's variables
voters_candidates = []
votes_per_candidate = []
stockham=0
DeGette=0
Doane=0

# Path to collect data from the Resources folder
election_data_csv_path = os.path.join("..","Resources", "election_data.csv")

# Open and read csv
with open(election_data_csv_path) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)
    print(csv_header)
    
    # Read through each row of data after the header
    for row in csv_reader:
            if row[2]=="Charles Casper Stockham":
                stockham=stockham+1
            elif row[2]=="Diana DeGette":
                DeGette=DeGette+1
            elif row[2]=="Raymon Anthony Doane":
                Doane=Doane+1
                
print(stockham)
print(DeGette)
print(Doane)
    
    
