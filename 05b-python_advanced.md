## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

Total number of unique degrees is 9
PhD 31
ScD 6
MS 2
MPH 2
MD 1
MA 1
JD 1
BSEd 1
0 1

####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

Total number of unique titles is 3
Professor 13
Associate Professor 12
Assistant Professor 12

####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.
```
>>> print emails
['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu', 'sellenbe@upenn.edu', 'jellenbe@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu', 'pgimotty@upenn.edu', 'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu', 'rhubb@mail.med.upenn.edu', 'whwang@mail.med.upenn.edu', 'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'liy3@email.chop.edu', 'mingyao@mail.med.upenn.edu', 'hongzhe@upenn.edu', 'rlocalio@upenn.edu', 'nanditam@mail.med.upenn.edu', 'knashawn@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu', 'michross@upenn.edu', 'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'shawp@upenn.edu', 'rshi@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu', 'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu', 'atroxel@mail.med.upenn.edu', 'rxiao@mail.med.upenn.edu', 'sxie@mail.med.upenn.edu', 'dxie@upenn.edu', 'weiyang@mail.med.upenn.edu']
```

####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.
```
>>> print unique_domains
['email.chop.edu', 'upenn.edu', 'cceb.med.upenn.edu', 'mail.med.upenn.edu']
```
Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:
```
first three sorted key and value pairs in alphabetical order:
Bellamy [[' Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu']]
Bilker [['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']]
Bryan [[' PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu']]
```
####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:
```
('A. Russell', 'Localio') [' JD MA MPH MS PhD', 'Associate Professor of Biostatistics', 'rlocalio@upenn.edu']
('Alisa Jane', 'Stephens') [' Ph.D.', 'Assistant Professor of Biostatistics', 'alisaste@mail.med.upenn.edu']
('Andrea Beth', 'Troxel') [' ScD', 'Professor of Biostatistics', 'atroxel@mail.med.upenn.edu']
```
####Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors
```
('Scarlett L.', 'Bellamy') [' Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu']
('Warren B.', 'Bilker') ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']
('Matthew W', 'Bryan') [' PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu']
('Jinbo', 'Chen') [' Ph.D.', 'Associate Professor of Biostatistics', 'jinboche@upenn.edu']
('Susan S', 'Ellenberg') [' Ph.D.', 'Professor of Biostatistics', 'sellenbe@upenn.edu']
('Jonas H.', 'Ellenberg') [' Ph.D.', 'Professor of Biostatistics', 'jellenbe@mail.med.upenn.edu']
('Rui', 'Feng') [' Ph.D', 'Assistant Professor of Biostatistics', 'ruifeng@upenn.edu']
('Benjamin C.', 'French') [' PhD', 'Associate Professor of Biostatistics', 'bcfrench@mail.med.upenn.edu']
('Phyllis A.', 'Gimotty') [' Ph.D', 'Professor of Biostatistics', 'pgimotty@upenn.edu']
('Wensheng', 'Guo') [' Ph.D', 'Professor of Biostatistics', 'wguo@mail.med.upenn.edu']
('Yenchih', 'Hsu') [' Ph.D.', 'Assistant Professor of Biostatistics', 'hsu9@mail.med.upenn.edu']
('Rebecca A', 'Hubbard') [' PhD', 'Associate Professor of Biostatistics', 'rhubb@mail.med.upenn.edu']
('Wei-Ting', 'Hwang') [' Ph.D.', 'Associate Professor of Biostatistics', 'whwang@mail.med.upenn.edu']
('Marshall M.', 'Joffe') [' MD MPH Ph.D', 'Professor of Biostatistics', 'mjoffe@mail.med.upenn.edu']
('J. Richard', 'Landis') [' B.S.Ed. M.S. Ph.D.', 'Professor of Biostatistics', 'jrlandis@mail.med.upenn.edu']
('Yimei', 'Li') [' Ph.D.', 'Assistant Professor of Biostatistics', 'liy3@email.chop.edu']
('Hongzhe', 'Li') [' Ph.D', 'Professor of Biostatistics', 'hongzhe@upenn.edu']
('Mingyao', 'Li') [' Ph.D.', 'Associate Professor of Biostatistics', 'mingyao@mail.med.upenn.edu']
('A. Russell', 'Localio') [' JD MA MPH MS PhD', 'Associate Professor of Biostatistics', 'rlocalio@upenn.edu']
('Nandita', 'Mitra') [' Ph.D.', 'Associate Professor of Biostatistics', 'nanditam@mail.med.upenn.edu']
('Knashawn H.', 'Morales') [' Sc.D.', 'Associate Professor of Biostatistics', 'knashawn@mail.med.upenn.edu']
('Kathleen Joy', 'Propert') [' Sc.D.', 'Professor of Biostatistics', 'propert@mail.med.upenn.edu']
('Mary E.', 'Putt') [' PhD ScD', 'Professor of Biostatistics', 'mputt@mail.med.upenn.edu']
('Sarah Jane', 'Ratcliffe') [' Ph.D.', 'Associate Professor of Biostatistics', 'sratclif@upenn.edu']
('Michelle Elana', 'Ross') [' PhD', 'Assistant Professor is Biostatistics', 'michross@upenn.edu']
('Jason A.', 'Roy') [' Ph.D.', 'Associate Professor of Biostatistics', 'jaroy@mail.med.upenn.edu']
('Mary D.', 'Sammel') [' Sc.D.', 'Professor of Biostatistics', 'msammel@cceb.med.upenn.edu']
('Pamela Ann', 'Shaw') [' PhD', 'Assistant Professor of Biostatistics', 'shawp@upenn.edu']
('Russell Takeshi', 'Shinohara') ['0', 'Assistant Professor of Biostatistics', 'rshi@mail.med.upenn.edu']
('Haochang', 'Shou') [' Ph.D.', 'Assistant Professor of Biostatistics', 'hshou@mail.med.upenn.edu']
('Justine', 'Shults') [' Ph.D.', 'Professor of Biostatistics', 'jshults@mail.med.upenn.edu']
('Alisa Jane', 'Stephens') [' Ph.D.', 'Assistant Professor of Biostatistics', 'alisaste@mail.med.upenn.edu']
('Andrea Beth', 'Troxel') [' ScD', 'Professor of Biostatistics', 'atroxel@mail.med.upenn.edu']
('Rui', 'Xiao') [' PhD', 'Assistant Professor of Biostatistics', 'rxiao@mail.med.upenn.edu']
('Sharon Xiangwen', 'Xie') [' Ph.D.', 'Associate Professor of Biostatistics', 'sxie@mail.med.upenn.edu']
('Dawei', 'Xie') [' PhD', 'Assistant Professor of Biostatistics', 'dxie@upenn.edu']
('Wei (Peter)', 'Yang') [' Ph.D.', 'Assistant Professor of Biostatistics', 'weiyang@mail.med.upenn.edu']
```
Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

