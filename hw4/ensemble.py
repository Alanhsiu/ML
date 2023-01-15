import csv

results = []
with open('./ensemble.csv', newline='') as csvfile:

  rows = csv.reader(csvfile, delimiter=',')

  for row in rows:
    max = 0
    if(row[2]==row[3]):
        max = row[2]
    else:
        max = row[1]
    results.append([row[0],max])


with open('./ensemble.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(results)