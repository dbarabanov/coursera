#Question 2
#This problem also asks you to solve a knapsack instance, but a much bigger one.
#Download the text file here. This file describes a knapsack instance, and it has the following format:
#[knapsack_size][number_of_items]
#[value_1] [weight_1]
#[value_2] [weight_2]
#...
#For example, the third line of the file is "50074 834558", indicating that the second item has value 50074 and size 834558, respectively. As before, you should assume that item weights and the knapsack capacity are integers.
#
#This instance is so big that the straightforward iterative implemetation uses an infeasible amount of time and space. So you will have to be creative to compute an optimal solution. One idea is to go back to a recursive implementation, solving subproblems --- and, of course, caching the results to avoid redundant work --- only on an "as needed" basis. Also, be sure to think about appropriate data structures for storing and looking up solutions to subproblems.
#
#In the box below, type in the value of the optimal solution.
#
#ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!

lines = [map(int, x.split(' ')) for x in open('knapsack2.txt', 'r').read().split('\n')[:-1]]

capacity = lines[0][0]
items = lines[1:]

memo = [0 for cap in range(capacity + 1)]

for i, item in enumerate(items):
    print i
    subproblem = []
    for cap in range(capacity + 1):
        subproblem.append(max(memo[cap], memo[cap - item[1]] + item[0] if cap - item[1] >= 0 else 0))
    memo = subproblem

print memo[-1]
#2595819
