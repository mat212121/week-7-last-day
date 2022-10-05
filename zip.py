def zip():
  # zip
  # Notice the format enumerate actually returns, let's take a look by transforming it to a list()
  # list(enumerate('abcde'))
  print("zip")
  
  
  # It was a list of tuples, meaning we could use tuple unpacking during our for loop. This data structure is actually very common in Python , especially when working with outside libraries. You can use the zip() function to quickly create a list of tuples by "zipping" up together two lists.
  
  
  mylist1 = [1,2,3,4,5]
  mylist2 = ['a','b','c','d','e']
  
  # This one is also a generator! We will explain this later, but for now let's transform it to a list
  zip(mylist1,mylist2)
  
  
  # list(zip(mylist1,mylist2))
  
  
  
  
  
  # in operator
  # We've already seen the in keyword during the for loop, but we can also use it to quickly check if an object is in a list
  
  # 'x' in ['x','y','z']
  # True
  # 'x' in [1,2,3]
  # False
  
  
  
  # not in
  # We can combine in with a not operator, to check if some object or variable is not present in a list.
  
  # 'x' not in ['x','y','z']
  # False
  # 'x' not in [1,2,3]
  # True
  
  
  
  ######################################### zip in python############################################
  
  
  
  # Zip Practice #1
  # Print to the screen phrases like the following example:
  
  # "The capital of Germany is Berlin"
  
  # Use the zip function, loops, and the following lists of countries and capitals to solve it quickly and efficiently.
  
  # capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
  # countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]
  
  
  
  # Zip Practice #2
  # Create a zip object made up of lists, of a set of brands and products that you prefer, inside the my_zip variable.
  # brands =
  # products =
  
  
  # Zip Practice #3
  # Create a zip object with the translations of the numbers from 1 to 5 in Spanish, Portuguese and English (in that same order), and then convert the generated object into a list called numbers:
  
  # one / um / one
  
  # two / two / two
  
  # three / three / three
  
  # four / four / four

# five / five / five

# The result should follow the structure:

# [('one', 'um', 'one'), ('two', 'dois', 'two'), ... ]

# 1: uno / um / one
# 2: dos / dois / two
# 3: tres / três / three
# 4: cuatro / quatro / four
# 5: cinco / cinco / five



