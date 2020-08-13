
def earliest_ancestor(ancestors, starting_node):

    # Stores parents and children in graph where key=child and value=parent.
    graph = {}

    # Adds each child as the key in for each entry.
    for ancestor in ancestors:
        if ancestor[1] in graph:
            graph[ancestor[1]].append(ancestor[0])
        else:
            graph[ancestor[1]] = [ancestor[0]]

    curr = starting_node

    print(graph)
    
    # If the input individual is not in the graph, it has no parents.
    if curr not in graph:
        return -1

    # Sets the current individual.
    curr = starting_node

    while True:

        # Array to store the current path of ancestors.
        path = []

        # Checks the array of parents for each child in the graph.
        for ancestor in graph[curr]:
            
            # If the the parent is also a child, add it to the path.
            if ancestor in graph:
                path = path + graph[ancestor]
        
        if len(path) == 0:
            return graph[curr][0]
        else:
            graph[curr] = path