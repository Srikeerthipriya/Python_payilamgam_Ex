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
 

 Predefined function:
 predefined functions (also called built-in functions) are functions that come with Python by default. You can use them anytime without importing anything

| Function  | What it does                    |
| --------- | ------------------------------- |
| `print()` | Displays output                 |
| `len()`   | Returns length of a sequence    |
| `type()`  | Returns the data type           |
| `input()` | Takes user input                |
| `max()`   | Returns the largest value       |
| `min()`   | Returns the smallest value      |
| `sum()`   | Adds elements in a list         |
| `range()` | Generates a sequence of numbers |

Userdefined function:
user-defined functions are functions that you create yourself to perform specific tasks. They are different from predefined (built-in) functions because they are written by the programmer, not by Python.
user-defined function is a block of code written by you that runs only when it is called.
You create it using the def keyword.

| Feature           | User-Defined Functions                               |
| ----------------- | ---------------------------------------------------- |
| Who creates them? | The programmer                                       |
| Why use them?     | Reusability, readability, organization, fewer errors |
| How to create?    | Using `def` keyword                                  |
| When to use?      | When the built-in functions are not enough           |

| Feature               | Predefined Functions                              | User-Defined Functions                                    |
| --------------------- | ------------------------------------------------- | --------------------------------------------------------- |
| **Who creates them?** | Built into Python (created by Python developers)  | Created by the programmer                                 |
| **Availability**      | Always available without import                   | Available only after you define them                      |
| **Examples**          | `print()`, `len()`, `range()`, `input()`, `max()` | Any function you write using `def`                        |
| **Purpose**           | Perform common tasks quickly                      | Perform custom or repeated tasks specific to your program |
| **Speed**             | Very fast (written in C internally)               | Depends on your code                                      |
| **Flexibility**       | Fixed functionality                               | You can design the function however you want              |

input() is a predefined function in Python because:

Python provides it automatically
It performs a common task (getting user input)
You don’t need to write or import code to use it
It is part of Python’s built-in functions
