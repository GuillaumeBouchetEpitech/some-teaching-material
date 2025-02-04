


#
#
#
#  PART 3
#
#
#

print("")
print("")
print("#" * 30)
print("# PART 3")
print("#")
print("")
print("")



# enumerate

my_list = ['one', 'two', 'three', 'four', 'five']

print(f"my_list -> {my_list}")

for index, value in enumerate(my_list):
    print(f"the value at index {index} is '{value}'")






# extend

my_list_A = ['one', 'two', 'three']
my_list_B = ['four', 'five']

print("") # spacing in the console

print(f"my_list_A -> {my_list_A}") # ['one', 'two', 'three']
print(f"my_list_B -> {my_list_B}") # ['four', 'five']


my_list_A.extend(my_list_B)

print("") # spacing in the console

print(f"my_list_A -> {my_list_A}") # ['one', 'two', 'three', 'four', 'five']
print(f"my_list_B -> {my_list_B}") # ['four', 'five']





# copy

my_list_A = ['one', 'two', 'three']
my_list_B = my_list_A.copy()

print("") # spacing in the console

print(f"my_list_A -> {my_list_A}") # ['one', 'two', 'three']
print(f"my_list_B -> {my_list_B}") # ['one', 'two', 'three']

# are 'my_list' and 'my_second_list' referencing the same list?
if my_list_A is my_list_B:
    print('both variables are referencing the same list') # not printed
else:
    print('both variables are NOT referencing the same list') # printed






# slice

my_list = ['one', 'two', 'three', 'four', 'five']

print("") # spacing in the console

print(f"my_list       -> {my_list}") # ['one', 'two', 'three', 'four', 'five']
print(f"my_list[3:]   -> {my_list[3:]}") # ['four', 'five']
print(f"my_list[2:4]  -> {my_list[2:4]}") # ['three', 'four']
print(f"my_list[:3]   -> {my_list[:3]}") # ['one', 'two', 'three']
print(f"my_list[0::2] -> {my_list[0::2]}") # ['one', 'three', 'five']

my_list[2:3] = [] # remove 'three'

print(f"my_list   -> {my_list}") # ['one', 'two', 'four', 'five']

my_list[2:2] = ['THREEEEE'] # add 'three'

print(f"my_list   -> {my_list}") # ['one', 'two', 'THREEEEE', 'four', 'five']

my_list[3:4] = ['FOUUUUR'] # replace 'four'

print(f"my_list   -> {my_list}") # ['one', 'two', 'THREEEEE', 'FOUUUUR', 'five']

my_list[-1:] = ['FIIIIVE'] # replace last

print(f"my_list   -> {my_list}") # ['one', 'two', 'THREEEEE', 'FOUUUUR', 'FIIIIVE']

my_list[0:1] = ['OOOOONE'] # replace first

print(f"my_list   -> {my_list}") # ['OOOOONE', 'two', 'THREEEEE', 'FOUUUUR', 'FIIIIVE']

del my_list[1:4] # -> remove slice

print(f"my_list   -> {my_list}") # ['OOOOONE', 'FIIIIVE']







# reversed looping

print("") # spacing in the console

print("reversed loop")

my_list = ['one', 'two', 'three', 'four', 'five']

print(f"my_list -> {my_list}") # ['one', 'two', 'three', 'four', 'five']

for index in range((len(my_list) - 1), -1, -1): # asking a descending range
    print(f" ---> {my_list[index]}")





# reversed function

print("") # spacing in the console

print("reversed loop")

my_list = ['one', 'two', 'three', 'four', 'five']

print(f"my_list          -> {my_list}") # ['one', 'two', 'three', 'four', 'five']

my_reversed_list = [x for x in reversed(my_list)] # copy

print(f"my_reversed_list -> {my_reversed_list}") # ['one', 'two', 'three', 'four', 'five']





# join

print("") # spacing in the console

print(f' -> (" __ ".join(["11", "22", "33", "44", "55"])) -> {" __ ".join(["11", "22", "33", "44", "55"])}')






print("") # spacing in the console




