import os
import csv

data = os.getcwd()
filepath = os.path.join( data,'election_data.csv')

totalCount = 0; kCount = 0; cCount = 0; lCount = 0; oCount = 0; maxVoteCount = 0

def percentage (part, whole):
    return 100 * float(part)/float(whole)

with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')

     for i in csvreader:
         vote = i[0]
         country = i[1]
         candidate = i[2]
        
         totalCount = totalCount + 1

         if candidate =="Khan":
            kCount = kCount + 1
         if candidate =="Correy":
            cCount = cCount + 1
         if candidate =="Li":
            lCount = lCount + 1
         if candidate =="O'Tooley":
            oCount = oCount + 1
            
     candidateVote = {"Khan": kCount,"Correy": cCount,"Li" :lCount, "O'Tooley": oCount}
     
     for candidate, value in candidateVote.items():
         if value > maxVoteCount:
            maxVoteCount = value
            winner = candidate
   
print(f'Election Results'+'\n')

print(f'Total Votes: {totalCount}'+'\n')
print(f'-------------------------------'+'\n')

print(f'Khan: {percentage(kCount,totalCount)}  ({kCount})')
print(f'Correy: {percentage(cCount,totalCount)}  ({cCount})')
print(f'Li: {percentage(lCount,totalCount)}  ({lCount})')
print(f'O\'Tooley: {percentage(oCount,totalCount)}  ({oCount})')

print(f'Winner: {winner} '+'\n')
