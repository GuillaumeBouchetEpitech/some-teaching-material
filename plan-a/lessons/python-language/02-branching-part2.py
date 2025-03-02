
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
#
# complex statement
#
#

#
# new operator: and
#

my_age = 35

if my_age >= 0 and my_age < 18: # in the [0..18] range
    print("you are minor")
elif my_age >= 18 and my_age < 30: # in the [18..29] range
    print("you are a young adult")
elif my_age >= 30 and my_age < 59: # in the [30..59] range
    print("you are a mature adult")
else: # in the [60..inf] range
    print("you are a senior")


#
# new operator: or
#

my_music_volume = 25

if my_music_volume < 0 or my_music_volume > 100: # NOT in the [0..100] range
    print("that music volume is invalid -> it should be between 0 and 100 (inclusive)")



#
# mix of both
#

how_much_I_like_my_job = 75 # from 0 to 100
how_much_I_like_my_partner = 999 # from 0 to 100

if how_much_I_like_my_job > 50 and how_much_I_like_my_partner > 50:
    print("you are veeeeeery lucky")
elif how_much_I_like_my_job > 50 or how_much_I_like_my_partner > 50:
    print("you are lucky")
else:
    print("you need to make your luck, work hard!")




#
# new parenthesis operator: ( )
#

if True and (True or False):
    print('if') # always print
else:
    print('else') # never print


if False and (True or False):
    print('if') # never print
else:
    print('else') # always print


if True and (False or False):
    print('if') # never print
else:
    print('else') # always print



# concrete example

user_age = 19
user_sex = 'M' # 'M' or 'F'


if user_age >= 18 and (user_sex == 'M' or user_sex == 'F'):
    print('we will show adverts about coffee and tea')
elif user_age < 18 and user_sex == 'M':
    print('we will show adverts about chocolate drinks with boys toys')
elif user_age < 18 and user_sex == 'F':
    print('we will show adverts about chocolate drinks with girls toys')
else:
    print('we will show adverts that are safe for all ages')

