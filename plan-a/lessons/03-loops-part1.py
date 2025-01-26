
#
#
# loops
#
#




###
###
###
### for loop
###
###
###


print() # space in the console
print('for-loop-start 1')
for index in range(0,5):
    print(f" -> index: {index}")

#
# new keyword: continue
#

print() # space in the console
print('for-loop-start 2')
for index in range(0,5):

    # is it an odd number?
    if (index % 2) != 0: # modulo of 2 -> eihter 0 or 1

        print(f" ---> skipping -> is an odd number")

        continue # yes, index is an odd number -> skip

    print(f" -> index: {index}")

#
# new keyword: break
#

print() # space in the console
print('for-loop-start 3')
for index in range(0,5):

    if index > 2:
        print(f" ---> break")
        break # stop the loop

    print(f" -> index: {index}")


#
# new keyword: break and else
#

print() # space in the console
print('for-loop-start 4')
for index in range(0,5):
    print(f" -> index: {index}")
else:
    print(f" -> we did not use break in the loop") # is called

#

print() # space in the console
print('for-loop-start 5')
for index in range(0,5):

    if index > 2:
        print(f" ---> break, the 'else part' will not be called")
        break # stop the loop

    print(f" -> index: {index}")
else:
    print(f" -> we did not use break in the loop") # is not called








