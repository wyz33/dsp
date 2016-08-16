# Hint:  use Google to find python function

import datetime
#need the datetime module to complete this task

def convert(word, params):
    date = datetime.datetime.strptime(word, params)
    return date
# defined a function called "convert" so i don't have to type datetime.datetime.strptime all the time
# word is the date string that was provided, params is whatever formatting that fit the date format.    

def diffdays(start, end, params):
    date1 = convert(start, params)
    date2 = convert(end, params)
    print (date2 - date1).days
#the above function calculate the number of days between two dates(start and end)
#users have to give the parameters (params) based on which the date strings can be parsed
    
####a)     
date_start = '01-02-2013'   
date_stop = '07-28-2015'   

diffdays(date_start, date_stop, "%m-%d-%Y")

####b)  
date_start = '12312013'  
date_stop = '05282015'  

diffdays(date_start, date_stop, "%m%d%Y")
####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

diffdays(date_start, date_stop, "%d-%b-%Y")