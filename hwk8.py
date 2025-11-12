# Name:       Quinn He, Elaine Chen, Emily Wang, Tanya Chen
# Peers:      Maggie Hollis (CSC TA)
# References: N/A

def get_initial_parents(graph:dict[str|None,dict[str,float]|None], initial:str) -> dict[str,str|None]|None:
    parents:dict[str,str|None] = {}
    for node in graph.keys():
        if node != None and node != initial:
            parents[node] = None
    initial_neighbors = graph[initial]
    if initial_neighbors == None:   # Error Checking
        return None
    for key in initial_neighbors.keys():
        parents[key] = initial
    return parents

def get_initial_costs(graph:dict[str|None,dict[str,float]|None], initial:str) -> dict[str,float]|None:
    costs:dict[str,float] = {}
    for node in graph.keys():
        if node != None:
            costs[node] = float("inf")
    initial_neighbors = graph[initial]
    if initial_neighbors == None:   # Error Checking
        return None
    for key, value in initial_neighbors.items():
        costs[key] = value
    return costs

def find_lowest_cost_node(costs:dict[str,float], processed:list[str]) -> str|None:
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node.
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            # ... set it as the new lowest-cost node.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def run_dijkstra(graph:dict[str|None,dict[str,float]|None], start:str, finish:str) -> list[str]:
    if start == finish:
        return [start]
    if start not in graph or finish not in graph:
        return []
    
    processed:list[str] = []
    parents = get_initial_parents(graph, start)
    costs = get_initial_costs(graph, start)

    if parents is None or costs is None:
        return []
    
    node = find_lowest_cost_node(costs, processed)
    processed.append(start)

    while node is not None:
        cost = costs[node]

        neighbors = graph[node] 
        if neighbors is not None:
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if costs[n] > new_cost:
                    costs[n] = new_cost 
                    parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs,processed)

    if finish not in costs or costs[finish] == float('inf'):
        return []

    path:list[str] = [finish] 
    curr:str = finish
    while (curr != start):
        parent:str|None = None
        if curr in parents.keys():
            parent = parents[curr]
        if parent is None:
            return []
        curr = parent
        path = [curr] + path
    return path


def main():
    # Assumption: We implement our undirected graph such that the undirected edges are represented as two directed edges (one each way). 
    graph:dict[str|None,dict[str,float]|None] = {}
    graph['Ford'] = {'Parking Lot':1, 'Gym':0.7, 'Menden':0, 'Bass':1, 'Seelye':0}
    graph['Parking Lot'] = {'Ford':1}
    graph['Gym'] = {'Ford':0.7, 'Sage':0.2}
    graph['Menden']  = {'Ford':0, 'Sage':0}
    graph['Bass'] = {'Ford':1, 'McConnell':0.1, 'Alumnae Gym':0.1, 'Neilson':0.6, 'Burton-Sabin-Reed':0.1}
    graph['Sage'] = {'Gym':0.2, 'Menden':0, 'Botanic Garden':0.7}
    graph['Seelye'] = {'Ford':0, 'Alumnae Gym':0.3, 'Hillyer':0.1}
    graph['Alumnae Gym'] = {'Seelye':0.3, 'Bass':0.1}
    graph['Hillyer'] = {'Seelye':0.1, 'Hatfield':0}
    graph['McConnell'] = {'Bass':0.1, 'Burton-Sabin-Reed':0.1}
    graph['Botanic Garden'] = {'Sage':0.7, 'Burton-Sabin-Reed':0.3}
    graph['Burton-Sabin-Reed'] = {'Botanic Garden':0.3, 'McConnell':0.1, 'Bass':0.1}
    graph['Hatfield'] = {'Hillyer':0}
    graph['Neilson'] = {'Bass':0.6, 'Wright':0.2, 'Campus Center':0.6}
    graph['Wright'] = {'Neilson':0.2, 'Campus Center':0.2}
    graph['Campus Center'] = {'Neilson':0.6, 'Wright':0.2}

    # print(f"From Ford to Neilson: {run_dijkstra(graph, 'Ford', 'Neilson')}")
    # print(f"From Ford to Botanic Garden: {run_dijkstra(graph, 'Ford', 'Botanic Garden')}")
    # print(f"From Bass to Campus Center: {run_dijkstra(graph, 'Bass', 'Campus Center')}")
    # print(f"From Ford to Hatfield: {run_dijkstra(graph, 'Ford', 'Hatfield')}")
    # print(f"From Ford to Bass: {run_dijkstra(graph, 'Ford', 'Bass')}")
    # print(f"From Ford to Ford: {run_dijkstra(graph, 'Ford', 'Ford')}")
    # print(f"From Ford to X: {run_dijkstra(graph, 'Ford', 'X')}")

    nodes = list(graph.keys())
    print("Nodes: [", end="")
    for i in range(len(nodes)):
        print(nodes[i], end="")
        if i != len(nodes) - 1:
            print(", ", end="")
    print("]")

    while True:
        start = input("Enter the start node: ").strip()
        finish = input("Enter the destination node: ").strip()
        if start in graph and finish in graph:
            break
        print("Error: one or both nodes are invalid.")

    path = run_dijkstra(graph, start, finish)

    if len(path) > 0:
        print("Shortest path:", end=" ")
        for i in range(len(path)):
            print(path[i], end="")
            if i != len(path) - 1:
                print(" -> ", end="")
        print()
    else:
        print("No path is found.")


if __name__ == "__main__":
    main()
