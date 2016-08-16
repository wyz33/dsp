# Learn Python


Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>>  Both lists and tuples are sequences. The biggest difference is that lists are mutable (i.e. you can change any element of the list at anytime after the list has been created), whereas tuples are immutable. 
    Dictionaries can only accpet immutable inputs as keys. so only tuples will work as keys in dictionaries.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> lists and sets are both collections of elements. However, lists are ordered sequence of muttable elements while sets are unordered collection of unique immutable elements. 
Their main differences are that (1) lists can have duplicates while sets cannot, (2)list elements are ordered by indices while elements in a set is unordered, and (3)lists are muttable and sets are immutable.

Example for usage:
(1) use a list when you will want to preserve the order the elements are in, sort the elements, and update elements as they change without creating a new list:
	ex. list of grades for a class: you will want to be able to sort from highest to lowest
	    this is probably best done by having a list of tuples which contain the name of the student and their grade: [('Name1', grade1), ('Name2', grade2), etc]
(2) use a set when you want to make sure that there are no duplicates in your collection, want to check if an item already exist in the set, or want to compare the differences between two sets:
	ex. a set of guests' names for a wedding.Starting with separate sets for the groom and bride:
	    groom = set(['Name1', 'Name2', 'Name3', etc])
	    bride = set(['Name4', 'Name5', 'Name1', etc])
        when needed, one can use the union function: groom.union(bride) to combine the guest lists which automatically ensures that there will be no repeats (also a nice metaphor).

When finding an element, it is much faster to do it in a set instead of a list. This is because Python uses a hashtable when searching for an element in a set, whereas it would look through every single element in a list. 
 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda is an anonymous function that one can use to define a short function that you only need once or twice. When using lambda,you can use the function to interface with other functions without having to write the definition of the function separately.
	Example 1. Using lambda function to filter a list of numbers:
		numbers = [i in range(1, 101)] #creates a list of numbers from 1 to 100
		even_numbers = filter(lambda x: x%2 ==0, numbers) #defines a lambda function where x%2==0, and filters the list numbers based on that condition.
	Example 2. Using lambda function as a key to sorted: 
		A list of tuples for a class of students, with different columns for name, age, and grades of the students:
		students = [ ('Elle', 13, 'B'),('Adam', 14, 'A'), ('Jane', 12, 'C')]
		#normally when using sorted(students), the program will default to sorting the first column, the names. However, with the key function, we can sort the tuple based on any user-defined column
		sorted(students, key= lambda a: a[1]) #This will sort by the 2nd column, or age. To sort by grades, we can change it to lambda a: a[2]
 

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension:A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
	Example (1) for every element in a list of numbers from 1 to 10, return a new list that consists of the square of each number.
	a. list comprehension way:
	square = [x**2 for x in range(1,11)]
	b. 'map' way:
	square = map(lambda x:x**2, range(1,11))

	Example (2) from a list of numbers from 1 to 100, return a new list of only odd numbers
	a. list comprehension way:
	odd = [x for x in range(1, 101) if x%2!=0]
	b. 'filter' way:
	odd = filter(lambda x: x%2!=0, range(1, 101))

   So far it seems that list comprehension and map/filter has similar capabilities. For me the choice is only based on stylistic preferences at the moment.

   Based on my current understanding, set and dictionary comprehension is very similar to list comprehension. 
        Example(3) Set comprehension: 
	square_set = {x**2 for x in range(1, 11)}
	
	Example(4) Dictionary comprehension:
	square_dict = {x:x**2 for x in range (1, 11)}	
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





