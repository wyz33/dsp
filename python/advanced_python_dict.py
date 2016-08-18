import csv
# use the csv module to read the csv file
f = open('faculty.csv')
reader = csv.reader(f)

#setting up to separate the csv files into different columns 
#also read the headline so we can skip right to the data part of the csv file.
header = next(reader)

#Use the header file to find the index of the columns
name_index = header.index('name')

faculty_dict = dict()
#answer to Q6, first dictionsary organized only by last name
for row in reader:
    name = row[name_index]
    separate = name.split()
    last = separate[-1]
    if last in faculty_dict.keys():
        faculty_dict[last].append(row[name_index+1:])
    else:
        faculty_dict[last] = [row[name_index +1:]]

for x in sorted(faculty_dict)[0:3]:
    print x, faculty_dict[x]
f.close()

#answr to Q7, better dictionary with (first name, last name) tuple as dictionary keys
f = open('faculty.csv')
reader = csv.reader(f)
header = next(reader)
name_index = header.index('name')
professor_dict = dict()    
for row in reader:
    name = row[name_index]
    separate = name.split()
    if len(separate)<3:
        better_name = (separate[0], separate[-1])
    else:
        better_name = (' '.join(separate[0:-1]), separate[-1])
    professor_dict[better_name] = row[name_index+1:]

##answer for Q7, sorted by first name    
for x in sorted(professor_dict)[0:3]:
    print x, professor_dict[x]

#answer for Q8, sorted by last name:
for x in sorted(professor_dict.keys(), key =lambda x: x[1]):
    print x, professor_dict[x]
    