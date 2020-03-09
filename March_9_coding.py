def calculate_days (years, months, days):
	num_days = 365 * years + 30 * months + days
	if years > 4:
		num_days += 1
	return num_days

if __name__ == "__main__":
    yrs = 23
    mos = 3
    days = 22
    length_of_time = calculate_days(yrs, mos, days)
    print("That is ", length_of_time, " days")


def subtract(x, y):
	print(x,"-",y,"=",str(x-y))

if __name__ == "__main__":
    x = 3
    y = 4
    subtract(y, x)


def print_error_message ():
    print("Sorry, that is not a valid option")

def get_valid_input():
    x = int(input("Enter a number between 0 and 9 inclusive"))
    while x < 0 or x > 9:
        print_error_message();
        x = int(input("Enter a number between 0 and9 inclusive"))
    return(x)

if __name__ == "__main__":
    num = get_valid_input();
    for i in range(10):
        power = num**i
        print ("{:3} to the power of {:3} is {:5}".format(num, i, power))
