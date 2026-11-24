from collections import deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        if 0 <= u < self.V and 0 <= v < self.V:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)  # Undirected graph

    def display_list(self):
        print("\n--- Adjacency List ---")
        for i in range(self.V):
            neighbors = " -> ".join(map(str, self.adj_list[i]))
            print(f"{i}: {neighbors}")

    def bfs(self, start_vertex):
        visited = [False] * self.V
        queue = deque([start_vertex])
        visited[start_vertex] = True

        print("BFS Traversal: ", end="")
        while queue:
            current = queue.popleft()
            print(current, end=" ")

            for neighbor in self.adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        print()


if __name__ == "__main__":
    v = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    g = Graph(v)

    print("Enter edges (u v) using 0-based indexing:")
    for _ in range(e):
        u, w = map(int, input().split())
        g.add_edge(u, w)

    g.display_list()

    start = int(input("\nEnter starting vertex for BFS: "))
    if 0 <= start < v:
        g.bfs(start)
    else:
        print("Invalid starting vertex.")
