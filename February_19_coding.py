#coding for Wednesday, February 19


# Printing new lines, or not
print("this produces two lines", "\n", "of output")
print("this produces one line", end="")
print("of output")

# printing out an integer
print("{:d} is the answer to the question".format(42))

#printing the same value as a float
print("{:f} is the answer to the question".format(42))
#limiting the number of decimal places
print("{:6.2f} is the answer to the question".format(42))

if roll == 7 or roll == 11:
    print ("you win")
elif roll == 2 or roll == 3 or roll == 12:
    print("you lose")
else:
    print("roll again")


CRAPS_WINNING_VALUES = [7,11]
CRAPS_LOSING_VALUES = [2,3,12]

if roll in CRAPS_WINNING_VALUES:
    print("you win")
elif roll in [2,3,12]:
    print ("you lose")
else:
    print("roll again")


str = 'Hey diddle diddle the cat and the fiddle”'
str_list = str.split() #this will split on whitespace, and the whitespace will be deleted
str_list = str.split("e") #what does this do? What happened to the “e” ?
int_str = "3 1 4 5 6 7 8 9 10"
int_list = int_str.split()
actual_int_list = []
for num in int_list:
	actual_int_list.append(int(num))

print("now is the time", end="this is where we stop")
print("and now we start again")
