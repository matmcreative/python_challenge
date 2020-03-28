import os
import csv

# Create function to analyze file
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
    for row in data[0:10]:
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] +=1
        else:
            candidates[candidate] =1
    return [candidates, total_votes]

# def vote_percents(candidates, total_votes):
#     percents ={}
#     for candidate, votes in candidate.items():
#         percents[candidate] = int(round((votes/total_votes) *100, 0))
#     return percents

def results(candidates, percents):
    winning_votes = 0
    winner = ""
    for candidate, votes in candidates.item():
        if votes > winning_votes:
            winner = candidate
            winning_votes = votes
    print_winner = f"The winner is {winner}!"
    print_candidates = ""
    for candidate, votes in candidate.items():
        print_candidates = print_candidates + f"{candidate}: {votes} votes({(votes/total_votes)*100}%)\n"
    results = f"{print_winner}/n___________________________________/n
{print_candidates}"
    return results

vote_csv = read_file("/Users/lisareedpreston/Documents/VanderbiltBootcamp/Homework/python_challenge/PyPoll/Resources/election_data.csv")
candidates, total_votes = vote_count(vote_csv)
results = results(candidates, total_votes)
print (results)


    
