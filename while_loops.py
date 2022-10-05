

########################################loops############################################################
# while Loops
# The while statement in Python is one of most general ways to perform iteration. A while statement will repeatedly execute a single statement or group of statements as long as the condition is true. The reason it is called a 'loop' is because the code statements are looped through over and over again until the condition is no longer met.

# The general format of a while loop is:

# while condition:
#     code statements
# else:
#     final code statements

# so a while loop is basically a way for python to loop through code several times until a condtion is met
# Let’s look at a few simple while loops in action.
#queue video about loops
# i = 1
# while i < 10:
#   print(i)
#   i = i + 1
#   # or i += 1

# print("done with loop")


# we can use a while loop to continually ask the user to guess a word until they guess it correctly
# secret_word ="giraffe"
# guess= ""

# while guess != secret_word:
#   guess = input("enter a guess: ")

# print("you win")


# While Loops Practice #1
# Create a While Loop that prints the numbers 10 to 0 on the screen, one at a time.

number = 10



# While Loops Practice #2
# Create a While Loop that subtracts one by one the numbers from 50 to 0 (both numbers included) with the following additional conditions:

# If the number is divisible by 5, show that number on the screen (remember that here you can use the modulus operation dividing by 5 and checking the remainder!)

# If the number is not divisible by 5, continue executing the loop without showing the value on the screen (don't forget to continue subtracting so that the program doesn't run infinitely).

number = 50



# Loop Interruption Statements Practice
# Create a For loop through the following list of numbers, printing each of its elements to the screen, and interrupt the flow when you find a negative value:

# list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

# You must not change the order of the list.

list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
