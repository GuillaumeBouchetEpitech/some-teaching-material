

#
#
#
# PART 2
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






#
# function that is documented
#



# define the function
def my_function_step7():

    """
    A function that do nothing <3

    Hello 1 <3

    Hello 2 <3

    Hello 3 <3

    Hello 4 <3

    """

# call the function

print("") # spacing in the console
print("STEP7: before the function call")

# HOVER THE MOUSE CURSOR ON THE FUNCTION CALL
# HOVER THE MOUSE CURSOR ON THE FUNCTION CALL
# HOVER THE MOUSE CURSOR ON THE FUNCTION CALL
my_function_step7()
# HOVER THE MOUSE CURSOR ON THE FUNCTION CALL
# HOVER THE MOUSE CURSOR ON THE FUNCTION CALL
# HOVER THE MOUSE CURSOR ON THE FUNCTION CALL

print("STEP7: before the function call")
print("") # spacing in the console








#
# function that has type annotations
#


# define the function
def my_function_step8(valueA: float, valueB: float = 444) -> float:
    print("STEP8: I am inside a function")
    print(f"STEP8: -> valueA is {valueA}")
    print(f"STEP8: -> valueB is {valueB}")

    return valueA + valueB


# call the function

print("") # spacing in the console
print("STEP8: before the function call")

# HOVER THE MOUSE CURSOR ON THE FUNCTION CALL
# HOVER THE MOUSE CURSOR ON THE FUNCTION CALL
# HOVER THE MOUSE CURSOR ON THE FUNCTION CALL
returned_value = my_function_step8(111) # we don't specify the 'valueB' parameter -> will default to 444
# HOVER THE MOUSE CURSOR ON THE FUNCTION CALL
# HOVER THE MOUSE CURSOR ON THE FUNCTION CALL
# HOVER THE MOUSE CURSOR ON THE FUNCTION CALL

print(f"STEP8: returned_value {returned_value}")
print("STEP8: before the function call")
print("") # spacing in the console








#
# function that multiple args
#


# define the function
def my_function_step9(*args) -> None:
    print("STEP9: I am inside a function")
    print(f"STEP9: -> args is {args} (type  is '{type(args)}')")

    for arg in args:
        print(f' ---> {arg}')


# call the function

print("") # spacing in the console
print("STEP9: before the function call")

my_function_step9(11, 22, 33, 44)

print("STEP9: before the function call")
print("") # spacing in the console









#
# function that multiple args as a dict
#


# define the function
def my_function_step9(**kargs) -> None:
    print("STEP9: I am inside a function")
    print(f"STEP9: -> kargs is {kargs} (type  is '{type(kargs)}')")

    for key in kargs:
        print(f' ---> {key} -> {kargs[key]}')


# call the function

print("") # spacing in the console
print("STEP9: before the function call")

my_function_step9(one=11, two=22, three=33, found=44)

print("STEP9: before the function call")
print("") # spacing in the console






