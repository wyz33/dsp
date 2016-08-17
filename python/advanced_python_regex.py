import csv
# use the csv module to read the csv file
f = open('faculty.csv')
reader = csv.reader(f)

#setting up to separate the csv files into different columns
header = next(reader)
names =[]
degrees = []
titles = []
emails = []

#Use the header file to find the index of the columns
name_index = header.index('name')
degree_index = header.index(' degree')
title_index = header.index(' title')
email_index = header.index(' email')

for row in reader:
    names.append(row[name_index])
    degrees.append(row[degree_index])
    titles.append(row[title_index])
    emails.append(row[email_index])

#a function that takes a list variable and outputs unique elements in the list and the number of times they occur
def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d
#another function that uses the histogram function and prints the list (with user defined description) from most to least
def most_frequent (s, description):
    freq = []
    d = histogram(s)
    print type(d)
    b = len(d)
    print 'Total number of unique '+description+' is', b
    for word in d:
        freq.append((d[word], word))
    freq.sort(reverse=True)
    for a, b in freq:        
        print b, a

#using a for loop to identify individual degrees in the degrees column, removes the  . in the degrees
ind_degrees = []
for i in degrees:
    no_dot = i.replace('.', '')
    singles = no_dot.split()
    for j in singles:
        ind_degrees.append(j)

#using a for loop to identify individual titles in the titles column, removing all departmental information
ind_titles = []

for i in titles:
    j = i.index('Professor') + len('Professor')
    no_department = i.replace(i[j:], '')
    ind_titles.append(no_department)

#using a for loop to find all email domains from the email list
domains = []
for i in emails:
    j = i.index('@') +1
    only_domain = i.replace(i[:j], '')
    domains.append(only_domain)
 
#answer to Q1   
most_frequent(ind_degrees, 'degrees')

#answer to Q2
most_frequent(ind_titles, 'titles')    

#answer to Q3
print emails

#answer to Q4
unique_domains = list(set(domains))
print unique_domains


    
    