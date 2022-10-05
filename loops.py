def loop():
  # names = ["mary", "john", "david","thomas", "janette"]
  # # print(names[0])
  # # print(names[1])
  # # print(names[2])
  # # print(names[3])
  # # print(names[4])
  # for name in names:
  #   print(f"hello {name}")


  # a = 1
  # while a < 10 :
  #   print(a)
  #   a = a + 1

  # num_list = [1,2,3,4,5,6,7,8,9,10]
  
  # for num in num_list:
  #   sum = 0
  #   sum = sum + num
  #   print(sum)
  # names = ["mary", "john", "david","thomas", "janette"]

  # for name in names:
  #   if name.startswith("j"):
  #     print(f"this {name} starts with j")

  #dictionaries
  # dic = {"key1": "a", "key2":"b", "key3": "c"}
  # #.items() gives back the values
  # # for item in dic.items():
  # #   print(item)
  # for a,b in dic.items():
  #   print(a,b)

  #while loops
  # coins = 30
  # while coins < 40:
  #   print(f"I have {coins} coins")
  #   coins += 1

  # answer = "y"
  # while answer == "y":
  #   answer = input("do you want to continue(y/n)")
  # else:
  #   print("thank you")
  
  ###################################loops intro######################################
  # queue videos
  #what is iteration?
  #what are for loops?
  
  #   for Loops
  # A for loop acts as an iterator in Python; it goes through items that are in a sequence or any other iterable item. Objects that we've learned about that we can iterate over include strings, lists, tuples, and even built-in iterables for dictionaries, such as keys or values.
  
  # We've already seen the for statement a little bit in past lectures but now let's formalize our understanding.
  
  # Here's the general format for a for loop in Python:
  
  # for item in object:
  #     statements to do stuff
  # The variable name used for the item is completely up to the coder, so use your best judgment for choosing a name that makes sense and you will be able to understand when revisiting your code. This item name can then be referenced inside your loop, for example if you wanted to use if statements to perform checks.
  
  # Let's go ahead and work through several example of for loops using a variety of data object types. We'll start simple and build more complexity later on.

# extra practice
  # iterate through the following list:
  # # We'll learn how to automate this sort of list in the next lecture
  list1 = [1,2,3,4,5,6,7,8,9,10]



  #   Modulo
  # The modulo allows us to get the remainder in a division and uses the % symbol. For example:
  
  # 17 % 5
  
  
  
  # This makes sense since 17 divided by 5 is 3 remainder 2. Let's see a few more quick examples:
  
  # # 3 Remainder 1
  # 10 % 3
  # 1
  # # 2 Remainder 4
  # 18 % 7
  # 4
  # # 2 no remainder
  # 4 % 2

  #   0
  # Notice that if a number is fully divisible with no remainder, the result of the modulo call is 0. We can use this to test for even numbers, since if a number modulo 2 is equal to 0, that means it is an even number!
  
  # Back to the for loops!

  # let's print only the even numbers from that list!
  # list1 = [1,2,3,4,5,6,7,8,9,10]

  
  

    
  # For Loops Practice #1
  # Using For loops, greet all members of a class, printing "Hello" + their name.
  
  # For example: "Hello Norville"
  
  students = ["Norville", "Fred", "Velma", "Daphne"]
  
  for name in students:
    print(f"hello {name}")
  
  
  # For Loops Practice #2
  # Given the following list of numbers, calculate the sum of all the numbers using For loops and store the result of the sum in a variable called sum_numbers:
  
  list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
  sum_numbers = 0 
  for list_numbers in list_numbers:
    sum_numbers = sum_numbers +list_numbers
    print(f" sum of list numbers is {sum_numbers}")
  
  
  
  
  # For Loops Practice #3
  # Given the following list of numbers, perform the sum of all even and odd* numbers separately in the variables sum_even and sum_odd respectively:
  
  list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
  
  # *Recall from previous days: the modulus (or remainder) of a number divided by 2 is zero when said value is even, and 1 when it is odd
  
  # num % 2 == 0 (even values)
  
  # num % 2 == 1 (odd values)
  
  list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
  
  # sum_even = 
  
  # sum_odd = 



