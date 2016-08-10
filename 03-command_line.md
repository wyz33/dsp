# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.


1. pushd: pushes current directory to a list for later reference

       syntax : pushd NEW_DIR
2. popd: Takes the latest directory on the list and cd to there
3. find:

       syntax: find DIR -name WILDCARD -print
4. env: displays all environmental variables
5. echo (ENV): displays value of environmental variable

       syntax: echo $VARIABLENAME
6. export: create or changes environmental variables

       syntax: export VARIABLE=value (or "value with space in between words")

7. grep: find text strings
8. touch: create new file
       
       syntax: touch FILENAME
9. |: pipes output from left side of bar to the function on the right
10. <,>: same as pipe, but directional, and also can funnel input into a file.


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

1. ls : list files in the directory
2. ls -a : list all files and directories in the directory, including the hidden files (starting with .)
3. ls -l : list files and directories with information about size, modification date/time, name, owner, and permission.
4. ls -lh: same as -l, but also show size in human readable formats
5. ls -lah: combines the above three, show all files and directories, including hidden ones, in long format listing with human readable formats
6. ls -t: sort the files and directories listed by time stamp (newest first)
7. ls -Glp: list files and directories with colorized output, in long format listing, with directories indicated with a "/" after their names.


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

1. -U      Use time of file creation, instead of last modification for sorting (-t) or long output (-l).
2. -r      Reverse the order of the sort to get reverse lexicographical order or the oldest entries first (or largest files last, if
             combined with sort by size
3. -S      Sort files by size
4. -m      Stream output format; list files across the page, separated by commas.
5. -d      Displays only directories

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs takes space, tab, newline and end-of-file delimited strings from the standard input and executes a specific function with the strings as arguments. It will cycle through and execute the funciton repeatedly until the input is exhausted.

Example:

I have a text file ex1.txt where there is a list of file names (separated by space), which I would like to use to create a whole new set of files. To do this using xargs, I would use the command line:

cat ex1.txt | xargs touch

This would create a single file for each entry in ex1.txt in the current directory.

 

