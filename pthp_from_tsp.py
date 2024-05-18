import networkx as nx
from mtsp_dp import mtsp_dp
from student_utils import *

def pthp_solver_from_tsp(G, H):
    """
    PTHP sovler via reduction to Euclidean TSP.
    Input:
        G: a NetworkX graph representing the city.\
        This directed graph is equivalent to an undirected one by construction.
        H: a list of home nodes that you must vist.
    Output:
        tour: a list of nodes traversed by your car.

    All nodes are reprented as integers.

    You must solve the question by first transforming a PTHP\
    problem to a TSP problem. After solving TSP via the dynammic\
    programming algorithm introduced in lectures, construct a solution\
    for the original PTHP problem.
    
    The tour must begin and end at node 0.
    It can only go through edges that exist in the graph..
    It must visit every node in H.
    """
    
    # reduction
    reduced_graph = nx.Graph()
    reduced_graph.add_node(0)
    reduced_graph.add_nodes_from(H)

    shortest_path = dict(nx.all_pairs_bellman_ford_path_length(G))
    
    reduced_graph_nodes = list(reduced_graph.nodes)

    new_graph = nx.Graph()
    new_graph.add_nodes_from([i for i in range(len(reduced_graph_nodes))])

    # print(reduced_graph.nodes)
    # print(new_graph.nodes)
    for i in range(len(reduced_graph_nodes)):
        for j in range(i+1, len(reduced_graph_nodes)):
            source = reduced_graph_nodes[i]
            target = reduced_graph_nodes[j]
            new_graph.add_edge(i, j, weight = shortest_path[source][target])
        new_graph.add_edge(i,i, weight = 0)

    tsp_tour = mtsp_dp(new_graph)
    # # print()
    # # print(tsp_tour)
    # # print()

    # # reduction
    
    # shortest_path_nodes = dict(nx.all_pairs_bellman_ford_path(G))
    # # print(shortest_path_nodes)
    # # print()

    # tour = []

    # for i in range(len(tsp_tour)-1):
    #     source = tsp_tour[i]
    #     target = tsp_tour[i+1]
    #     if i == 0:
    #         tour += shortest_path_nodes[source][target]
    #     else:
    #         tour += shortest_path_nodes[source][target][1:]

    # print(tour)
    tour = 0
    return tour


if __name__ == "__main__":
    pass