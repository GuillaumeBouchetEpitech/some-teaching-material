
#
#
# Built-in type: list
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


my_list = [] # -> empty
print(my_list) # -> []



my_list.append(1) # append one element
my_list.append(2) # append one element
my_list.append(3) # append one element
print(my_list) # -> [1,2,3]
print(my_list[0]) # -> 1
print(my_list[1]) # -> 2
print(my_list[2]) # -> 3



del my_list[1] # -> remove second item -> remove item of value 2

print(my_list) # -> [1,3]



my_list[0] = 9 # -> replace value 1 by 9 -> replace first element of the list by 9

print(my_list) # -> [9,3]



my_list.sort() # -> sort the list in an ascending order

print(my_list) # -> [3,9]



my_list.sort(reverse=True) # -> sort the list in an descending order

print(my_list) # -> [9,3]


my_list.clear()
print(my_list) # -> []






