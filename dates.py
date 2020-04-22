def convert_date(s):
    '''
This function takes a string representing a day
of a year. The date format is mmddyyyy.
The function returns the julian date; that is
the ordinal number of the day in the year.
'''
#First convert the string into three integers representing
# the day, month and year
    month = int(s[:2])
    day = int(s[2:4])
    year = int(s[4:])

#Now convert:
    j_day = (month -1) * 30 + day
    if month == 2 or month == 4:
        j_day += 1
    elif month == 6 or month == 7:
        j_day += 2
    elif month == 8:
        j_day += 3
    elif month == 9 or month == 10:
        j_day += 4
    elif month == 11 or month == 12:
        j_day += 5
    else:
        j_day += 0

    return j_day

if __name__ == "__main__":
    print(convert_date('07042020'))
