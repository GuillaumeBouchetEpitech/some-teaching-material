
#
#
# Functions
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
# simple function
#


# define the function
def my_function_step1():
    print("STEP1: I am inside a function")

# call the function

print("") # spacing in the console
print("STEP1: before the function call")

my_function_step1()

print("STEP1: before the function call")
print("") # spacing in the console






#
# function that accept parameter(s)
#



# define the function
def my_function_step2(valueA, valueB):
    print("STEP2: I am inside a function")
    print(f"STEP2: -> valueA is {valueA}")
    print(f"STEP2: -> valueB is {valueB}")


# call the function

print("") # spacing in the console
print("STEP2: before the function call")

my_function_step2(111, 222)

print("STEP2: before the function call")
print("") # spacing in the console






#
# function that do returns
#



# define the function
def my_function_step3(valueA, valueB):
    print("STEP3: I am inside a function")
    print(f"STEP3: -> valueA is {valueA}")
    print(f"STEP3: -> valueB is {valueB}")

    return valueA + valueB


# call the function

print("") # spacing in the console
print("STEP3: before the function call")

returned_value = my_function_step3(111, 222)

print(f"STEP3: returned_value {returned_value}")
print("STEP3: before the function call")
print("") # spacing in the console









#
# function that do NOT returns
#



# define the function
def my_function_step4():
    print("STEP4: I am inside a function that does NOT return")


# call the function

print("") # spacing in the console
print("STEP4: before the function call")

returned_value = my_function_step4()

print(f"STEP4: (returned_value is None) -> {returned_value is None}")
print("STEP4: before the function call")
print("") # spacing in the console









#
# function with parameters with default values
#



# define the function
def my_function_step5(valueA, valueB = 444): # here "valueB" has a default value if 444
    print("STEP5: I am inside a function")
    print(f"STEP5: -> valueA is {valueA}")
    print(f"STEP5: -> valueB is {valueB}")

    return valueA + valueB


# call the function

print("") # spacing in the console
print("STEP5: before the function call")

returned_value = my_function_step5(111) # we don't specify the 'valueB' parameter -> will default to 444

print(f"STEP5: returned_value {returned_value}")
print("STEP5: before the function call")
print("") # spacing in the console









#
# function with parameters that is used with the parameters names
#



# define the function
def my_function_step6(valueA, valueB = 444, valueC = 555):
    print("STEP6: I am inside a function")
    print(f"STEP6: -> valueA is {valueA}")
    print(f"STEP6: -> valueB is {valueB}")

    return valueA + valueB + valueC


# call the function

print("") # spacing in the console
print("STEP6: before the function call")

returned_value = my_function_step6(111, valueC=666) # <- we forcefully specify valueC

print(f"STEP6: returned_value {returned_value}")
print("STEP6: before the function call")
print("") # spacing in the console


















