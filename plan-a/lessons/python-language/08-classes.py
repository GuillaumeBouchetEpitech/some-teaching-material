


print("") # spacing in the console





my_number_a = 2
my_number_b = 3

# this operation
print(my_number_a + my_number_b) # 5

# is in fact this operation
print(my_number_a.__add__(my_number_b)) # 5


# "my_number_a" is an "object"

# an "object" is constructed from a "class"

# a "class" is a blueprint of an "object"

# the "class" of "my_number_a" is "int"

# a "class" can possess "functions" -> here we just saw "__add__" from the class "int"

# when a "class" has "functions" those "functions" are called "methods"

# to sum it up:
# -> the variable "my_number_a"...
# -> ...holds an "object"...
# -> ...from the class "int"...
# -> ...that possess the method "__add__"




# other example

my_str = "hello" # my variable "my_str" hold an "object" of class "str"
my_str.upper() # the object of class "str" possess the method "upper()"
my_str.lower() # the object of class "str" possess the method "lower()"
my_str.capitalize() # etc.





# in Python we can create classes




# this is the syntax:

class my_class:


  # the "__init__" method is called when the class create a new object
  # the exact name is -> "__init__" is the "constructor" method of my_class
  def __init__(self):
    # the "self" variable represent the object

    # variables that belong to "self" is named an "attribute"
    self._my_attribute = 0


  # here we create a method "my_method"
  # it accept 2 parameters: "my_parameterA" and "my_parameterB"
  def my_method(self, my_parameterA, my_parameterB):
    self._my_attribute = my_parameterA + my_parameterB



my_object = my_class() # construct a new object from the class "my_class"

print(f"#1 my_object._my_attribute = {my_object._my_attribute}") # 0



my_object._my_attribute = 123 # set the

print(f"#2 my_object._my_attribute = {my_object._my_attribute}") # 123



my_object.my_method(222, 111) # call to the method "my_method"

print(f"#3 my_object._my_attribute = {my_object._my_attribute}") # 333



print("") # spacing in the console







# in software engineering there is a practice call "OOP"

# "OOP" stand for "Object Oriented Programming"

# the goal of "OOP" is to "abstract" the logic in reusable blocks -> objects

# ex: int, float, str, etc.










print("") # spacing in the console
