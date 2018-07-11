# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""

# var = []
# var2 = ["a", "b", "cat", 3]
#
# #index - 0 indexed
# #one item
# print var2[2]
# # slice of list
# print var2[0:1]
# #all but the first
# print var2[1:]
# #all but the last
# print var2[:-1]
#
# #replace
# var2[0] = "tree"
# print var2
#
# #loop
# #to change
# counter = 0
# for item in var2:
#     if item == "cat": #searches for cat"
#             var2[counter] = "dog"
#     elif item == "tree":
#             var2[counter] = "flower"
#     counter = counter + 1
# print var2
#
# #add to a list
# var2.append("28")
# print var2
#
# lst = []
# s = "This is a string"
# for letter in s:
#     lst.append(letter)
#
# print lst

#if cat not/in var2:
    #print "cat"


#Part I
#Take a list, say for example this one:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b= []
# #and write a program that prints out all the elements of the list that are less than 5.
# counter = 0
# for item in a:
#     if item < 5:
#         b.append(item)
#         counter = counter + 1
# print b










#Part II
# Take two lists, say for example these two:
# b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# b = [46, 354, 76, 24, 86, 3456]
# c = [45, 234, 76, 23, 84, 3456]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
# counter = 0
# for item in b:
#     if item in c:
#         print item
#     counter = counter + 1


# list = ["Michele", "Sara", "Cassie"]
# name = raw_input("Type name to check:")
# counter = 0
# for item in list:
#     if name in list:
#         print ("This student is enrolled.")
#         break
#     elif name not in list:
#         print ("This student is not enrolled")
#         break





#Part III
# Take a list, say for example this one:

# d = ["b", "a", "f", "y", "a", "t", "a", "p", "a", "R"]
# # and write a program that replaces all “a” with “*”.
# counter = 0
# for item in d:
#     if item == "a":
#         d[counter] = "*"
#     counter = counter + 1
# print d




# a = [2, 3, 6]
# print len(a)



#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.
# counter = 0
# lst = []
# p = raw_input("Enter a word: ")
# for letter in p:
#     lst.append(letter)
#     print lst
# print len(lst)
# while len(lst) > 2:
#     print "here"
#     if lst[0] == lst[-1]:
#         lst = lst[1:-1]
#         print ("This is a palindrome.")
#         print lst
#     else:
#         print ("This is not a palindrome.")
#         break
#     counter = counter + 1


counter = 0
lst = []
p = raw_input("Enter a word: ")
for letter in p:
    lst.append(letter)
while len(lst) > 2:
    if lst[0] == lst[-1]:
        lst = lst[1:-1]
        print ("This is a palindrome.")
    else:
        print ("This is not a palindrome.")
        break
    counter = counter + 1






