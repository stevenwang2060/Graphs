"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() # Holds edges.

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Non-existent vertice")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Creates an empty queue.
        q = Queue()

        # Creates a set to store the visited nodes.
        visited = set()

        # Enqueue the starting node.
        q.enqueue(starting_vertex)

        # While the queue isn't empty,
        while q.size() > 0:

            # dequeue the first item.
            v = q.dequeue()

            # If it's not been visited,
            if v not in visited:
                print(v)

                # mark as visited.
                visited.add(v)
                
                # Adds all neighbors to the queue.
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

        """for x in visited:
            print(x)
        """

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Creates an empty stack.
        s = Stack()

        # Creates a set to store the visited nodes.
        visited = set()

        # Pushes the starting node.
        s.push(starting_vertex)

        # While the stack isn't empty,
        while s.size() > 0:
            # pop the first item.
            v = s.pop()
            
            # If it's not been visited,
            if v not in visited:
                # mark as visited.
                visited.add(v)
                print(v)
                
                # Adds all neighbors to the stack.
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, cache = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)

        # Creates a cache to store all the visted node.
        if cache is None:
            cache = set()
        
        cache.add(starting_vertex)

        for x in self.get_neighbors(starting_vertex):
            if x not in cache:
                self.dft_recursive(starting_vertex=x, cache=cache)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty Queue.
        q = Queue()

        q.enqueue([starting_vertex])

        # Creates a Set to store visited vertices.
        visited = set()

        # While the queue is not empty,
        while q.size() > 0:

            # dequeue the first PATH.
            path = q.dequeue()

            # Grab the last vertex from the PATH.
            last_vertex = path[-1]
            
            # If the last vertex is not in visited, we need to check its neighbors.
            if last_vertex not in visited:

                # If the last vertex is the destination, return the path.
                if last_vertex == destination_vertex:
                    return path

                # Else, we create new paths with each neighbor of the last vertex and enqueue them to be searched.
                else:
                    visited.add(last_vertex)
                    for x in self.get_neighbors(last_vertex):
                        new_path = list(path)
                        new_path.append(x)
                        q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()

        s.push([starting_vertex])

        # Create a Set to store visited vertices.
        visited = set()

        # While the queue is not empty,
        while s.size() > 0:

            # dequeue the first PATH.
            path = s.pop()

            # Grab the last vertex from the PATH.
            last_vertex = path[-1]

            # If the last vertex is not in visited, we need to check its neighbors.
            if last_vertex not in visited:

                # If the last vertex is the destination, return the path.
                if last_vertex == destination_vertex:
                    return path

                # Else, we create new paths with each neighbor of the last vertex and enqueue them to be searched.
                else:
                    visited.add(last_vertex)
                    for x in self.vertices[last_vertex]:
                        new_path = list(path)
                        new_path.append(x)
                        s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, path = None, visited = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if path is None:
            path = []
        
        visited.add(starting_vertex)

        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path
        
        for x in self.get_neighbors(starting_vertex):
            if x not in visited:
                new_path = self.dfs_recursive(starting_vertex=x, destination_vertex=destination_vertex, 
                path=path, visited=visited)

                if new_path:
                    return new_path
        
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
