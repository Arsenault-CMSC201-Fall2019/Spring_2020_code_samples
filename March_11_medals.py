def read_data(data_file):
    with open(data_file,"r") as infile:
        contents = infile.read()
        return(contents)

def break_up_data (instring):
    list_of_strings = instring.split('\n')
    header = list_of_strings[0]
    print(len(list_of_strings))
    for i in range(1,len(list_of_strings)-1):
        country = list_of_strings[i]
        result = country.split()
        total_medals = int(result[2]) + int(result[3])+ int(result[4])
        print("total medals ", total_medals)
    return list_of_strings

def write_text_file(data_to_print, file_to_print):
    with open (file_to_print, "w") as textfile:
        #print out the text files

def write_csv_file(data_to_print, file_to_print):
    with open (file_to_print, "w") as csvfile:
        # print

if __name__ == "__main__":
    
# read in data
    data_string = read_data("medals.txt")
#break data into components
    l_o_s = break_up_data(data_string)
