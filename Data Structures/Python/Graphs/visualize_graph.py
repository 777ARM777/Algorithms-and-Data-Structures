# First networkx library is imported
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt


# Defining a Class
class GraphVisualization:

    def __init__(self):
        # visual is a list which stores all
        # the set of edges that constitutes a
        # graph
        self.visual = []
        self.isolated_nodes = []

    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, u, v):
        self.visual.append([u, v])

    def addNode(self, G, u):
        for v in G.graph[u]:
            self.visual.append([u, v])

    def addIsolatedNode(self, u):
        self.isolated_nodes.append(u)

    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self, title):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        G.add_nodes_from(self.isolated_nodes)

        nx.draw_networkx(G, node_color='violet')
        plt.title(title, fontdict={'size':25, 'color':'Blue'})
        plt.show()

    # Driver code

if __name__ == "__main__":
    G = GraphVisualization()
    G.addEdge(0, 2)
    G.addEdge(1, 2)
    G.addEdge(1, 3)
    G.addEdge(5, 3)
    G.addEdge(3, 4)
    G.addEdge(1, 0)
    G.addEdge(6, 0)
    G.addEdge(8, 0)
    G.addEdge(4, 0)
    G.visualize('Graph visualization')
