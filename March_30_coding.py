#code for lecture on Monday, March 30

# This works the way you expect
a = 1
b = a
b += 1
print(a)

# This might be surprising
c = [1, 2, 3, 4]
d = c
d.append(5)
print(c)


# This will fail - why?
state = 'Maryland'
state[0] = 'G'


def strange_stuff (a_list):
   a_list.append(5)
   return

# This function doesn't return any value
# that's usable by the main program. So
# what will happen?

# a calling program
if __name__ == "__main__":
    main_list = [1, 2, 3, 4]
    strange_stuff(main_list)
    print(main_list)


a = [
    [1,2,3],
    [4,5,6],
    [7,8.9]
]
b = list(a)
b[1].append(10)
