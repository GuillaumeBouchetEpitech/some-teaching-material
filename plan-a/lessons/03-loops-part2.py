

###
###
###
### while loop
###
###
###



print() # space in the console
print('while-start 1')

index = 0
while index < 5:
    print(f" -> index: {index}")

    index = index + 1



#
# with keyword: break
#

print() # space in the console
print('while-start 2')

index = 0
while index < 5:

    if index > 2:
        print(f" ---> break")
        break # stop the loop

    print(f" -> index: {index}")

    index += 1



print() # space in the console

