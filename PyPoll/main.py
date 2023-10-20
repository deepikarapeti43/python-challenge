# Import modules
import os
import csv

# Define  variables
count=0
stockham=0
DeGette=0
Doane=0
Winner_name=''

# Path to collect data from the Resources folder
election_data_csv_path = os.path.join("..","Resources", "election_data.csv")

# Open and read csv
with open(election_data_csv_path) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)
    
    # Read through each row of data after the header
    for row in csv_reader:
        
        # calculate total no of votes
        count=count+1
        
        # checks each candidate and stores in particular variable
        if row[2]=="Charles Casper Stockham":
                stockham=stockham+1
        elif row[2]=="Diana DeGette":
                DeGette=DeGette+1
        elif row[2]=="Raymon Anthony Doane":
                Doane=Doane+1

# calculate percentage of votes for each candidate                
percentage_stockham=round(stockham/count*100,3)           
percentage_DeGette=round(DeGette/count*100,3)
percentage_Doane=round(Doane/count*100,3)  

# Pulls the maximum number of votes
Winner=max(stockham,DeGette,Doane)

# Based on votes assigns the candidate name
if Winner==stockham:
   Winner_name="Charles casper Stockham"
elif Winner==DeGette:
    Winner_name="Diana DeGette"   
else :
    Winner_name="Raymon Anthony Doane"


print("Election results")
print("----------------------------")
print(f'Total votes: {count}')
print("----------------------------")
print(f'Charles casper Stockham: {percentage_stockham}% {(stockham)}')
print(f'Diana DeGette: {percentage_DeGette}% {DeGette} ')
print(f'Raymon Anthony Doane: {percentage_Doane}% {Doane}')
print("----------------------------")
print(f'Winner: {Winner_name}')

election_file = os.path.join("..","analysis", "election_data_output.txt")
with open(election_file, "w") as outfile:
    outfile.write("Election results\n")
    outfile.write("----------------------------\n")
    outfile.write(f'Total votes: {count}\n')
    outfile.write("----------------------------\n")
    outfile.write(f'Charles casper Stockham: {percentage_stockham}% ({stockham})\n')
    outfile.write(f'Diana DeGette: {percentage_DeGette}% ({DeGette})\n')
    outfile.write(f'Raymon Anthony Doane: {percentage_Doane}% ({Doane})\n')
    outfile.write("----------------------------\n")
    outfile.write(f'Winner: {Winner_name}')
    
    
