import time
import queue
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os


'''
Course from:
    NeuralNine
on:
    https://www.youtube.com/watch?v=7XVTnCrWDPY
'''

# BFS function
def order_bfs(graph, start_node):
    # since we have a graph, there COULD be cycles, so we keep track of visited nodes
    # we use a set so that there are no duplicates
    visited = set()

    # FIFO
    q = queue.Queue()
    # put first node into queue
    q.put(start_node)

    # result list of order of nodes to travel in for a BFS search
    order = []

    # while we still have nodes in our queue, run loop
    while not q.empty():
        # first node in queue
        vertex = q.get()
        # if vertex is not in our visited nodes, add to our BFS traversal order list
        if vertex not in visited:
            order.append(vertex)
            # also mark this node as visited
            visited.add(vertex)
            # now that we have visited a node, add it to end of the queue
            # (so will be visited after we visit the rest of nodes at same depth in our queue)
            for node in graph[vertex]:
                # HOWEVER, because this is a graph, this could be a cycle, so need to check if
                # each successor node has already been visited
                if node not in visited:
                    q.put(node)

                    # here we do NOT add current node to visited nodes, it will
                    # automatically be added when it is evaluated next in the queue

    # resulting order of nodes
    return order

# DFS function (best done with recursion),
# we ALSO need visited parameter for recursion, initially None
def order_dfs(graph, start_node, visited=None):
    # if no visited nodes, base case, so create empty set for next recursive call
    if visited is None:
        visited = set()

    # result list of order of nodes in DFS search
    order = []

    # if our current node not already visited, add it to order and to visited nodes
    if start_node not in visited:
        order.append(start_node)
        visited.add(start_node)
        # for each neighbour of our current node
        for node in graph[start_node]:
            # if not visited already, look through its neighbours
            if node not in visited:
                # perform a new DFS search, with current node as new start node,
                # the reason we use extend() and not append() is because we return
                # a list, and appending a list onto a list will just make a nested
                # list, so this just makes sure the list is flattened out
                order.extend(order_dfs(graph, node, visited))

                # here we do NOT add current node to visited nodes, it will
                # automatically be added when it becomes the start node in next
                # call of DFS search

    # return order of nodes
    return order

# visualise our search using NetworkX library
def visualise_search(order, title, G, pos):
    plt.figure()
    # different titles for different searches
    plt.title(title)
    # for each node in the order, re-draw graph to show search occurring
    for i, node in enumerate(order, start=1):
        plt.clf()
        plt.title(title)
        # colour coded graph, will be red while at current node,
        # then turn green once that node has been traversed
        nx.draw(G, pos, with_labels=True, node_color=['r' if n == node else 'g' for n in G.nodes])
        plt.draw()
        plt.pause(1.5)
    plt.show()
    time.sleep(0.5)

# takes in number of nodes n and edges m
def generate_connected_random_graph(n, m):
    # brute force way to generate connected graph
    while True:
        G = nx.gnm_random_graph(n, m)
        # if connected, return
        if nx.is_connected(G):
            return G

def search_algorithms_loop():
    # create two graphs used in functions
    G1 = nx.Graph()
    G1.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
    pos_1 = nx.spring_layout(G1)
    G2 = generate_connected_random_graph(15, 20)
    pos_2 = nx.spring_layout(G2)

    run = True
    user_input = -1
    while run:
        # clear screen
        os.system('cls')
        print('\nWelcome to a brief overview of Search Algorithms BFS and DFS in Python \n\t(using the NetworkX library)')
        print('\nHere are your options (1-4):\n\t(check out comments in each function for more in-depth information)')

        print('\n\t(1): BFS Search in Simple Graph')
        print('\t(2): DFS Search in Simple Graph')
        print('\t(3): BFS Search in Complex Graph')
        print('\t(4): DFS Search in Complex Graph')

        print('\nPress \'e\' to exit program')

        while (user_input not in range(1,5)) or (user_input != 'e'):
            user_input = input('\nChoose an input from list: ')

            if user_input.lower() == 'e':
                run = False
                break
            else:
                try:
                    user_input = int(user_input)
                except:
                    print('Invalid input')

            match user_input:
                case 1:
                    visualise_search(order_bfs(G1, 'A'), 'BFS Visualisation', G1, pos_1)
                case 2:
                    visualise_search(order_dfs(G1, 'A'), 'DFS Visualisation', G1, pos_1)
                case 3:
                    visualise_search(order_bfs(G2, 0), 'BFS Visualisation', G2, pos_2)
                case 4:
                    visualise_search(order_dfs(G2, 0), 'DFS Visualisation', G2, pos_2)
                case _:
                    print('Invalid number')
                    break
            # wait for user input before clearing screen in next loop iteration
            input('--Press any key to continue--')
            # reset user input so break out of this loop and ask for user input again
            user_input = -1
            break



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # main program loop
    search_algorithms_loop()
    print('END OF MAIN')