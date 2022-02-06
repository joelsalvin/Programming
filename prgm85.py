import csv

with open('temp.csv', mode='w') as outf:

 fieldnames = ['Name', 'Department', 'Month of join']

 content = csv.DictWriter(outf, fieldnames=fieldnames)

 content.writeheader()

 content.writerow({'Name': 'Joel', 'Department': 'HR', 'Month of joining': 'march'})

 content.writerow({'Name': 'Maria', 'Department': 'Accounting', 'Month of joining': 'May'})
data = csv.DictReader(open("temp.csv"))
print("CSV file as a dictionary:\n")
for row in data:
   print(row)
