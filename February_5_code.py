######################
#
# This is one way to write a block
# of comments
#
########################

"""
This is another way to write a block
of comments
"""
'''
This will work too

'''


verb = input("please enter a verb")
new_verb = verb + "ing"
print(new_verb)

principal = 10000
rate = 0.03/12
n_payments = 72
cost = (principal * rate * (1 + rate)**n_payments)/((1 + rate)**n_payments -1)

print(cost)

