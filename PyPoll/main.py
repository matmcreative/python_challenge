import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(dir_path,"Resources/Election_Data.csv")

output_file=os.path.join(dir_path,"Final_PyPoll.txt")

<<<<<<< HEAD
total=0
candidate=[]
unique_candidate=[]
vote_count=[]
vote_percent=[]
=======
def read_file(path):
    with open(path) as f:
        csvreader = csv.reader(f, delimiter = ',')
        header = next(csvreader)
        data = []
        for row in csvreader:
            data.append(row)
        return data

def vote_count(data):
    candidates = {}
    total_votes = 0
    for row in data:
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] +=1
        else:
            candidates[candidate] =1
    return [candidates, total_votes]

def results(candidates, total_votes):
    winning_votes = 0
    winner = ""
    for candidate, votes in candidates.items():
        if votes > winning_votes:
            winner = candidate
            winning_votes = votes
    print_winner = f"The winner is {winner} with {winning_votes} votes!"
    print_candidates = ""
    for candidate, votes in candidates.items():
        print_candidates = print_candidates + f"{candidate}: {votes} votes({(votes/total_votes)*100}%)\n"
    results = f"{print_winner}/n___________________________________/n{print_candidates}"
    return results

def final_results(path):
        vote_csv = read_file("Resources/election_data.csv")
        candidates, total_votes = vote_count(vote_csv)
        results = results(candidates, total_votes)
        print(results)
        save_results = input("Do you want to save the file? (y/n)\n")
        if save_results =="y":
                with open("output_file.txt, "w") as doc:
                          doc.write(results)
final_results("eletion_data.csv")
Collapse
>>>>>>> 3ae98903a72221a4d001870998efbf0db4a9a02f


with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvreader)

    for row in csvreader:
        #Total votes
        total=total+1

        #Candidate count
        candidate.append(row[2])
   
    #Loop through, find the count for each candidate 
    #and calc % of votes for each candidate
    for c in set(candidate):
        unique_candidate.append(c)
        v=candidate.count(c)
        vote_count.append(v)
        p=round((v/total)*100,2)
        vote_percent.append(p)
    
    #Identify the winner based on vote count adn index name based on count
    winner_count=max(vote_count)
    winner=unique_candidate[vote_count.index(winner_count)]

#Print results in terminal
print('Election Results')
print('--------------------------------')
print(f'Total Votes: {total}')
print('--------------------------------')
for i in range(len(unique_candidate)):
    print(f'{unique_candidate[i]}: {vote_percent[i]}% {vote_count[i]}')
print('--------------------------------')
print(f'Winner: {winner}')
print('--------------------------------')

#Write results to text file
with open(output_file, "w") as txtfile:
    txtfile.write('Election Results')
    txtfile.write('\n------------------------------------')
    txtfile.write(f'\nTotal Votes: {total}')
    txtfile.write('\n------------------------------------')
    for i in range (len(unique_candidate)):
        txtfile.write(f'\n{unique_candidate[i]}: {vote_percent[i]}% {vote_count[i]}')
    txtfile.write('\n------------------------------------')
    txtfile.write(f'\nWinner: {winner}')
    txtfile.write('\n------------------------------------')