def enum():
  # enumerate
  print("enumerate")
  
my_list = ['a','b','c']
for index,item in enumerate(range(50,551)):
  print(index,item)
  
  # enumerate is a very useful function to use with for loops. Let's imagine the following situation:
  
  # index_count = 0
  
  # for letter in 'abcde':
  #     print("At index {} the letter is {}".format(index_count,letter))
  #     index_count += 1
  # Keeping track of how many loops you've gone through is so common, that enumerate was created so you don't need to worry about creating and updating this index_count or loop_count variable
  
  
  # Notice the tuple unpacking!
  
  # for i,letter in enumerate('abcde'):
  #     print("At index {} the letter is {}".format(i,letter))
  
  
  ##############################enumerators in python #####################################################
  
  
  # Enumerator Practice #1
  # Print sentences like the following on the screen:
  
#'{name} is found at index {index}'
  
  #Where name must be each of the names in the list below, and the index, must be obtained via enumerate().
  
# list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]
  
# You can use the given print() line as an example and change its variable names, but the returned phrases must be the same!
  
  # Tip: use loops!
  
# list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]
  
# print(f'{name} se encuentra en el índice {index}')
# for index, name in enumerate(my_list):
#   print(f"{name} is found at {index}")
  
  
  # Enumerator Practice #2
  # Create a list formed by the tuples (index, element), obtained through enumerating the indices of each character of the "Python" string.
  
  # Call the returned list with the variable name indices_list.
  
  # "Python"
  indices_list = list(enumerate("Python"))
  print(indices-list)
  
  # Enumerator Practice #3
  # Print to the screen only the indices of those names in the list below, that start with M:
  
  list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]
  for i,name in enumerate(list_names):
    if name[0] == "M":
      print(name)
      print(i)
  # You can solve it in different ways, but it will help you keeping mind some (if not all) the following elements:
  
  # loops
  
  # if conditionals
  
  # the enumerate() method
  
  # string methods and indexing
  
  # list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]
  
