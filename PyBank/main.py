# *Your task is to create a Python script that analyzes the records to calculate each of the following:
import os
import csv
# path to .csv input file
pybank_csv = os.path.join("PyBank/Resources/budget_data.csv")
# path to .txt output file
output_txt = os.path.join('PyBank/Resources/output.txt')
# test path to .csv input
#print(pybank_csv)

# open and read .csv
with open(pybank_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #print(csv_reader)

# specify delimiter and check to see if headers are correct
    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header} ")

#declare variables
    total_months = []
    profit_loss = []
    total_change = []
    average_change = []
    greatest_increase = []
    greatest_decrease = []

#   * The total number of months included in the dataset
    for row in csv_reader:
        total_months.append(row[0])
        profit_loss.append(row[1])
        profit_loss = [int(i) for i in profit_loss]
        total_change = 0

#   * The net total amount of "Profit/Losses" over the entire period
    for i in range(len(profit_loss)-1):
        difference=profit_loss[i+1] - profit_loss[i]
        total_change = total_change + difference

#   * The average of the changes in "Profit/Losses" over the entire period
    average_change = (total_change)/(len(profit_loss)-1)
    #print(difference)

#   * The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(profit_loss)
    greatest_increase_date = str( total_months[profit_loss.index(min(profit_loss))]) 
#   * The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(profit_loss)
    greatest_decrease_date = str( total_months[profit_loss.index(min(profit_loss))]) 

with open(output_txt,"w") as writer:
    writer.writelines("Financial Analysis")
    writer.writelines("---------------------------------------------\n")
    writer.writelines("Total Months: " + str(total_months)+ "\n")
    writer.writelines("Total : $" + str(profit_loss) + "\n")
    writer.writelines("Average Change:" + "$" + str(difference)+ "\n")
    writer.writelines("Greatest Increase:" + greatest_increase_date + " ($" + str(greatest_increase) + ")\n")
    writer.writelines("Greatest Decrease: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")\n")
          
# Outputs
print("Financial Analysis")
print("------------------")
print("Total Months:", len(total_months))
print("Total : $", sum(profit_loss))      
print("Average Change: $",round(average_change))
print("Greatest Increase :" + greatest_increase_date + " $" + str(greatest_increase))
print("Greatest Decrease :" + greatest_decrease_date + " $" + str(greatest_decrease))