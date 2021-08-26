import csv
import os

path_election = os.path.join(r'Resources/election_data.csv')
with open(path_election, 'r') as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    #skip header
    next(csv_reader)

    # Store all of the text inside a variable called "lines"
    to_list = list(csv_reader)
    # print(to_list)

#Total Votes

total_votes = len(to_list)
#print(total_votes)

#Vote count

khan_vote = 0
correy_vote =0
li_vote = 0
tooley_vote =0

for i in range(0, total_votes):
    if to_list[i][2] == "Khan":
        khan_vote += 1
    elif to_list[i][2] =="Correy":
        correy_vote +=1
    elif to_list[i][2] =="Li":
        li_vote += 1
    elif to_list[i][2] =="O'Tooley":
        tooley_vote += 1

#winning percentage

khan_vote_rate = "{:.3%}".format(khan_vote / total_votes)
correy_vote_rate = "{:.3%}".format(correy_vote / total_votes)
li_vote_rate = "{:.3%}".format(li_vote / total_votes)
tooley_vote_rate = "{:.3%}".format(tooley_vote / total_votes)


#winner
#candidates = {"Khan":khan_vote,"Correy":correy_vote,"Li":li_vote,"O'Tooley":tooley_vote}
candidates = {khan_vote:"Khan",correy_vote:"Correy",li_vote:"Li",tooley_vote:"O'Tooley"}

winner_count = max(khan_vote,correy_vote,li_vote,tooley_vote)
winner = candidates[winner_count]


#print em all

print("Election Results\n"+ "-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {khan_vote_rate} ({khan_vote})\nCorrey: {correy_vote_rate} ({correy_vote})\nLi: {li_vote_rate} ({li_vote})\nO'Tooley: {tooley_vote_rate} ({tooley_vote})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#write in a text

with open('Analysis/Analysis.txt', 'w') as a:
    a.writelines("Election Results\n"+"-------------------------")
    a.writelines('\n')
    a.writelines(f"Total Votes: {total_votes}")
    a.writelines('\n')
    a.writelines("-------------------------")
    a.writelines('\n')
    a.writelines(f"Khan: {khan_vote_rate} ({khan_vote})\nCorrey: {correy_vote_rate} ({correy_vote})\nLi: {li_vote_rate} ({li_vote})\nO'Tooley: {tooley_vote_rate} ({tooley_vote})")
    a.writelines('\n')
    a.writelines("-------------------------")
    a.writelines('\n')
    a.writelines(f"Winner: {winner}")
    a.writelines('\n')
    a.writelines("-------------------------")
    a.writelines('\n')