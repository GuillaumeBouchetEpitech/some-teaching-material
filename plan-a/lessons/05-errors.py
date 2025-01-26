





# raise ValueError("Hello?") # <- will stop the script







# try-block
try:

    print('start')

    raise ValueError("Hello?")

    print('stop') # <- will not be reached

# catch all errors
except:

    print('an error was catched')

    # raise err # <- can decide to raise it again

    pass # can decide to quietly ignore it








# try-block
try:

    print('start')

    raise ValueError("Hello?") # <- this would crash the program if not in the try-block

    print('stop') # <- will not be reached

# catch only ValueError errors
except ValueError as err:

    print(f'an error was intercepted, err= "{err}"')





# try-block
try:

    print('start')

    raise NotImplementedError("Hello?") # <- this would crash the program if not in the try-block

    print('stop') # <- will not be reached

except ValueError as err: # catch only ValueError errors
    print(f'an ValueError error was intercepted, err= "{err}"') # <- not a ValueError will not be reached
except:
    print(f'an error was intercepted, we don\'t know its type') # will be printed










