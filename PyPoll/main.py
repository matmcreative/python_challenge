import os
import csv

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


    
