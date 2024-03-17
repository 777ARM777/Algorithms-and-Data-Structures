# Python3 code to implement the approach
import visualize_graph as vg

# Function to find union of two graphs
def findUnion(G1, G2):
    # Stores an edge of the graph G1
    added = {}

    # Stores the union graph G1
    G = []

    # Iterate over the edges
    # of the graph G1
    for p in G1:
        a = p[0]
        b = p[1]
        c = p[2]

        # Insert the current
        # edges into graph G
        G.append([a, b, c])
        added[a] = [b, c]

    # Iterate over the edges
    # of the graph G1
    for p in G2:
        a = p[0]
        b = p[1]
        c = p[2]

        x = [b, c]
        y = [c, b]

        # If either edge x or
        # y is already added
        if added.get(a) == x or added.get(a) == y:
            continue

        # Otherwise
        G.append([a, b, c])

    # visualize graph
    Graph = vg.GraphVisualization()
    for p in G:
        Graph.addEdge(p[1], p[2])
    Graph.visualize('Union in graphs')



# Function to find intersection of two graphs
def findIntersection(G1, G2):
    # Stores an edge
    added = {}

    # Stores the graph of intersection
    G = []

    # Iterate over edges of graph G1
    for p in G1:
        a = p[0]
        b = p[1]
        c = p[2]

        added[a] = [b, c]

    # Iterate over edges of graph G2
    for p in G2:
        a = p[0]
        b = p[1]
        c = p[2]

        x = [b, c]
        y = [c, b]

        # If either edge x or
        # y is already added
        if added.get(a) == x or added.get(a) == y:
            G.append([a, b, c])

    # visualize graph
    Graph = vg.GraphVisualization()
    for p in G:
        Graph.addEdge(p[1], p[2])
    Graph.visualize('Intersection in graphs')


if __name__ == "__main__":
    G1 = [["e1", 1, 2], ["e2", 1, 3], ["e3", 3, 4], ["e4", 2, 4]]
    G2 = [["e4", 2, 4], ["e5", 2, 3], ["e6", 3, 5], ["e7", 4, 5]]

    findUnion(G1, G2)
    findIntersection(G1, G2)
