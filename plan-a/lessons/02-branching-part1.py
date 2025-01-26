
#
#
# Branching
#
#


#
#
#
# PART 1
#
#
#

print("")
print("")
print("#" * 30)
print("# PART 1")
print("#")
print("")
print("")



#
# single 'if' statement
#

if True: # this pass
    print("hello") # always print

if False: # this does not pass
    print("hello") # never print



#
# 'if-else' statement
#

if True: # this pass
    print("hello") # always print
else:
    print("hello") # never print (first 'if' was first)



if False:
    print("hello") # never print
else: # this pass
    print("hello") # always print


#
# 'if-elif' statement
#


if True: # this pass
    print("hello") # always print
elif True:
    print("hello") # never print (first 'if' was first)



if False:
    print("hello") # always print
elif True: # this pass
    print("hello") # never print



#
# 'if-elif-else' statement
#


if True: # this pass
    print("hello") # always print
elif True:
    print("hello") # never print (first 'if' was first)
else:
    print("hello") # never print (first 'if' was first)



if False:
    print("hello") # never print
elif True: # this pass
    print("hello") # always print
else:
    print("hello") # never print (first 'elif' was first)



if False:
    print("hello") # never print
elif False:
    print("hello") # never print
else: # this pass
    print("hello") # always print





# branching operators

# less than
print("less than")
print(f" (1 < 100) = {1 < 100}") # -> True

# greater than
print("greater than")
print(f" (1 > 100) = {1 > 100}") # -> False

# double condition
print("double condition")
my_number = 55
print(f" (1 <= my_number({my_number}) <= 100) = {1 <= my_number <= 100}") # -> True -> is inside the range 1..100
my_number = -5
print(f" (1 <= my_number({my_number}) <= 100) = {1 <= my_number <= 100}") # -> False -> is outside the range 1..100
my_number = 105
print(f" (1 <= my_number({my_number}) <= 100) = {1 <= my_number <= 100}") # -> False -> is outside the range 1..100

# is equal
print("is equal")

print(f" (50 == 50) = {50 == 50}") # -> True
print(f" (50 == 60) = {50 == 60}") # -> False

print(f' ("hello" == "hello") = {"hello" == "hello"}') # -> True
print(f' ("hello" == "world") = {"hello" == "world"}') # -> False


# is not equal
print("is not equal")
print(f" (50 != 50) = {50 != 50}") # -> False
print(f" (50 != 60) = {50 != 60}") # -> True

print(f' ("hello" != "hello") = {"hello" != "hello"}') # -> False
print(f' ("hello" != "world") = {"hello" != "world"}') # -> True

# less or equal than
print("less or equal than")
print(f" (20 <= 20) = {20 <= 20}") # -> True
print(f" (20 <= 30) = {20 <= 30}") # -> True
print(f" (30 <= 20) = {30 <= 20}") # -> False

# greater or equal than
print("greater or equal than")
print(f" (20 >= 20) = {20 >= 20}") # -> True
print(f" (20 >= 30) = {20 >= 30}") # -> False
print(f" (30 >= 20) = {30 >= 20}") # -> True


