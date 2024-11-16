import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#

# TO UPDATE TCL NOT FOUND ERROR, go to ENVIRONMENT VARIABLES AND UPDATE PATH TO NEW ONE FOR:
#       TCL_LIBRARY
#       TK_LIBRARY
# NEVERMIND, but if you do have issues, NOTICE PATH OF THESE, PyCharms pointed to a slightly different
# place so i made a symbolic link

'''
Course from:
    NeuralNine
on:
    https://www.youtube.com/watch?v=VetBkjcm9Go&t=1162s

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

def find_shortest_path():
    # can also add edges as a list of tuples
    edge_list = [(1, 2), (2, 3), (3, 4), (3, 5), (4, 6), (6, 7),
                 (2, 8), (8, 9), (9, 4)]

    # CREATE graph, add edges from our list
    graph = nx.Graph()
    graph.add_edges_from(edge_list)

    # find shortest path in graph from node 2 to 4 in graph
    # (returns a list of nodes to get to 4)
    print(f'\nShortest path from node 2 to node 4: \n\t{nx.shortest_path(graph, 2, 4)}')

    # first lets show how it draws normally using spring
    nx.draw_planar(graph, with_labels=True)
    plt.show()

    # result above was:
    #   [2, 3, 4]
    # so if we removed node 3 by omitting the edge (2, 3) in our edge list, would result in:
    #   [2, 8, 9, 4]
    # as seen in next graph

    # can also add edges as a list of tuples
    edge_list_two = [(1, 2), (3, 4), (3, 5), (4, 6), (6, 7),
                 (2, 8), (8, 9), (9, 4)]
    # CREATE directional graph, add edges from our list
    graph = nx.Graph()
    graph.add_edges_from(edge_list_two)

    # find shortest path in graph from node 2 to 4 in graph
    # (returns a list of nodes to get to 4)
    print(f'\nShortest path from node 2 to node 4 \n(after removing the edge connecting node 2 and 3): \n\t{nx.shortest_path(graph, 2, 4)}')

    # first lets show how it draws normally using spring
    nx.draw_planar(graph, with_labels=True)
    plt.show()

def find_centrality():
    # can also add edges as a list of tuples
    edge_list = [(1, 2), (2, 3), (3, 4), (3, 5), (4, 6), (6, 7),
                 (2, 8), (8, 9), (9, 4)]

    # CREATE graph, add edges from our list
    graph = nx.Graph()
    graph.add_edges_from(edge_list)

    # Degree Centrality takes the degree of the node (how many other nodes it is connected to)
    # as the most important, so higher degree would imply higher Degree Centrality for that node
    print(f'\nDegree Centrality for each node: \n\t{nx.degree_centrality(graph)}')

    # Closeness Centrality relies on the average distance from this node to all other nodes,
    # so first looks at distance to all other nodes, then divides it by the number of other nodes
    # to get the average distance
    # For example say you have a graph like this (where 0 is a node in graph, X is the node with
    # highest closeness centrality, Y is node with highest degree):
    #              0
    #              |
    #     0--X-----Y-------0--------0------0
    #        |     |
    #        |     |
    #        |     0
    #        0
    # Despite node Y having highest degree, X is higher in closeness centrality BECAUSE if you
    # look at average distance to all other nodes, X is one average closer to the rest
    print(f'\nCloseness Centrality for each node: \n\t{nx.closeness_centrality(graph)}')

    # Eigenvector Centrality also takes into consideration importance of nodes, so it cares about
    # how connected it is to other nodes BUT ALSO the quality of other nodes, because if it is
    # connected to a lot of unimportant nodes, still not an important node, but if a node is
    # connected to fewer nodes but they are more important, would be more important so should
    # have higher centrality
    print(f'\nEigenvector Centrality for each node: \n\t{nx.eigenvector_centrality(graph)}')

    # Betweenness Centrality means the percentage of shortest paths that run through a particular
    # node, or in simpler terms, how much % of shortest paths run through a node, so how many of
    # those optimal/important shortest paths run through a node to use the shortest path
    print(f'\nBetweenness Centrality for each node: \n\t{nx.betweenness_centrality(graph)}')

    # first lets show how it draws normally using spring
    nx.draw_planar(graph, with_labels=True)
    plt.show()

def show_betweenness_centrality():
    # CREATE graphs
    graph_one = nx.complete_graph(5)
    graph_two = nx.complete_graph(5)

    # relabelling nodes based specified by our dictionary (key is node name, remapped to value)
    graph_two = nx.relabel_nodes(graph_two, {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'})

    # X will be the bridge connecting our two graphs
    graph_connector = nx.from_edgelist([(4, 'X'), ('X', 'A')])

    # from a full graph from the previous 3 created so we end up with:
    #
    #          (rest of graph_one)-4--------X--------A-(rest of graph_two)
    graph = nx.compose_all([graph_one, graph_two, graph_connector])

    # This is the graph we now have:
    #
    #      2 1           B C
    #       \|           |/
    #     3--0-----X-----A--D
    #        |           |
    #        4           E
    #
    # We can compare the degree centrality to betweenness centrality to see that, although nodes
    # 0 and A have highest degree centrality, X has the highest betweenness centrality because
    # it is a bridge that connects both graphs, and is the only bridge between them
    print(f'\nDegree Centrality for each node: \n\t{nx.degree_centrality(graph)}')
    print(f'\nBetweenness Centrality for each node: \n\t{nx.betweenness_centrality(graph)}')

    # first lets show how it draws normally using spring
    nx.draw_spring(graph, with_labels=True)
    plt.show()

def get_density_and_diameter():
    # CREATE one graph (same one used in show_betweenness_centrality function)
    graph_one = nx.complete_graph(5)
    graph_two = nx.complete_graph(5)
    graph_two = nx.relabel_nodes(graph_two, {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'})
    graph_connector = nx.from_edgelist([(4, 'X'), ('X', 'A')])
    graph = nx.compose_all([graph_one, graph_two, graph_connector])

    # Density means how many edges we have in our graph divided by how many edges we COULD have
    # if we were to connect every node to every other node, making the graph complete
    # i.e.
    #       density = (total_graph_edges)/(total_possible_edges)
    # so, for a complete graph, density = 1
    print(f'\nDensity of example graph: \n\t{nx.density(graph)}')
    print(f'\nDensity of complete graph: \n\t{nx.density(graph_one)}')

    # Diameter means the longest shortest path, in other words, if we were trying to get from
    # one end of graph to the furthest point on the other end of the graph, how far away would
    # it be, assuming we take the optimal path (in this case returns number of edges it has to
    # cross to get to that other node)
    #
    # For a complete graph, diameter = 1 (in number of edges) BECAUSE every node is connected
    # to every other node, so there is a direct path to the node on opposite end of the graph
    # if it is complete
    print(f'\nDiameter of example graph: \n\t{nx.diameter(graph)}')
    print(f'\nDiameter of complete graph: \n\t{nx.diameter(graph_one)}')

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

    # # can also do the same SPECIFICALLY for directed graphs (in/out degrees)
    # get_directed_graph_degrees()

    # # can also do the same SPECIFICALLY for directed graphs (in/out degrees)
    # find_shortest_path()

    # # sometimes we want to know how central a node is in the graph, can decide in different ways
    # # (all the different centralities used are explained through comments within the function)
    # find_centrality()

    # # to show betweenness centrality a bit better, will showcase in its own function
    # show_betweenness_centrality()

    # can obtain density and diameter of graph
    get_density_and_diameter()





