#This will allow us to create file paths across operating systems
import os 
import csv

# csv_path = ../Resources/budget_data.csv
csv_path = os.path.join('..','Resources', 'budget_data.csv')

output_path = "output.txt"

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    
    csv_header = next(csvreader)
    data = list(csvreader)
    
    with open(output_path, 'w') as output_file:
        total_months = 0
        total_profit_losses = 0
        total_number_of_changes = 0
        
        output_file.write("Financial Analysis\n")
        output_file.write("------------------------------\n")
        
        for row in data:
            months = row[0].split("-")[0]
            total_months += 1
            
            profit_loss = int(row[1])
            total_profit_losses += profit_loss
            
            max_increase = 0
            changes = []
            greatest_increase =['feb', 10]
            greatest_decrease =['Aug', 10]
            
            for row2 in range(1, len(data)):
                current_profit = int(data[row2][1])
                previous_profit = int(data[row2-1][1])
                
                current_month = (data[row2][0])
                previous_month = data[row2-1][0]
                
                profit_change = current_profit - previous_profit 
                changes.append(profit_change)
                
                if profit_change > greatest_increase[1]:
                    greatest_increase = (current_month, profit_change)
                    
                if greatest_decrease[1] > profit_change:
                    greatest_decrease = (current_month, profit_change)
                    
                average_change = sum(changes)/len(changes)
                
        output_file.write(f"Total months: {total_months}\n")
        output_file.write(f"Total: ${total_profit_losses}\n")
        output_file.write(f"Average Change: ${round(average_change, 2)}\n")
        output_file.write(f"Greatest Increase in Profits: {greatest_increase}\n")
        output_file.write(f"Greatest Decrease in Profits: {greatest_decrease}\n")
    
    

      
   
  
