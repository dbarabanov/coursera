#In this programming problem you'll code up Prim's minimum spanning tree algorithm. Download the text file here. This file describes an undirected graph with integer edge costs. It has the format
#[number_of_nodes] [number_of_edges]
#[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
#[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
#...
#For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and vertex #3 that has cost -8874. You should NOT assume that edge costs are positive, nor should you assume that they are distinct.
#
#Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below.
#
#IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing a heap-based version. The simpler approach, which should already give you a healthy speed-up, is to maintain relevant edges in a heap (with keys = edge costs). The superior approach stores the unprocessed vertices in the heap, as described in lecture. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.

edges = [map(int, x.split(' ')) for x in open('edges.txt', 'r').read().split('\n')[1:-1]]
vertices = set()
for edge in edges:
    vertices.add(edge[0])
    vertices.add(edge[1])
spanned = set()
spanned.add(vertices.pop())

total_cost = 0
while len(vertices)>0:
    best_cost = 9999999
    for edge in edges:
        if edge[0] in spanned and edge[1] in vertices and edge[2]<best_cost:
            best_cost = edge[2]
            best_vert = edge[1]
        if edge[1] in spanned and edge[0] in vertices and edge[2]<best_cost:
            best_cost = edge[2]
            best_vert = edge[0]
    spanned.add(best_vert)
    vertices.remove(best_vert)
    total_cost+=best_cost

#    print vertices
#    print best_cost
#    print best_vert
#    print spanned
#    print total_cost
print total_cost
