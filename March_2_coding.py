with open("test_data.txt", "r") as f:
    test_data = f.read()

#okay, now we have a big honking string that is not
# useful to us. The first thing we need to do is split
# it into a list of words.  Remember, this list will
# consist of nothing but strings

    words = test_data.split()

    # that splits the string on white space.
    # now we need to further split this into four
    # separate lists:
    # - a list of last names
    # - a list of first names
    # - a list of section numbers
    # - a list of test scores

    # spoiler alert: there is going to be a way to do this as one
    # big, multi-dimensional list, but for now we're going to use
    # four separate lists

    # first create the empty lists
    last_names = []
    first_names = []
    sections = []
    grades = []

    # so here's how we split

    for i in range(0, len(words), 4):

        # we did this so we can handle a full student record at a time
        # copy the last name


        last_names.append(words[i])


        # copy the first name
        first_names.append(words[i+1])

        # copy the section number.
        # We're not going to do any math on it, so it doesn't
        # matter if we convert it to an integer or leave it as
        # a string. but we'll convert ib, because

        sections.append(int(words[i+2]))

        # copy the score. This will have to be converted to an integer
        grades.append(int(words[i+3]))

# now, compute the average in each section
    sec_41_total = 0
    sec_41_students = 0
    sec_42_total = 0
    sec_42_students = 0
    for i in range(len(grades)):
        if sections[i] == 41:
            sec_41_students += 1
            sec_41_total += grades[i]
        else:
            sec_42_students += 1
            sec_42_total += grades[i]

    sec_41_ave = sec_41_total/sec_41_students
    print('section 41 average grade is {:5.2f}'.format(sec_41_ave))
    sec_42_ave = sec_42_total/sec_42_students
    print('section 42 average grade is {:5.2f}'.format(sec_42_ave))

    # now we'll print a histogram of the whole class grandes
    # we're only interested in the number of A's, B's, and "others

    # define a list to count the number of each grade
    # initialize the list to all zeros:
    num_grades = [0,0,0]
    for i in range(len(grades)):
        if grades[i] > 67:
            num_grades[0] += 1
        elif grades[i] >= 60:
            num_grades[1] += 1
        else:
            num_grades[2] += 1

    # now print the histogram
    for i in range(len(num_grades)):
        print(i, end='')
        for j in range(num_grades[i]):
            print('*', end='')
        print('\n')


