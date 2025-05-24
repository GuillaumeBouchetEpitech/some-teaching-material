
#
#
#
#  PART 2
#
#
#

print("")
print("")
print("#" * 30)
print("# PART 2")
print("#")
print("")
print("")










my_listInt: list[int] = []



print(f"len(my_list) -> {len(my_listInt)}") # -> 0

# fill the list with a range iterator call
my_listInt.extend(range(0,5)) # -> [0,1,2,3,4]


# Note -> it's OK if the 'range' function does not make sense


print(f"len(my_listInt) -> {len(my_listInt)}") # -> 5

# loop alt1 (preferred)
print("loop alt1")
for my_item in my_listInt:
    print(f" ---> {my_item}")

# loop alt2 (Not preferred)
print("loop alt2")
for index in range(0, (len(my_listInt))):
    print(f" ---> {my_listInt[index]}")






# easy way to check if a value is in a list
print(f"my_listInt -> {my_listInt}")
print(f"0 in my_listInt -> {0 in my_listInt}") # True
print(f"1 in my_listInt -> {1 in my_listInt}") # True
print(f"2 in my_listInt -> {2 in my_listInt}") # True
print(f"3 in my_listInt -> {3 in my_listInt}") # True
print(f"4 in my_listInt -> {4 in my_listInt}") # True
print(f"5 in my_listInt -> {5 in my_listInt}") # False






# search an item and find it's index

my_list: list[str] = ['one', 'two', 'three', 'four', 'five']
print(f"my_list -> {my_list}")

to_search = 'three' # search for value 3

# check first if part of the list
if 'three' in my_list:

    # actually the item's index in the list
    print(f"my_list.index('three') -> {my_list.index('three')}")



print("") # spacing in the console



# list are object that are 'referenced'

my_list: list[str] = ['one', 'two', 'three', 'four', 'five']
my_second_list = my_list

print(f"my_list        -> {my_list}") # ['one', 'two', 'three', 'four', 'five']
print(f"my_second_list -> {my_second_list}") # ['one', 'two', 'three', 'four', 'five']

print(f"id(my_list)        -> {id(my_list)}") # it's internal to python
print(f"id(my_second_list) -> {id(my_second_list)}") # it's internal to python

# are 'my_list' and 'my_second_list' referencing the same list?
if id(my_list) == id(my_second_list):
    print('both variables are referencing the same list') # printed
else:
    print('both variables are NOT referencing the same list') # not printed

# are 'my_list' and 'my_second_list' referencing the same list?
if my_list is my_second_list:
    print('both variables are referencing the same list') # not printed
else:
    print('both variables are NOT referencing the same list') # printed



# changes made to 'my_second_list' will affect my_list

my_second_list.append('siiiiiix')

print(f"my_list        -> {my_list}") # ['one', 'two', 'three', 'four', 'five', 'siiiiiix']
print(f"my_second_list -> {my_second_list}") # ['one', 'two', 'three', 'four', 'five', 'siiiiiix']

# and vice versa

my_list.append('seveeeen')

print(f"my_list        -> {my_list}") # ['one', 'two', 'three', 'four', 'five', 'siiiiiix', 'seveeeen']
print(f"my_second_list -> {my_second_list}") # ['one', 'two', 'three', 'four', 'five', 'siiiiiix', 'seveeeen']

print("") # spacing in the console






# how to duplicate a list

my_list: list[str] = ['one', 'two', 'three', 'four', 'five']
my_second_list = [x for x in my_list]

print(f"my_list        -> {my_list}") # ['one', 'two', 'three', 'four', 'five']
print(f"my_second_list -> {my_second_list}") # ['one', 'two', 'three', 'four', 'five']

# are 'my_list' and 'my_second_list' referencing the same list?
if id(my_list) == id(my_second_list):
    print('both variables are referencing the same list') # not printed
else:
    print('both variables are NOT referencing the same list') # printed


# are 'my_list' and 'my_second_list' referencing the same list?
if my_list is my_second_list:
    print('both variables are referencing the same list') # not printed
else:
    print('both variables are NOT referencing the same list') # printed




# changes made to 'my_second_list' will NOT affect my_list

my_second_list.append('siiiiiix')

print("") # spacing in the console

print(f"my_list        -> {my_list}") # ['one', 'two', 'three', 'four', 'five']
print(f"my_second_list -> {my_second_list}") # ['one', 'two', 'three', 'four', 'five', 'siiiiiix']

# and vice versa

my_list.append('seveeeen')

print("") # spacing in the console

print(f"my_list        -> {my_list}") # ['one', 'two', 'three', 'four', 'five', 'seveeeen']
print(f"my_second_list -> {my_second_list}") # ['one', 'two', 'three', 'four', 'five', 'siiiiiix']

print("") # spacing in the console











