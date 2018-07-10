# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
#key word is for
#loop over a range of #s
# sum = 0
# for num in range (51):
#     sum = sum + num
#     print sum
#
# s = "vsa"
# #loop over strings
# for letter in s:
#     print letter
#     if letter == "s":
#         print "This is an s"

prev_num = 0
current_num = 1
next_num = prev_num + current_num
num = 0
user_input = int(raw_input("How many Fibonacci numbers would you like to generate?"))
for num in range (user_input):
    print current_num
    next_num = prev_num + current_num
    prev_num = current_num
    current_num = next_num

# counter = 0
#
# while counter == 0:
#     user_n = int(raw_input("How many Fibonacci numbers would you like to generate?"))
#     print current_num
#     next_num = prev_num + current_num
#     prev_num = current_num
#     current_num = next_num
#     break







