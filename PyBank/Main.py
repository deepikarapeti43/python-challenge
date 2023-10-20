# Import modules
import os 
import csv

# Define lists and variables
months=[]
profit_loss_changes=[]
count_months=0
Total_net_profit_loss=0
previous_mnth_profit_loss=0
current_mnth_profit_loss=0
profit_loss_change=0


# Set path
budget_csv_file=os.path.join("..","Resources","budget_data.csv")

# open csv file and read
with open(budget_csv_file) as csv_file:
    csv_read=csv.reader(csv_file,delimiter=',')
    
    # Reads the header row
    csv_header=next(csv_file)
    
    #print(csv_header)
    
    # Reads each row data in csv file
    for row in csv_read:
        
        # count of months
        count_months += 1
         
        # calculating Total profit and loss
        current_mnth_profit_loss=int(row[1])
        Total_net_profit_loss+=current_mnth_profit_loss
        
        # If count is 1 then it stores the previous month value to current month
        if count_months==1:
            previous_mnth_profit_loss=current_mnth_profit_loss
        else:
             # Calculate Average 
             profit_loss_change=current_mnth_profit_loss-previous_mnth_profit_loss
             
             # Add each month to months
             months.append(row[0])
             
             #Add each profit and loss change to list
             profit_loss_changes.append(profit_loss_change)
             
             # Assign current month values to previous months
             previous_mnth_profit_loss=current_mnth_profit_loss
    
    # Add all the values          
    sum_profit_loss = sum(profit_loss_changes)
    
    # calculate average of profit/loss changes
    average_profit_loss =round(sum_profit_loss/(count_months - 1), 2)
 
    # Calculates highest and lowest profit/loss changes over the period
    greatest_increase_change=max(profit_loss_changes)
    greatest_decrease_change=min(profit_loss_changes)
    
    # Find out the highest and lowest months of profit loss changes
    greatest_month_index=profit_loss_changes.index(greatest_increase_change)
    lowest_month_index=profit_loss_changes.index(greatest_decrease_change)
    
    # Assign values
    Highest_month=months[greatest_month_index]
    lowest_month=months[lowest_month_index]
    
print("Financial Analysis")
print("----------------------------")
print(f'Total Months:  {count_months}')
print(f'Total:  ${Total_net_profit_loss}')
print(f'Average Change:  ${average_profit_loss}')
print(f'Greatest Increase in Profits:  {Highest_month} (${greatest_increase_change})')
print(f'Greatest Decrease in Losses:  {lowest_month} (${greatest_decrease_change})')  

budget_file = os.path.join("..","analysis", "budget_data_output.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count_months}\n")
    outfile.write(f"Total:  ${Total_net_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {Highest_month} (${greatest_increase_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {lowest_month} (${greatest_decrease_change})\n")        
        
    
    