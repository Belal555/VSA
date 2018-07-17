# Classes

# define class
class Person(object):

    # methods

    # initialize
    def __init__(self, name, age):
        # storing attributes
        self.name = name
        self.age = age
        self.living = True

    # other methods
    def update_age(self):
        self.age = self.age + 1

    # accessor method
    def get_age(self):
        return self.age


# creating a person
p1 = Person("Belal Hammad", 17)
print p1.get_age()  # calling a method
print p1.name

p1.living = False
print p1.living


# Creating Subclasses
class Student(Person):
    def set_grade(self, grade):
        self.grade = grade

    def years_until_graduate(self):
        return 13 - self.grade


s1 = Student("Morgan", 17)
s1.set_grade(12)
print s1.years_until_graduate()


