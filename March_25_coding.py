"""
Coding for March 25, 2020 lecture
Demonstrating list slicing and 2D lists

"""

"""
List slicing

"""

"""
 2D Arrays
"""

# CONSTANTS
RANK = 0
GOLD = 1
SILVER = 2
BRONZE = 3
TOTAL = 4

medal_table = [
   [1, 14, 11,4,29],
   [2,5,2,4,11],
   [3,3,5,4,12],
   [4,3,3,3,9],
   [5,2,5,1,8],
   [6,2,3,0,5],
   [7,2,0,4,6],
]
# to view an individual element
medal_table[0][0]

medal_table[len(medal_table)-1][0]

# to view a row
medal_table[0]

#You CAN'T use that same technique to view a column.
#You have to view a column one element at a time
for i in range(len(medal_table)):
    print(medal_table[i][3])

# adding a column
# to put the "country" in
countries =["United States", "Kenya", "Jamaica", "China", "Ethiopia", "Great Britain", "Germany"]
for i in range(len(medal_table)):
   medal_table[i].insert(1, countries[i])


for k in range(len(medal_table)):
   print(medal_table[k])

# Now we need to update the constant definitions
# so that our previous code will still work
RANK = 0
COUNTRY = 1
GOLDS = 2
SILVERS = 3
BRONZES = 4
TOTALS = 5

golds_won = 0
for i in range(len(medal_table)):
   golds_won += medal_table[i][GOLDS]
print(golds_won)


#write a routine that fills a 2D table with the
#successive squares - 1, 4, 9, 16, 25,...
ROWS = 5
COLUMNS = 10
square_table = []  #create the initial blank table
num_to_be_squared = 1
for i in range(ROWS):
   row = []
   for j in range(COLUMNS):
       row.append(num_to_be_squared**2)
       num_to_be_squared += 1
   square_table.append(row)
print(square_table)

for k in range(ROWS):
   print(square_table[k])
