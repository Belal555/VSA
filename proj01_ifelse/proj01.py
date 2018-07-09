# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday


# If you complete extensions, describe your extensions here!
# var name  input from user

# user_name = raw_input("Enter your name: ")
# str = user_name
# str = user_name[0].upper() + user_name[1:].lower()
# print str
# user_grade = raw_input("Enter your grade: ")
# x = 12 - int(user_grade)
# print "You will graduate in" , x , "year!"


# age = 16
# if age > 16:
#     print "you can drive!"
#     print "this is still in the if statement"
#     print "over", 16
# elif age == 16:
#     print "you can drive in some states"
# elif age > 95:
#     print "you're too old to drive"
# else:
#     print "you can't drive!"

name = raw_input("Enter your name: ")
birth_month = raw_input("Enter your birth month: ")
birth_day = raw_input("Enter your birth day: ")
# a = int(birth_month) - 7
# b = int(birth_day) - 9
c = name
current_month = 7
current_day = 9
if birth_month > current_month:
    a = int(birth_month) - 7
else:
    a = 7 - int(birth_month)
if birth_day > current_day:
    b = int(birth_day) - 9
else:
    b = 9 - int(birth_day)
print c, "your birthday is in" ,a, "months and" ,b, "days!"