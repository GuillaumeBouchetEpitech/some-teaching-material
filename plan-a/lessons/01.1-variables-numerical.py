




print("") # space in the console



print("add/subtract")
print(f"3 + 2 = {3 + 2}") # add -> 5
print(f"3 - 2 = {3 - 2}") # subtract -> 1

print("multiply/power")
print(f"3 * 2 = {3 * 2}") # multiply -> 6
print(f"2 ** 4 = {2 ** 4}") # power -> 16

print("divide/whole-divide")
print(f"3 / 2 = {3 / 2}") # divide (decimal) -> 1.5
print(f"3 // 2 = {3 // 2}") # divide (whole) -> 1

print("modulo")
print(f"5 % 2 = {5 % 2}") # modulo -> 1
print(f"10 % 4 = {10 % 4}") # modulo -> 2
print(f"10 % 7 = {10 % 7}") # modulo -> 3
print(f"10 % 6 = {10 % 6}") # modulo -> 4


print("") # space in the console


my_number = 666 # -> 666
my_number_from_string = int("666") # -> 666


# is a number, whole and decimal
print(f"666 -> {666}") # -> 666 -> type: int
print(f"type(666) -> {type(666)}") # -> 666 -> type: int

print("") # space in the console

print(f"99.999 -> {99.999}") # -> 99.999 -> type: float
print(f"type(99.999) -> {type(99.999)}") # -> 99.999 -> type: float

print("") # space in the console

# not a number
print("666") # -> 666 -> type: str
print("99.999") # -> 99.999 -> type: str

print("") # space in the console

# this is "parsed text" into numbers, whole and decimal
print(int("666")) # -> 666 -> type: int
print(float("99.999")) # -> 99.999 -> type: float




# set to 1
my_var = 1

# add 2 (will total to 3)
my_var = my_var + 2

# again, add 2 (will total to 5)
my_var += 2 # popular syntax

print(f'my_var {my_var} (after add)') # 5




# subtract 1 (will total to 4)
my_var = my_var - 1

# again, subtract 1 (will total to 3)
my_var -= 1 # popular syntax

print(f'my_var {my_var} (after subtract)') # 3




# multiply by 3 (will total to 9)
my_var = my_var * 3

# multiply by 2 (will total to 18)
my_var = my_var * 2 # popular syntax

print(f'my_var {my_var} (after multiply)') # 18




# divide by 3 (will total to 6.0)
my_var = my_var / 3

# divide by 2 (will total to 3.0)
my_var /= 2 # popular syntax

print(f'my_var {my_var} (after divide)') # 3




# power by 2 (will total to 9.0)
my_var = my_var ** 2

# power by 2 (will total to 81.0)
my_var **= 2

print(f'my_var {my_var} (after power)') # 81.0



# modulo by 6 (will total to 3.0)
my_var = my_var % 6

# divide by 2 (will total to 1.0)
my_var %= 2

print(f'my_var {my_var} (after modulo)') # 1.0









