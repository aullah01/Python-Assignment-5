# Problem # 1:
# Extracting Sublist from a List of Temperatures
# Objective: Given a list of daily temperatures for a month, extract the temperatures for a specific week (e.g., week 2).
# temperatures = [22, 24, 20, 25, 23, 26, 24, 25, 27, 29, 30, 28, 26, 27, 24, 23, 22, 21, 25, 24, 26, 27, 29, 28, 26, 25, 24, 23, 22, 21]

# Solution:

# temperatures = [22, 24, 20, 25, 23, 26, 24, 25, 27, 29, 30, 28, 26, 27, 24, 23, 22, 21, 25, 24, 26, 27, 29, 28, 26, 25, 24, 23, 22, 21]

# week_3_temp = temperatures[14:21]
# print("Temperature for  week 3 is: ", week_3_temp)

# Problem # 2:
"""
Extracting a Substring from a Sentence
Objective: Given a sentence, extract and print a specific word using string slicing.
sentence = "The quick brown fox jumps over the lazy dog"
extract third word "brow"
"""
# Solution:

# sentence = "The quick brown fox jumps over the lazy dog"

# third_word = sentence[9:14]
# print("Third word is:",third_word)

# Problem # 3:
"""
Extracting a Sublist of Favorite Colors
Objective: Given a list of favorite colors, extract a sublist of the first three colors using list slicing.
favorite_colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
extract first three colors
"""
# Solution:

# favorite_colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]

# favorite_colors = favorite_colors[:3]

# print(favorite_colors)

# Problem # 4:

# Write a Python program to check if a list is empty or not.

# Solution:

# empty_list = []

# if not empty_list:
#     print("List is empty")
# else:
#     print("List is not empty")
    

# Problem # 5:

# 1. output the numbers from 1 to 10 using range function and for loop
# output should be like
# 1
# 2
# 3
# etc

# Solution:

# for i in range(1,11):
#     print(i)


# Problem # 6:

# 2. output the numbers from 35 to 50 using range function and for loop
# output should be like
# 35
# 36
# 37
# etc

# Solution:

# for i in range(35,51):
#     print(i)



# Problem # 7:

# 3. output the numbers from -15 to -25 using range function and for loop
# output should be like
# -15
# -16
# -17
# etc

# Solution:

# for i in range(-15,-26,-1):
#     print(i)


# Problem # 8:

# 4. output the numbers from 5 to -10 using range function and for loop
# output should be like
# 5
# 4
# 3
# etc

# Solution:

# for i in range(5,-11,-1):
#     print(i)


# Problem # 9:

# 5. output the numbers from 0 to 50 incremented by 3 using range function and for loop
# output should be like
# 0
# 3
# 6
# 9
# etc

# Solution:

# for i in range(0,51,3):
#     print(i)

# Problem # 10:

# 6.  Write a program to Generate Multiplication Table of 2 using range function and for loop
# output format should be like
# 2 x 1 = 2
# 2 x 2 = 4
# etc

# Solution:

# for i in range(1,11):
#     output = 2 * i
#     print("2 x", i, "=", output)


# Problem # 11:

# 7. Write a Python program to sum all the items in a list use for loop. consider the list [3, 5, 2, 1, 4]
# output should be 15
# hint: 
# create a variable x outside the loop and assign the value 0
# inside the loop increment the value of x with the local variable of loop
# x += i

# Solution:

# x = 0
# list = [3,5,2,1,4]

# for i in list:
#     x += i
# print(x)


# Problem # 12:

# 8. Write a Python program to get the largest number from a list and use for loop consider the list [3, 5, 2, 1, 4]
# output should be 5
# hint:
# create a variable x outside the loop and assign the value 0
# inside the loop compare the variable x with the local variable of loop

# Solution:

# x = 0
# list = [3,5,2,1,4]

# for i in list:
#     if i > x:
#         x = i
# print(x)


# Problem # 13:

# Exercise 1: Sum of Elements in a List
# Objective: Write a Python program that calculates the sum of all elements in a given list.
# Example list
# numbers = [10, 20, 30, 40, 50]

# Solution:
# sum = 0
# numbers = [10, 20, 30, 40, 50]

# for i in numbers:
#     sum = sum + i
#     print(sum)
# print("Sum of all emlements: ", sum)


# Problem # 14:

# Count Even and Odd Numbers in a List
# Objective: Write a Python program that counts the number of even and odd numbers in a given list.
# Example list
# numbers = [12, 7, 9, 24, 18, 5, 3, 20]

# Solution:

# numbers = [12, 7, 9, 24, 18, 5, 3, 20]
# even = 0
# odd = 0
# for i in numbers:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("No of even numbers: ", even)
# print("No of odd numbers: ", odd)


# Problem # 15:

# Print List Elements with Their Indices
# Objective: Write a Python program that prints each element of a list along with its index.
# Example list
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# output should like
# "Index: 0 Element: apple"
# "Index: 1 Element: banana"
# "Index: 2 Element: cherry"

# Solution:

# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# for i in fruits:
#     print("Index: ", fruits.index(i), "Element: ", i)


# Problem # 16:

# Create a List of Even Numbers from 1 to 20
# Objective: Write a Python program that creates a list of all even numbers from 1 to 20.

# solution:

# list = []

# for i in range(1,21):
#     if i % 2 == 0:
#         list.append(i)
# print(list)
    

# Problem # 17:


# Find Common Elements Between Two Lists
# Objective: Write a Python program that finds and prints the common elements between two lists.
# Example lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# Solution:

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# for i in list1:
#     if i in list2:
#         print(i)   


# Problem # 18:

# Find the Length of Each String in a List
# Objective: Write a Python program that finds and prints the length of each string in a given list.
# Example list
# strings = ["apple", "banana", "cherry", "date"]

# Solution:

# strings = ["apple", "banana", "cherry", "date"]

# for i in strings:
#     print("Index :", strings.index(i),"Element :",i ,"Length of Element :",len(i))
    
    
    
    
    
    
    
    
    
    
    