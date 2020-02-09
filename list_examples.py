#First, create an empty list

grocery_list = []

#Then add the items to the list one by one
grocery_list.append("Milk")
grocery_list.append("eggs")
grocery_list.append("cereal")
grocery_list.append("coffee")
grocery_list.append("apples")
grocery_list.append("strawberries")
grocery_list.append("broccoli")
grocery_list.append("cucumber")
grocery_list.append("tomatoes")
grocery_list.append("green onions")

# Yes, you had to append the items one at a time
# if you try to append multiple items in a statement
# it's an error
# grocery_list.append("cucumber", "tomatoes", "green onions")
# results in an error

#now check to see what our list looks like
print (grocery_list)

# okay, I got the eggs. Let's remove it from the list
grocery_list.remove("eggs")

# What happens if I get the spelling or capitalization wrong?
grocery_list.remove("Eggs")

# Now, check to see what's left on the list after
# I remove what I bought
print(grocery_list)

# Let's just remove the first item on the list.  That uses "pop"
grocery_list.pop(0)

print(grocery_list)

# Oops, I removed Milk from my list but I didn't buy Milk yet.
# Let's put it back. "append" puts it at the end; can we
# put "Milk" back where it was?

grocery_list.insert(0, "Milk")

# My wife texts me to make sure to get bagels.
# First I need to see whether that's already
# part of my list. If it's not, append it

if not("bagels" in grocery_list):
	grocery_list.append("bagels")

# I have to be careful to spell that right
# Maybe "Bagels" is in my list; or maybe "bagles"





# here's an example where we create a list all at once

ordinals = ["first", "second", "third", "fourth", "fifth"]

# Now another example where we'll get the data from the user

names = []


str = "please input the first name:"
name = input(str)
names.append(name)

str = "please input the second name:"
name = input(str)
names.append(name)
print(names)

str = "please input the third name:"
name = input(str)
names.append(name)
print(names)

str = "please input the fourth name:"
name = input(str)
names.append(name)
print(names)

str = "please input the fifth name:"
name = input(str)
names.append(name)
print(names)


test_name = input("Enter another name")

if test_name in names:
	print("Success")
else:
	print("No fair I've never seen that name")