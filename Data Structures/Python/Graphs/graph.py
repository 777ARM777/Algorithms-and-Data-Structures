# Python program to find bridges in a given undirected graph
# Complexity : O(V+E)

from collections import defaultdict
import visualize_graph as vg


# This class represents an undirected graph using adjacency list representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.Time = 0
        self.count = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BCCUtil(self, u, parent, low, disc, st, graph_vis):

        # Count of children in current node
        children = 0

        # Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        # Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:
            # If v is not visited yet, then make it a child of u
            # in DFS tree and recur for it
            if disc[v] == -1:
                parent[v] = u
                children += 1
                st.append((u, v))  # store the edge in stack
                self.BCCUtil(v, parent, low, disc, st, graph_vis)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                # Case 1 -- per Strongly Connected Components Article
                low[u] = min(low[u], low[v])

                # If u is an articulation point, pop
                # all edges from stack till (u, v)
                if parent[u] == -1 and children > 1 or parent[u] != -1 and low[v] >= disc[u]:
                    self.count += 1  # increment count
                    w = -1
                    while w != (u, v):
                        w = st.pop()
                        graph_vis.addEdge(*w)
                        # print(w, end=" ")
                    # print()

            elif v != parent[u] and low[u] > disc[v]:
                '''Update low value of 'u' only of 'v' is still in stack
                (i.e. it's a back edge, not cross edge).
                Case 2 
                -- per Strongly Connected Components Article'''

                low[u] = min(low[u], disc[v])

                st.append((u, v))

    # The function to do DFS traversal.
    # It uses recursive BCCUtil()
    def BCC(self, graph_vis):

        # Initialize disc and low, and parent arrays
        disc = [-1] * self.V
        low = [-1] * self.V
        parent = [-1] * self.V
        st = []

        # Call the recursive helper function to
        # find articulation points
        # in DFS tree rooted with vertex 'i'
        for i in range(self.V):
            if disc[i] == -1:
                self.BCCUtil(i, parent, low, disc, st, graph_vis)

            # If stack is not empty, pop all edges from stack
            if st:
                self.count = self.count + 1

                while st:
                    w = st.pop()
                    graph_vis.addEdge(*w)
                    # print(w, end=" ")
                # print()

    '''A recursive function that finds and prints bridges
    using DFS traversal
    u --> The vertex to be visited next
    visited[] --> keeps track of visited vertices
    disc[] --> Stores discovery times of visited vertices
    parent[] --> Stores parent vertices in DFS tree'''

    def bridgeUtil(self, u, visited, parent, low, disc, graph_vis):

        # Mark the current node as visited and print it
        visited[u] = True

        # Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        # Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:
            # If v is not visited yet, then make it a child of u
            # in DFS tree and recur for it
            if not visited[v]:
                parent[v] = u
                self.bridgeUtil(v, visited, parent, low, disc, graph_vis)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                low[u] = min(low[u], low[v])

                ''' If the lowest vertex reachable from subtree
                under v is below u in DFS tree, then u-v is
                a bridge'''
                if low[v] > disc[u]:
                    graph_vis.addEdge(u, v)

            elif v != parent[u]:  # Update low value of u for parent function calls.
                low[u] = min(low[u], disc[v])

    # DFS based function to find all bridges. It uses recursive
    # function bridgeUtil()
    def bridge(self, graph_vis):

        # Mark all the vertices as not visited and Initialize parent and visited,
        # and ap(articulation point) arrays
        visited = [False] * self.V
        disc = [float("Inf")] * self.V
        low = [float("Inf")] * self.V
        parent = [-1] * self.V

        # Call the recursive helper function to find bridges
        # in DFS tree rooted with vertex 'i'
        for i in range(self.V):
            if not visited[i]:
                self.bridgeUtil(i, visited, parent, low, disc, graph_vis)

    def dfs(self, V, vis, i, curr):
        vis[curr] = 1
        for x in self.graph[curr]:
            if x != i and not vis[x]:
                self.dfs(V, vis, i, x)

    # Function to find Articulation Points in the graph
    def AP(self, V):
        initial_components = len(self.connectedComponents())
        nodes = []

        for i in range(1, V):

            # To keep track of number of components of graph
            components = 0

            # To keep track of visited vertices
            vis = [0] * V

            # Iterating over the graph after removing vertex i
            # and its associated edges
            for j in range(1, V):
                if j != i:

                    # If the jth vertex is not visited, it will
                    # form a new component.
                    if not vis[j]:
                        # Increasing the number of components.
                        components += 1

                        # dfs call for the jth vertex
                        self.dfs(V, vis, i, j)

            # If number of components is more than 1 after
            # removing the ith vertex then vertex i is an
            # articulation point.
            if components > initial_components:
                nodes.append(i)

        return nodes

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if not visited[v]:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc

    def DFSUtil(self, temp, v, visited):

        # Mark the current vertex as visited
        visited[v] = True

        # Store the vertex to list
        temp.append(v)

        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.graph[v]:
            if not visited[i]:
                # Update the list
                temp = self.DFSUtil(temp, i, visited)
        return temp


if __name__ == "__main__":
    number_of_nodes = 13
    g = Graph(number_of_nodes)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.addEdge(1, 5)
    g.addEdge(0, 6)
    g.addEdge(5, 6)
    g.addEdge(5, 7)
    g.addEdge(5, 8)
    g.addEdge(7, 8)
    g.addEdge(8, 9)
    g.addEdge(10, 11)
    g.addEdge(10, 12)

    G = vg.GraphVisualization()
    for i in range(1, number_of_nodes + 1):
        G.addNode(g, i)
    G.visualize('Graph visualization')

    cc = g.connectedComponents()
    print("Following are connected components number")
    print(len(cc))
    print("Following are connected components")
    print(*cc)

    nodes = g.AP(number_of_nodes)
    print('Articular points are: ', *nodes)

    G = vg.GraphVisualization()
    for u in nodes:
        has_connection = False
        for v in g.graph[u]:
            if v in nodes:
                has_connection = True
                G.addEdge(u, v)
                print(u, v)
        if not has_connection:
            G.addIsolatedNode(u)

    G.visualize('Articulation Points in graph')

    # G = vg.GraphVisualization()
    # g.BCC(G)
    # G.visualize('Biconnected components in graph')
    # print(f"Above are {g.count} biconnected components in graph")

    G = vg.GraphVisualization()
    g.bridge(G)
    G.visualize('Bridges in graph')
