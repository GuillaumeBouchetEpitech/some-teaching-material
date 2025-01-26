
#
#
# Built-in type: tuple
#
#




print("") # spacing in the console

my_tuple = 'one', 'two', 'three'

print(f"my_tuple    -> {my_tuple}") # ('one', 'two', 'three')
print(f"my_tuple[0] -> {my_tuple[0]}") # 'one'
print(f"my_tuple[1] -> {my_tuple[1]}") # 'two'
print(f"my_tuple[2] -> {my_tuple[2]}") # 'three'

my_tuple = ('one', 'two', 'three') # alt syntax

print(f"my_tuple    -> {my_tuple}") # ('one', 'two', 'three')



# unpacking

print("") # spacing in the console

my_tuple = 'one', 'two', 'three'

one, two, three = my_tuple

print(f"my_tuple -> {my_tuple}") # ('one', 'two', 'three')
print(f"one      -> {one}") # 'one'
print(f"two      -> {two}") # 'two'
print(f"three    -> {three}") # 'three'








# enumerate returns a tuple

print("") # spacing in the console

for (index, value) in enumerate(range(0, 3)):
    print(f" -> index: {index},   value: {value}")

for t in enumerate(range(0, 3)):
    print(f" -> t[0]: {t[0]},   t[1]: {t[1]}")










print("") # spacing in the console

