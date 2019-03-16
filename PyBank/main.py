import os 
import csv
#import csv file
data = csv.reader(open('budget_data.csv'), delimiter=",")
#file = open('budget_data.csv')
#csv_file = csv.reader(file)
# title 
print("Financial Analysis")
print("----------------------------")
#Total number of months 
row_count = sum(1 for row in data) - 1
print(f"Total Months: {row_count} ")
#Net Total Amount of profits/losses over the entire period 
headerline = fin.next()
  total = 0
  for row in csv.reader(fin):
    print col # for troubleshooting
    for col in row[2]:
  print total

#average of the changes in proffit/losses
# TOTAL DIVIDED BY row_count = sum(1 for row in data) - 1  
#greatest increase in proffits 
#greatest decrease in losses 