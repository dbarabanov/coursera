#Question 1
#In this programming problem and the next you'll code up the clustering algorithm from lecture for computing a max-spacing k-clustering. Download the text file here. This file describes a distance function (equivalently, a complete graph with edge costs). It has the following format:
#[number_of_nodes]
#[edge 1 node 1] [edge 1 node 2] [edge 1 cost]
#[edge 2 node 1] [edge 2 node 2] [edge 2 cost]
#...
#There is one edge (i,j) for each choice of 1 lte i lt j lte n, where n is the number of nodes. For example, the third line of the file is "1 3 5250", indicating that the distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250. You can assume that distances are positive, but you should NOT assume that they are distinct.
#
#Your task in this problem is to run the clustering algorithm from lecture on this data set, where the target number k of clusters is set to 4. What is the maximum spacing of a 4-clustering?
#
#ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!

edges = [map(int, x.split(' ')) for x in open('clustering1.txt', 'r').read().split('\n')[1:-1]]

edges.sort(key=lambda x: x[2])

vertices = {}
for edge in edges:
    vertices[edge[0]] = edge[0]
    vertices[edge[1]] = edge[1]

costs = {}
for v in vertices:
    costs[v] = 0

cluster_count = len(vertices)

for edge in edges:
    head1 = vertices[edge[0]]
    while vertices[head1] != head1:
        head1 = vertices[head1] 

    head2 = vertices[edge[1]]
    while vertices[head2] != head2:
        head2 = vertices[head2] 

    if head1 != head2:
        if cluster_count <= 4:
            spacing_distance = edge[2]
            break
        vertices[head2] = head1
        costs[head1] += (edge[2] + costs[head2])
        cluster_count -= 1

print spacing_distance
#106
