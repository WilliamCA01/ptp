import networkx as nx
import math

memo = [[-1]*(1 << (20+1)) for _ in range(20+1)]

def mtsp_dp(G):
    """
    TSP solver using dynamic programming.
    Input:
        G: a NetworkX graph representing the city.\
        This directed graph is equivalent to an undirected one by construction.
    Output:
        tour: a list of nodes traversed by your car.

    All nodes are reprented as integers.

    You must solve the problem using dynamic programming.
    
    The tour must begin and end at node 0.
    It can only go through edges that exist in the graph..
    It must visit every node in G exactly once.
    """

    nodes = list(G.nodes)
    number = len(nodes)

    # memo = [[-1]*(1 << (number+1)) for _ in range(number+1)]

    result = math.inf
    # print(G.edges)

    for i in range(number):
        print(f"[DEBUG] i: {i}")
        second_result = dp_MTSP(i, (1 << (number+1))-1, number, G) + G.edges[i,0]['weight']
        print(f"[DEBUG] result: {second_result}")
        result = min(result, second_result)
    
    print("Answer:", result)
    # memo = [[-1] * (max(nodes)) for _ in range(G.number_of_nodes())]
    # nodes.remove(0)
    # print(f"[DEBUG] nodes: {nodes}\n")

    # n = max(nodes)
    # memo = [[-1]*(1 << (n+1)) for _ in range(n+1)]
    # result = [math.inf, [0]]

    # second_result = 10**9

    # for i in range(1, n+1):

    #     if i in nodes:
    #         second_result = min(second_result, dp_MTSP(i, (1 << (n+1))-1, G, memo, n) + G.edges[i, 0]['weight'])

    #         # second_result += G.edges[i, 0]['weight']

    #         # if second_result < result:
    #             # result = second_result


    # print(second_result)
    # tour = second_result


    tour = result
    return tour

def dp_MTSP(source, mask, number, G):

    if mask == ((1 << source) | 3):
        return G.edges[0][source]
    
    if memo[source][mask] != -1:
        return memo[source][mask]
    
    result = math.inf

    for j in range(number):
        if (mask & (1 << j)) != 0 and j != source and j != 0:
            # print(f"[DEBUG] j: {j}")
            # print(f"[DEBUG] source: {source}")
            result = min(result, dp_MTSP(j, mask & (~(1 << source)), number, G) + G.edges[j, source]['weight'])

    memo[source][mask] = result
    return result

    # if nodes == ((1 << source) | 3):
    #     return G.edges[0, source]['weight']
    
    # if memo[source][nodes] != -1:
    #     return memo[source][nodes]
    
    # result = 10**9

    # for i in range(1, n+1):
    #     if i in list(G.nodes):
    #         if (nodes & (1 << i)) != 0 and source != i and i != 0:
    #             # print(f"[DEBUG] i: {i}, source: {source}\n")
    #             # print(f"[DEBUG] edges: {}\n")
    #             result = min(result, dp_MTSP(i, nodes & (~(1 << source)), G, memo, n) + G.edges[i, source]['weight'])
    # memo[source][nodes] = result



    return result

# def dp_MTSP(source, nodes, G, tour, memo):

#     if nodes == ((1 << source) | 3):
#         current_tour = tour.copy()
#         current_tour.append(0)
#         return [G.edges[source, 0]['weight'], current_tour]
    
#     if memo[i][]

#     result = [math.inf, tour]

#     for neighbor in nodes:
#         current_node = nodes.copy()
#         current_node.remove(neighbor)

#         current_tour = tour.copy()
#         current_tour.append(neighbor)

#         """
#         The code below is a modification to:
#             `result = min(result, dp_MTSP(neighbor, current_node, G) + G.edges[source, neighbor]['weight'])`
       
#         This modification helps with noting down the Hamiltonian Tour nodes
#         """
        
#         second_result = dp_MTSP(neighbor, current_node, G, current_tour)
#         second_result[0] += G.edges[source, neighbor]['weight']

#         if second_result[0] < result[0]:
#             result = second_result
    
#     return result