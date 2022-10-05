def range():
  # Useful Operators
    # There are a few built-in functions and "operators" in Python that don't fit well into any category, so we will go over them in this lecture, let's begin!
    print("range")
    # range
    # The range function allows you to quickly generate a list of integers, this comes in handy a lot, so take note of how to use it! There are 3 parameters you can pass, a start, a stop, and a step size. Let's see some examples:
  # instead of doing this:  
  # my_list = [0,1,2,3,4,5,6,7,8,9,10,11]
  #you can do this instead
  #   range(0,11)
  
  
  #   Note that this is a generator function, so to actually get a list out of it, we need to cast it to a list with list(). What is a generator? Its a special type of function that will generate information and not need to save it to memory. We haven't talked about functions or generators yet, so just keep this in your notes for now, we will discuss this in much more detail in later on in your training!
  
  
  
  # # Notice how 11 is not included, up to but not including 11, just like slice notation!
  # list(range(0,11))
  
  
  # Third parameter is step size!
  # step size just means how big of a jump/leap/step you 
  # take from the starting number to get to the next number.
  
  # list(range(0,11,2))
  
  # list(range(0,101,10))
  
  ##############################ranges#####################################################
  
  # Range Practice #1
  # Create a list consisting of all the numbers from 2500 to 2585 (inclusive). Store this list in the variable my_list.
  
  
  
  # Range Practice #2
  # Using the range() function, create in a single line of code a list consisting of all numbers that are multiples of 3 from 3 to 300 (inclusive). Store this list in the variable my_list.
  
  
  
  # Range Practice #3
  # Use the range() function and a loop to add the squares of all the numbers from 1 to 15 (inclusive). Store the result in a variable called sum_squares.
  
  
  
  # For this purpose:
  
  # Create a range of values that you can iterate through in a loop
  
  # For each of these values, find its squared value (power of 2). You may need to create intermediate variables (optionally).
  
  # Sum all the squared values obtained. Accumulate the sum in the variable sum_squares.
  
  
