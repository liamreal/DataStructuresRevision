import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# TO UPDATE TCL NOT FOUND ERROR, go to ENVIRONMENT VARIABLES AND UPDATE PATH TO NEW ONE FOR:
#       TCL_LIBRARY
#       TK_LIBRARY
# NEVERMIND, but if you do have issues, NOTICE PATH OF THESE, PyCharms pointed to a slightly different
# place so i made a symbolic link

'''
Data Types:
    G = nx.Graph()  # undirected graph (edges go both ways)
    D = nx.DiGraph() # directed graph (one-way)
    M = nx.MultiGraph() # undirected multiple edges between nodes (and edges go both ways)
    N = nx.MultiDiGraph() # directed multiple edges between nodes (one-way)
'''


def simple_overview():
    graph = nx.Graph() # undirected graph (edges go both ways)
    # connect node u to node v, if they dont exist they are automatically created by library
    graph.add_edge(1, 2)

    # can also add weight (can interpret it yourself in your code,
    #                   i.e. higher better for speed
    #                     OR lower better for cose
    graph.add_edge(2, 3, weight=0.9)

    # can also use anything hashable (i.e. hash value that never changes during its lifetime,
    #                                      basically anything that is an object in Python)
    graph.add_edge("A", "B")

    # connect node to itself (doesnt really do anything)
    graph.add_edge("B", "B")

    # add node without establishing any connection
    graph.add_node("C")

    # even passing print function as a node
    graph.add_node(print)

    # visualise graph G with labels on nodes
    nx.draw_spring(graph, with_labels=True)


def creating_from_edge_list():
    # can also add edges as a list of tuples
    edge_list = [(1, 2), (2, 3), (3, 4), (3, 5), (4, 6), (6, 7)]

    # CREATE graph from edge list
    graph = nx.from_edgelist(edge_list)

    # visualise graph G with labels on nodes
    nx.draw_spring(graph, with_labels=True)

    # show plotted data
    plt.show()

def adding_from_edge_list():
    # our edge list (same as above)
    edge_list = [(1, 2), (2, 3), (3, 4), (3, 5), (4, 6), (6, 7)]

    # define our graph
    graph = nx.Graph()

    # ADDING edges into our graph
    graph.add_edges_from(edge_list)

    # visualise graph G with labels on nodes
    nx.draw_spring(graph, with_labels=True)

    # show plotted data
    plt.show()

def get_adjacency_matrix():
    # can also add edges as a list of tuples
    edge_list = [(1, 2), (2, 3), (3, 4), (3, 5), (4, 6), (6, 7)]

    # CREATE graph from edge list
    graph = nx.from_edgelist(edge_list)

    # print adjacency matrix of our graph
    print(nx.adjacency_matrix(graph))

def create_adjacency_matrix():
    '''
        here is our n*n adjacency matrix, where n is number of nodes
        this makes sense for directed graph, where say we had nodes A,B,C
        then it is arranged like so:

                    A     B     C

                A   0     1     0

                B   1     1     1

                C   0     0     0

        which means:
                A -> B
                B -> A
                B -> B
                B -> C
        and there are no other edges, since this is directed, in above we can
        see B goes to C, but C does NOT go to B

        OBVIOUSLY though if you want that to be represented properly, use the
        "directed" graph type
    '''
    adj_mat = np.array([[0, 1, 0],
              [1, 1, 1],
              [0, 0, 0]])

    # can then convert this to graph using respective method for numpy arrays
    graph = nx.from_numpy_array(adj_mat)

    # visualise graph G with labels on nodes
    nx.draw_spring(graph, with_labels=True)

    # show plotted data
    plt.show()

def draw_graphs():
    # can also add edges as a list of tuples
    edge_list = [(1, 2), (2, 3), (3, 4), (3, 5), (4, 6), (6, 7)]

    # CREATE graph from edge list
    graph = nx.from_edgelist(edge_list)

    # draw using spring (the one used so far, just a straight line)
    nx.draw_spring(graph, with_labels=True)
    plt.show()

    # draw using circular (tries to draw circle)
    nx.draw_circular(graph, with_labels=True)
    plt.show()

    # draw using shell (tries to draw concentric circles, i.e. circles all have same origin)
    nx.draw_shell(graph, with_labels=True)
    plt.show()

    # draw as spectral graph (relation to adjacency/Laplacian matrix and eigenvalues)
    nx.draw_spectral(graph, with_labels=True)
    plt.show()

    # draw nodes in random positions
    nx.draw_random(graph, with_labels=True)
    plt.show()

    # draw nodes as a planar graph (i.e. edges do NOT intersect with other edges IF POSSIBLE)
    nx.draw_planar(graph, with_labels=True)
    plt.show()

def draw_planar_graph_four_nodes():
    # can also add edges as a list of tuples
    edge_list = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

    # CREATE graph from edge list
    graph = nx.from_edgelist(edge_list)

    # first lets show how it draws normally using spring
    nx.draw_spring(graph, with_labels=True)
    plt.show()

    # will readjust graph so edges dont intersect
    nx.draw_planar(graph, with_labels=True)
    plt.show()

def draw_planar_graph_five_nodes():
    # can also add edges as a list of tuples
    edge_list = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]

    # CREATE graph from edge list
    graph = nx.from_edgelist(edge_list)

    # first lets show how it draws normally using spring
    nx.draw_spring(graph, with_labels=True)
    plt.show()

    # will readjust graph so edges dont intersect
    nx.draw_planar(graph, with_labels=True)
    plt.show()

def draw_complete_graph():
    # specify number of nodes
    num_nodes = 4

    # CREATE graph from edge list
    graph = nx.complete_graph(num_nodes)

    # first lets show how it draws normally using spring
    nx.draw_spring(graph, with_labels=True)
    plt.show()

def get_graph_degrees():
    # can also add edges as a list of tuples
    edge_list = [(1, 2), (2, 3), (3, 4), (3, 5), (4, 6), (6, 7)]

    # CREATE graph from edge list
    graph = nx.from_edgelist(edge_list)

    # can cast to dictionary and index the degrees
    degrees = dict(graph.degree)
    # using list comprehension to print tuple pairs from degrees dictionary
    [print(f'Node {k}: {v} edge(s)') for k,v in degrees.items()]

    # first lets show how it draws normally using spring
    nx.draw_spring(graph, with_labels=True)
    plt.show()



def get_directed_graph_degrees():
    # can also add edges as a list of tuples
    edge_list = [(1, 2), (2, 3), (3, 4), (3, 5), (4, 6), (6, 7)]

    # CREATE directional graph, add edges from our list
    graph = nx.DiGraph()
    graph.add_edges_from(edge_list)

    # can cast to dictionary and index the degrees
    in_degrees = dict(graph.in_degree)
    out_degrees = dict(graph.out_degree)
    total_degrees = dict(graph.degree)
    # using list comprehension to print tuple pairs from degrees dictionary
    print("\nIn Degrees")
    [print(f'Node {k}: {v} edge(s)') for k,v in in_degrees.items()]
    print("\nOut Degrees")
    [print(f'Node {k}: {v} edge(s)') for k,v in out_degrees.items()]
    print("\nTotal Degrees")
    [print(f'Node {k}: {v} edge(s)') for k,v in total_degrees.items()]

    # first lets show how it draws normally using spring
    nx.draw_spring(graph, with_labels=True)
    plt.show()

if __name__ == "__main__":
    # # function gives simple overview of basic functionality of NetworkX
    # simple_overview()


    # # using edge list to CREATE graph
    # creating_from_edge_list()

    # # also using edge list, but ADDING instead of CREATING
    # adding_from_edge_list()


    # # can also get the adjacency matrix representation of our graph
    # get_adjacency_matrix()

    # # can also create adjacency matrix ourselves using numpy
    # create_adjacency_matrix()

    # # lets look at different ways to draw the graphs
    # draw_graphs()

    # # in relation to planar graphs, we can display a COMPLETE graph,
    # # and see how for planar graphs it will try to avoid edges going
    # # through other edges, lets try a complete graph with 4 nodes
    # draw_planar_graph_four_nodes()

    # # now lets try a complete graph with 5 nodes
    # # (will throw exception that G is not planar)
    # draw_planar_graph_five_nodes()

    # # also, we dont have to manually generate complete graphs
    # draw_complete_graph()

    # # we can get specific information about our graph
    # get_graph_degrees()

    # can also do the same SPECIFICALLY for directed graphs (in/out degrees)
    get_directed_graph_degrees()

    # can also find shortest path
    # WIP