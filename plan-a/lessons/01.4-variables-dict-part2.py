

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



my_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
}



print("") # spacing in the console

all_values = [x for x in my_dict.values()] # get a list of all values
print(f"all_values {all_values}") # -> [1,2,3]

# loop
print("loop")
for my_value in my_dict.values():
    print(f" ---> {my_value}") # 1,2,3


print("") # spacing in the console

all_keys = [x for x in my_dict.keys()] # get a list of all keys
print(f"all_keys {all_keys}") # -> ['one','two','three']

# loop
print("loop")
for my_key in my_dict.keys():
    print(f" ---> {my_key}") # 'one','two','three'


print("") # spacing in the console

all_items = [x for x in my_dict.items()] # get a list of all items

print(f"all_items[0][0] {all_items[0][0]}") # -> 'one'
print(f"all_items[0][1] {all_items[0][1]}") # -> 1
print(f"all_items[1][0] {all_items[1][0]}") # -> 'two'
print(f"all_items[1][1] {all_items[1][1]}") # -> 2
print(f"all_items[2][0] {all_items[2][0]}") # -> 'three'
print(f"all_items[2][1] {all_items[2][1]}") # -> 3

print("") # spacing in the console

# loop
print("loop")
for my_item in my_dict.items():
    print(f" ---> key: {my_item[0]}, value: {my_item[1]}") # 'one': 1,'two': 2,'three': 3









