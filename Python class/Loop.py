# for loop & While loop 
# what is different b/w while & for 

# Continuous in life 
# eg auto renuwal - billing generate 
# clock 
# count down timer 
# heart beat 
# passing the value in function is parameter while calling the function it's agrument 

# while - we need termination but for clock example we no need terminate because it's indefinite

# while expression:
#      statement 1
# 

# For Loop:
# Iteration over Sequences: A for loop is primarily used for iterating over a sequence (like lists, tuples, strings, dictionaries, or ranges) where the number of iterations is typically known or determined by the length of the sequence.
# Syntax: It directly iterates over the elements of a sequence.


 #   for item in sequence:
        # code to execute for each item
#While Loop:
#Conditional Repetition: A while loop is used to repeatedly execute a block of code as long as a specified condition remains True. The number of iterations is not necessarily known beforehand and depends on when the condition becomes False.
#Syntax: It requires a condition that is evaluated before each iteration.


#    while condition:
        # code to execute while condition is True
#Key Differences Summarized:
#Known vs. Unknown Iterations: for loops are suitable when the number of iterations is known or defined by a sequence's length. while loops are used when the number of iterations is unknown and depends on a dynamic condition.
#Iteration Mechanism: for loops iterate directly over elements of a sequence. while loops repeat based on a boolean condition.
#Initialization and Increment: In for loops using range(), the initialization and increment of the loop variable are implicitly handled. In while loops, the initialization of variables and their modification within the loop (to eventually make the condition False) must be explicitly managed.
#Common Use Cases: for loops are common for processing items in collections, performing actions a fixed number of times (e.g., using range()). while loops are used for scenarios like user input validation (looping until valid input is received), implementing algorithms that continue until a specific state is reached, or handling indefinite repetition based on a condition.

seconds = 1

while True:
    print(seconds)
    seconds = seconds + 1

    if seconds > 60:
        break

# while seconds < 60:
#     print (seconds)
#     seconds = seconds + 1

def print_update(num):
    pass



