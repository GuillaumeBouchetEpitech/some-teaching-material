
#
#
# Built-in type: dict
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


my_dict = {} # -> empty dict
print(my_dict) # -> {}



print("") # spacing in the console

my_dict["one"] = 1 # set key-value pair 'one' -> 1
my_dict["two"] = 2 # set key-value pair 'two' -> 2
my_dict["three"] = 3 # set key-value pair 'three' -> 3

print(f"my_dict, {my_dict}") # -> {'one': 1, 'two': 2, 'three': 3}



print("") # spacing in the console

# access dictionary elements
print(f'my_dict["one"]   {my_dict["one"]}') # -> 1
print(f'my_dict["two"]   {my_dict["two"]}') # -> 2
print(f'my_dict["three"] {my_dict["three"]}') # -> 3



print("") # spacing in the console

# access dictionary elements
print(f'my_dict.get("one")   {my_dict.get("one", None)}') # -> 1
print(f'my_dict.get("two")   {my_dict.get("two", None)}') # -> 2
print(f'my_dict.get("three") {my_dict.get("three", None)}') # -> 3
print(f'my_dict.get("four")  {my_dict.get("four", None)}') # -> None



print("") # spacing in the console

# check if exist
print(f"'one'   in my_dict -> {'one'   in my_dict}") # True
print(f"'two'   in my_dict -> {'two'   in my_dict}") # True
print(f"'three' in my_dict -> {'three' in my_dict}") # True
print(f"'four'  in my_dict -> {'four'  in my_dict}") # False



print("") # spacing in the console

del my_dict["two"] # -> remove the key-value pair -> 'two': 2

print(my_dict) # -> {'one': 1, 'three': 3}






print("") # spacing in the console

# pop the dict entry -> it exist
result = my_dict.pop("three", "not found")
print(my_dict) # -> {'one': 1}
print(f"result -> {result}") # -> 3
print(f"type(result) -> {type(result)}") # -> int

print("") # spacing in the console

# pop the dict entry -> it does not exist and default to None
result = my_dict.pop("three", None)
print(my_dict) # -> {'one': 1}
print(f"result -> {result}") # -> None
print(f"type(result) -> {type(result)}") # -> NoneType

print("") # spacing in the console

# pop the dict entry -> it does not exist and default to the string "not found"
result = my_dict.pop("three", "not found")
print(my_dict) # -> {'one': 1}
print(f"result -> {result}") # -> not found
print(f"type(result) -> {type(result)}") # -> str








print("") # spacing in the console

my_dict.clear()

print(my_dict) # -> {}




