#I deleted the original comment because for some reason it was causing errors for my code.(see error message below)
#>>>>runfile('/Users/Home/ds/metis/metisgh/prework/dsp/python/q8_parsing.py', wdir=r'/Users/Home/ds/metis/metisgh/prework/dsp/python')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "/Users/Home/anaconda/lib/python2.7/site-packages/spyderlib/widgets/externalshell/sitecustomize.py", line 580, in runfile
#    execfile(filename, namespace)
#  File "/Users/Home/ds/metis/metisgh/prework/dsp/python/q8_parsing.py", line 2
#SyntaxError: Non-ASCII character '\xe2' in file /Users/Home/ds/metis/metisgh/prework/dsp/python/q8_parsing.py on line 3, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

import csv
# use the csv module to read the csv file
f = open('football.csv')

reader = csv.reader(f)

entire_file=[]
#first use a for-loop to extract the entire file, line by line
for row in reader:
    entire_file.append(row)
#because i read the file in excel first, i know there is a line of headers. Extract that from the body of the file
header = entire_file[0]
#the rest is data
data = entire_file[1:]    

#initialize some variables
diff = []
names = []
#get the index for goals and goals allowed columns from the header
g_index = header.index('Goals')
ga_index = header.index('Goals Allowed')

#now loop through the data lists, and extract only the stuff we need: absolute value of goals- goals allowed, 
#and the name of the teams
for i in data:
    diff.append (abs(int(i[g_index])-int(i[ga_index])))    
    names.append(i[0])

#find the minimum team and match it to the name by index (since we haven't change the indexing of anything)
res = names[diff.index(min(diff))]

print 'the team with the lowest difference in "for" and "against" goals is:', res