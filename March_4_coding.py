# Open two files. The one that we're going to read from, and the
# one that we're going to write to. For this example, these are
# different files

with open("/Users/alfredarsenault/PyCharmProjects/code_from_Jan_29/medals.txt","r") as medal_file:
    with open("r.txt","w") as outfile:
#The first line is just the header row.  Read that in.
        headers = medal_file.readline()

# We're going to add a column called "Total", so add that to the
# headers string
        headers = headers + "       Total"

# Next, read in one line at a time. We know that there are
# 9 more rows to read
        for i in range(9):
            country_result = medal_file.readline()

# country_result is a string. Split it into its component parts
            data = country_result.split()
# data is a list. data[0] is the rank. data[1] is the country name
# data[2] is a string representing the number of gold medals won.
# data[3] is a string representing the number of silver medals won.
# data[4] is a string representing the number of bronze medals won.

# to get the total medals won, convert data[2], data[3] and data[4]
# to integers and add them.
            total = int(data[2]) + int(data[3]) + int(data[4])
            data.append(str(total))
# now we have to create a single string with the original data
# and the total number of medals won

# the opposite of string.split() is string.join()
# split turns a string into a list. join turns a list into a
# single string
            endstring = '\t'.join(data)
            endstring = endstring + '\n'
            outfile.write(endstring)