import csv
# use the csv module to read the csv file
f = open('faculty.csv')
reader = csv.reader(f)

#extract all the emails into a list
header = next(reader)
emails = []
email_index = header.index(' email')

for row in reader:
    emails.append(row[email_index])

#now open a file called emails.csv
#and write a single email address per line.
with open("emails.csv", "w") as g:
    writer = csv.writer(g)
    for i in emails:    
        writer.writerow([i])
        
g.close()