import os
import csv

# Set path for file
csvpath = os.path.join('PyPoll/Resources/election_data.csv')

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#Create candidate variables

    candidate1 = "Khan" 
    candidate2 = "Correy"
    candidate3 = "Li"
    candidate4 = "O'Tooley"

    #Define Starting number of votes
    initialvotes1 = 0
    initialvotes2 = 0
    initialvotes3 = 0
    initialvotes4 = 0

    # Loop through looking for the video
    for row in csvreader:
        if row[2] == candidate1:
            initialvotes1 = initialvotes1 + 1
        elif row[2] == candidate2:
            initialvotes2 = initialvotes2 + 1
        elif row[2] == candidate3:
            initialvotes3 = initialvotes3 + 1
        elif row[2] == candidate4:
            initialvotes4 = initialvotes4 + 1

    #define total votes
    totalvotes = initialvotes1 + initialvotes2 + initialvotes3 + initialvotes4

    #define percentages
    khanpercentage = round((initialvotes1/totalvotes)*100,3)
    correypercentage = round((initialvotes2/totalvotes)*100,3)
    lipercentage = round((initialvotes3/totalvotes)*100,3)
    otooleypercentage = round((initialvotes4/totalvotes)*100,3)
    
# Write File
output_file = os.path.join('.', 'PyPoll', 'Resources', 'election_data_revised.text')

# Open file with 'w'
with open(output_file, 'w',) as txtfile:

    #print results
    print ("Election Results:")
    print("Total Votes:" + str(totalvotes))
    print("Khan:" + str(khanpercentage) + '%' + ' ' + '(' + str(initialvotes1) + ')')
    print("Correy:" + str(correypercentage) + '%' + ' ' + '(' + str(initialvotes2) + ')')
    print("Li:" + str(lipercentage) + '%' + ' ' + '(' + str(initialvotes3) + ')')
    print("Otooley:" + str(otooleypercentage) + '%' + ' ' + '(' + str(initialvotes4) + ')')

    if initialvotes1 > initialvotes2 and initialvotes1 > initialvotes2 and initialvotes1 > initialvotes4:
        print ("Winner: Khan")
    elif initialvotes2 > initialvotes1 and initialvotes2 > initialvotes3 and initialvotes2 > initialvotes4:
        print ("Winner: Correy")
    elif initialvotes3 > initialvotes1 and initialvotes3 > initialvotes2 and initialvotes3 > initialvotes4:
        print ("Winner: Li")
    elif initialvotes4 > initialvotes1 and initialvotes4 > initialvotes2 and initialvotes4 > initialvotes3:
        print ("Winner: O'Tooley") 