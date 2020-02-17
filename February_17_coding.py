# Examples of code using while loops
# from Monday, Feb. 17

age = 0;
while (age < 18):
	age = input("enter your age in years: ")
	print ("If you’re 18 or older you should vote")
print ("that's the end of our story")


# compute 10! Using a while loop
product = 1
factor = 1
while factor <= 10:
	product *= factor   #or product = product * factor
	factor += 1
print("our answer is ", product)

num = 1
while num % 2 == 0:
	print(num)
	num += 2

age = int(input("please enter your age in years: "))
while (age < 0) or (age > 100):
	print("Age must be between 0 and 100 inclusive ")
	age = int(input("please enter your age in years: ")

grade = ""
name  = ""
while name != "Hrabowski":
    # get the user's grade
    grade = input("What is your grade? ")
print("You passed!")

cookiesLeft = 50

while cookiesLeft > 0:
    # eat a cookie
    cookiesLeft = cookiesLeft + 1

#print all the positive odd numbers 
#less than 100

num = 1
while num != 100:
    print(num)
    num = num + 2

