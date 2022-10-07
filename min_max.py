def min_max():
  # min and max
  print("min and max")
  # Quickly check the minimum or maximum of a list with these functions.
  
  mylist = [10,20,30,40,100]
  mylist2 = (range(20,38))
  # print(min(mylist))
  # 10
  print(max(mylist))
  # 100
  print(list(zip(mylist, mylist2)))
  #################################################min/max######################################
  
  # Min & Max Practice #1
  # Get the maximum value among the values in the following list, and store it in a variable named maximum_value:
  
number_list = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
maximum_value = max(number_list)
print(maximum_value)
  
  
  
  # Min & Max Practice #2
  # Calculate the difference between the maximum and minimum value in the following list of numbers, and store it in a variable called number_range:
  
number_list = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
bignum = max(number_list)
smllnum = min(number_list)
number_range = bignum - smllnum
print(number_range)
  # Min & Max Practice #3
  # Using max(), min(), and dictionary methods, get the minimum value from the following dictionary:
  
dictionary_ages = {"Tony":55, "Paulie":42, "Meadow":78, "Vito":44, "Ralph":24, "Sarah":35, "Evan":19, "Jean":2 ,"Ned":49}
minimum_age = min(dictionary_ages.values)  
last_name = max(dictionary_ages.keys())
print(minimum_age)
print(last_name)
  # Store this value in a variable called minimum_age.
  
  # Also, get the name that comes last in alphabetical order, and store it in a variable called last_name.
  
