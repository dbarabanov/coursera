#Question 1
#In this programming problem and the next you'll code up the knapsack algorithm from lecture. Let's start with a warm-up. Download the text file here. This file describes a knapsack instance, and it has the following format:
#[knapsack_size][number_of_items]
#[value_1] [weight_1]
#[value_2] [weight_2]
#...
#For example, the third line of the file is "50074 659", indicating that the second item has value 50074 and size 659, respectively.
#You can assume that all numbers are positive. You should assume that item weights and the knapsack capacity are integers.
#
#In the box below, type in the value of the optimal solution.
#
#ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!

lines = [map(int, x.split(' ')) for x in open('knapsack1.txt', 'r').read().split('\n')[:-1]]

capacity = lines[0][0]
items = lines[1:]

subproblems = []
subproblems.append([0 for cap in range(capacity + 1)])

for i, item in enumerate(items):
    subproblem = []
    for cap in range(capacity + 1):
        subproblem.append(max(subproblems[i][cap], subproblems[i][cap - item[1]] + item[0] if cap - item[1] >= 0 else 0))
    subproblems.append(subproblem)

print subproblems[-1][-1]
#2493893
