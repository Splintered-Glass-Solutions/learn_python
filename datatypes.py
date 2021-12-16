
# == Imports ==
# * lets skip these for now
# import print_cat_facts as pcf
# import traceback2 as traceback
# import pandas as pd
from datetime import datetime as dt
# ======== PYTHON 101 ==========
# %% #_ region[grey]
# ==== Comments ====
# * staring a line with a # make it a comment in python.
# # Meaning this line will not be ran
var1 = 2 + 2
# ==== Cell Execiton (shift+enter) ====
# %% #* the '#%%' is a special command in VS Code.
#           It allows us to run code in chunks

# we can do this by hitting shift+enter
print("Just testing things")

# * That should have opened an "Interactive" window.
# If it didnt then check your vs code settings > key shortcuts.
#   The main command you want shift+enter mapped to is:
#       Jupyter: Run Selection/line in Interactive Window

# %% #* Enough set up, lets write some code
# * lets make our first variable named "my_first_var"
my_first_var = 2 + 2
my_first_var  # then print it
# %%
# * we can reference our fist variable in making a new variable
my_first_var = my_first_var + 4
print(my_first_var)
# _ endregion

# %% #==== DataTypes ====
# %% #_ region[purple]
# * well wasnt that fun, but now for some more boring stuff... sorry
# Let talk about datatypes...

# %%#= integers
some_int = 50
# "type" is a built in python function that tells us what datatype an object it. Very helpful
type(some_int)

# %%#= floats
number = 1.5
print(number)
type(number)

# %%#*  converting ints to floats
some_int = float(some_int)

# %%#* rounding floats to ints
print(round(1.3))
type(round(1.7))

# %%#* converting numbers to strings
num = str(1.2)
# looks the same but its a string, basically a series of characters
print("my favorite number is: " + num)
type(num)
# %% # soo if we ran this we get an error
num + 2

# %%#= strings
some_text = 'aberlknsdlkjasdfg,m234587hajkn24j'
print(some_text)

# %%
# * we can get just a certain "slice" of the string by indicating which charaters we want in []
print(some_text[5])
print(some_text[0:10])  # note the first charcter is the 0 index
print(some_text[0])
print(some_text[0] + "bc")  # and we can cobine strings with '+'

# %% #= lists
# * a list is just just a comma seperated collection of objects
a_list = [1, 2.4, '5.7', True, None, ['a', 'b', 'c'], {"key": 'vlue'}]
print(a_list)

# %% #* lists can contain other lists
print(a_list[-3:])
print(a_list[:3])
len(a_list)  # len is another helpful function that shows us how many objects are in a list

# %%
len('abcd')  # also works on strings, fyi

# %%#==== dictionaries ====

person = {"FirstName": "Preston",
          "LastName": "Pope",
          "Location": "Texas",
          "Age": 29,
          "Hobbies": ["Soccer", "Coding", "Outdoors"]
          }

person['FullName'] = person['FirstName'] + " " + person['LastName']

# %% #* iterate over each item in a dictionary
for k, v in person.items():
    print(v)

# %% #* get all the keys from a dictionary
for k in person.keys():
    print(k)

# %% #* get all the keys from a dictionary
person_values = person.values()
person_values = list(person_values)

# %%#= dates
# * here we gave the datetime module a nickname 'dt' so we dont have to type it everytime we use it
# generally you import at the top of the file.. but oh well

day = dt.now()  # * now this is called a dot function.
# previously we use a function like 'len()' by placing a the objects or paramters into the ().
# with a dot fucntion, we place just put the function after the object, seperated by a '.'
# like this. Here we have a datetime object called 'day' and use a dot function called 'weekday' on it
type(day)
# %%
dayofweek = day.weekday()
print(dayofweek)
print(type(dayofweek))  # since were here anyways
print(day)
print(type(day))  # since were here anyways

# %%#* this is an example of conditional statements. they run certain lines of code based on a given criterian
if dayofweek == 1:
    its_tuesday = True
    its_monday = False
elif dayofweek == 0:
    it_tuesday = False
    its_monday = True
else:
    its_tuesday = False
    its_monday = False

print((its_tuesday))   # this is a boolean, its either True or False
type(its_monday)

# %%#* that if else is ugly and error prone.  This is a great use case for a 'match' statement
#! however this is only avaliable python version 3.10.. I am currently running 3.7
# match dayofweek:
#     case 0:
#         its_monday = True
#     case 1:
#         its_tuesday = True
#     case 2:
#         its_wednesday = True
#     ...
#     case _:
#         print('no day found)

# %%#* truthy and falsey
if 0:
    print('lets go get pizza')
else:
    print('yuck just a salad...')
# %% #= booleans
print(1 == 1)  # the double equal sign is essentially asking "is this equal to this?"
print(True == (1 == 3))
print(dayofweek)

var1 = 0
if var1:
    print(var1)
else:
    # google python "falsish and trueish values"
    print('wait why did it print this?')

# %%
a_list = [0, 1, -1, None, False, True, "random",
          "", [1, 2], [], {'test': 'value'}, {}]
for i in a_list:
    print(i)
    # chekc if item is truthy or falsey
    if i:
        print('this is truthy')
    else:
        # google python "falsish and trueish values"
        print('this is falsey')

# %% #= dictionaries
# * a collection of key value pairs
my_dictionary = {'key': 'value', 'another': 1, 'and_another': ['a', 'list']}
dir(my_dictionary)
# %%
my_dictionary['another']

# %%
# _ endregion
