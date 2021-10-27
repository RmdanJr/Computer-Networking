def Dijkstra(graph, src, dst):
    number_of_nodes = len(graph[0])   # Number of nodes in the graph
    parent = [-1] * number_of_nodes    # Setting up various lists
    visited = []
    unvisited = [i for i in range(number_of_nodes)]
    # The distance list initially has a distance of infinite for all but the source node
    distance = [16] * number_of_nodes
    distance[src] = 0
    shortest_path = []                # This list will have the shortest path at the end
    current = src                     # We start with the source

    while(len(unvisited) > 0):
        # Visit all neighbors of current and update distance
        for i in range(number_of_nodes):
            if(graph[current][i] >= 0 and distance[i] > graph[current][i]+distance[current]):
                distance[i] = graph[current][i] + \
                    distance[current]  # Update distance
                parent[i] = current  # Set new parent

        if(current == dst):
            break

        unvisited.remove(current)  # Move current node from unvisited to visted
        visited.append(current)
        if(len(unvisited) != 0):
            # New current node is an unvisited node with the smallest 'distance'
            current = unvisited[0]
            for n in unvisited:
                if(distance[n] < distance[current]):
                    current = n

    curr = dst  # Some code to get the shortest path from 'parent'
    shortest_path.append(curr)
    cost = 0
    while curr is not src:
        if parent[curr] == -1:  # If there is no path to the source node
            return([[], -1])
        # The cost is the sum of the links in a path
        cost = cost + graph[curr][parent[curr]]
        curr = parent[curr]
        shortest_path.append(curr)
    shortest_path.reverse()
    return([shortest_path, cost])


def main():
    graph = [
        [0, 1, 5, -1, -1],
        [1, 0, 3, -1, 9],
        [5, 3, 0, 4, -1],
        [-1, -1, 4, 0, 2],
        [-1, 9, -1, 2, 0]
    ]
    src = 0
    dst = 3
    print(Dijkstra(graph, src, dst))


if __name__ == "__main__":
    main()
