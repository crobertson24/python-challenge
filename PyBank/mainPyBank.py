
import os
import csv

data = os.getcwd()

filepath = os.path.join( data,'./budget_data.csv')


count = 0; total = 0; initialValue = 0; diff = 0; profitMax = 0; profitMin = 0

with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     print('Financial Analysis'+'\n')

     for i in csvreader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         diff =  iAmount - initialValue
        
         if profitMax < diff:
            profitMax = diff
            profitMaxDate = month
         
         if profitMin > diff:
            profitMin = diff
            profitMinDate = month

         initalValue = iAmount   
         
         count = count + 1
         total += int(Amount) 

print(f'Total Months : {count}')
print(f'Total: $ {total}')
print(f'Greatest Increase in Profits: {profitMaxDate} : ($ {profitMax})')
print(f'Greatest Decrease in Profits: {profitMinDate} : ($ {profitMin})')
