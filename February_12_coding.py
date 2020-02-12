# Coding for Wednesday February 12
# for the first example set up a grocery list

grocery_list = ["Milk", "Eggs", "Cereal", "Coffee", "Apples", "Strawberries", "Broccoli", "Cucumber", "Tomatoes", "Green Onions"]

# Now, a "for each" loop that goes through the list and prints
# out each item

for item in grocery_list:
    print(item)
#Notice that Python automatically made "item" a string!!!

# A comparison of for each and for i loops:

integer_list = [20,21,22,23,24,25,26,27,28,29,30,31,32]
for item in integer_list:
	item += 1
print(integer_list)

for i in range(len(integer_list)):
    integer_list[i] += 1
print(integer_list)

#what not to do:
for item in integer_list:
    integer_list[item] += 1
print(integer_list)
