# In-class coding from Wedeesay, April 1

# Dictionaries

dogs = {"doug":["beagle","bulldog"], "lizzie":"Australian cattle dog", "penny":"spaniel","bonnie":"beagle", "remy":"shepherd"}

# Add an element using an assignment

dogs['cinder'] = 'doberman'

# Accessing an element by key
print(dogs['doug'])
print(dogs['cinder'])

#Accessing a key that doesn't exist
print(dogs['pepper'])

# Accessing an element by key using the 'get' method

print(dogs.get('doug'))

# If you use 'get' and the key doesn't exist

print(dogs.get('pepper'))

# Using get to return a value other than None

print(dogs.get('pepper','Key not found'))
print(dogs.get('pepper', -1))


# Remove an element using 'del'
del dogs['cinder']

# An error - deleting a key that isn't in the dictionary

del dogs['lady']

# Removing an element using pop

# Still causes an error

dogs.pop('lady')

# Defining a value to return if the key doesn't exist

print(dogs.pop('lady','Error - key not found'))
print(dogs.pop('lady', -1))


# Now a dictionary to hold the elements of a recipe

recipe = {'butter':2, 'flour':1.5,'salt':1,'Soda':1, 'Granulated sugar':0.25, 'brown sugar':1, 'egg':2,
          'milk':2, 'vanilla':1.5,'Chocolate chips':12}


eggs = int(input("How many eggs do you have?"))
if eggs < recipe["egg"]:
	print("Add eggs to your grocery list")
chips = int(input("How many ounces of chocolate chips do you have?"))
if chips < recipe["Chocolate chips"]:
	print("Get a bag of chocolate chips at the store")



a = [1,2,3]
b = [4,5,6]
d = dict(zip(a,b))
print(d)
