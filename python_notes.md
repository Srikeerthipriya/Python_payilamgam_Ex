## Python Notes
#### Day 2 (21/11/25)
#### Python
Python founded by ‘Guido van Rossum’ in december of 1989 over christmas holiday.
Python’s name was inspired by ‘Monty Python’s Flying Circus’.

Python is Interpreted language , interpreter helps you translate it, may not match ur speed Compiled to a byte-code but still interpreted at execution & dynamic programing language

Variable -- named storage location used to hold data values
         -- labels for data, allowing you to refer to and manipulate that data
         -- eg Alphabet, numbers, Symbols 

Data type -- type of data 
          -- Number -- int -- intgers & float -- decimal 
          -- Text -- str -- strings 
          -- Boolean -- bool -- True or flase , yes or no, veg or non-veg
          -- None -- none -- null

IO operation -- Input -- input() -- get the data
             -- Output -- print() -- print the result or o/p

Type Conversion -- int, float , str --  We are converting the data type to another data types 
                -- eg x=15/2
                      print(x) -- 7
                      type(x) -- int
                 -- to convert data type int to float 
                    x=float(x)
                    x=15/2
                      print(x) --7.5
                      type(x) -- float 

Name Conversion -- Can be alpha + num
                -- Name starts with alpha
                -- Prefer small case
                -- Constant can be upper case eg PI
                -- Can’t start with number
                -- Don’t start with _
                -- Can be any length
                -- Expected_salary – we need to keep in one word (one token)so we are using underscore

###### Python is used both Programming & Scripting language
Python programming -- all the characteristics of a full-fledged programming language
                   -- various programming like object-oriented, imperative, and functional programming. It's used for building complex applications, web development, data science, machine learning
Scripting language -- excellent for scripting due to its interpreted nature, readability, and extensive libraries
                   -- mostly used for automating tasks, system administration, data manipulation, and creating small, quick programs (scripts) to achieve specific functions.

Different b/w Python 2 and Python 3
Python 2 -- print is statement
         -- String & Unicode -- ASCII (7 bits 128 character) encoded string by default
         Unciode type for characters
         -- Exception Handling -- comma to separate the exception type & variable name
         # code
         except Expection, e:
         -- raw_input() --to get string i/p input()-- evaluate the o/p 
         -- True & flase --not strict keyword it can be reassigned 
         -- Interger Division -- floor division default by intgers and result also in intgers
Python 3 -- print() is function
         -- String & Unicode -- Unicode encoded string by default str represented by Unciode text & bytes for binary data
         -- Exception Handling -- uses the as keyword
         # code
         except Expection as e:
         -- input() --to get string i/p & eval(input())-- evaluate the exp
         -- True & flase --is a keyword it can't be reassigned 
         -- Interger Division -- True division  and result  in float

Different b/w programming & scripting language
Programming language -- Execution -- Compiled(before execution)
                     -- Independence -- self executable
                     -- Purpose -- building standalone applications
                     -- Development -- often more complex (longer time)
                     -- Performance -- Generally faster due to compilation 
                     -- Error Handling -- Error during compilation 
Scripting language -- Execution -- Interpreted (at runtime)
                     -- Independence -- requires a host environment
                     -- Purpose -- automating tasks extending functionality
                     -- Development -- often simpler (faster development)
                     -- Performance -- Can be slower due to interpretation 
                     -- Error Handling -- Error during execution

#### Day 3 (22/11/25)
Conditional Statements:
if elseif else
for in range
while
match case
 