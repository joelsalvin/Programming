import csv
with open('jov.txt') as inf:
 content = csv.DictReader(inf)

 print("playername")

 for row in content:
   print(row["PlayerName"])
    
