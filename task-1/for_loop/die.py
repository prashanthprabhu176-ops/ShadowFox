# Using a for loop, simulate rolling a sixsided die multiple times (at least 20 times). 
# Count and print the following statistics: 
# How many times you rolled a 6 
# How many times you rolled a 1 
# How many times you rolled two 6s in a row 

import random
rolls = 20
count_of_six = 0
count_of_one = 0
count_of_two_six = 0

prev_roll = None

for i in range(rolls):
    roll = random.randint(1,6)
    print(roll, end=" ")

    if roll == 6:
        count_of_six += 1

        # count 1s
    if roll == 1:
        count_of_one += 1

        # check two 6s in a row
    if prev_roll == 6 and roll == 6:
        count_of_two_six += 1
        prev_roll = roll  # update previous roll

print("\n")
print("Number of times rolled 6:", count_of_six)
print("Number of times rolled 1:", count_of_one)
print("Two 6s in a row:", count_of_two_six)

#Output : 
# 4 6 1 2 3 4 1 5 2 2 5 2 6 3 1 2 5 4 3 2 

# Number of times rolled 6: 2
# Number of times rolled 1: 3
# Two 6s in a row: 0