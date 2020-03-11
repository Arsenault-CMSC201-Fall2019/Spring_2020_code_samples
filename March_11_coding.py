def calculate_root(num, root):

    # a function to calculate the nth root of a number
    if num >= 0:
        r = num**(1/root)
        return r
    else:
        print(" Roots of negative numbers are not defined")
        return -1
    print("this line of code will never be executed")
    
if __name__ == "__main__":
    x = calculate_root(-125,3)
    print(x)

# This an extension of the coding we did March 4. 
# Open three files. The one that we're going to read from, and two
# that we're going to write to. One will be a text file; the other
# will be a comma-separated value (CSV) file. For this example, these are
# different files

def write_text_file(medals):
    with open("r.txt","w") as outfile:
        outfile.write(medals)
    
def write_csv_file(medals):
    with open ("r.csv","w") as csvfile:
        csvfile.write(medals)
        
def adjust_headers(headers):
    # We're going to add a column called "Total", so add that to the
    # headers string. We first have to strip the newline character 
    # \n off the current header; then add the new column heading;
    # then put the newline back 
    headers = headers.rstrip()
    headers = headers + "       Total" + '\n'
    return headers

def add_totals_column(line_from_table):
    data = line_from_table.split()
    # data is a list. data[0] is the rank. data[1] is the country name
    # data[2] is a string representing the number of gold medals won.
    # data[3] is a string representing the number of silver medals won.
    # data[4] is a string representing the number of bronze medals won.

    # to get the total medals won, convert data[2], data[3] and data[4]
    # to integers and add them.
    total = int(data[2]) + int(data[3]) + int(data[4])
    data.append(str(total))
    return data

if __name__ == "__main__":    
    with open("/Users/alfredarsenault/PyCharmProjects/code_from_Jan_29/medals.txt","r") as medal_file:
    
#The first line is just the header row.  Read that in.
            headers = medal_file.readline()

# We're going to add a column called "Total", so add that to the
# headers string. We first have to strip the newline character 
# \n off the current header; then add the new column heading;
# then put the newline back 
#            headers = headers.rstrip()
#           headers = headers + "       Total" + '\n'
            headers = adjust_headers(headers)

# Next, read in the whole file at once, and create a list
# of lines.
            for i in range(9):
                country_result = medal_file.readline()
            
# country_result is a string. Split it into its component parts
                data = add_totals_column(country_result)

# now we have to create a single string with the original data
# and the total number of medals won

# the opposite of string.split() is string.join()
# split turns a string into a list. join turns a list into a
# single string
                text_string = '\\t'.join(data) + '\n'
                write_text_file(text_string)
                
                csv_string = ','.join(data) + '\n'
                write_csv_file(csv_string)
                
                
                
def open_files(infile):
    with open(infile,"r") as f:
        return(f)
    
    
def factorial(num):
    product = 1
    for i in range(num):
        product *= i
        print(product)
    return product