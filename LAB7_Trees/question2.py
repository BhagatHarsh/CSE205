# the graph to find the shortest path


class Graph:
    def __init__(self):
        print("Graph Created")
        self.graph = {}

    def addEdge(self, u, v):
        print("Adding an edge from", u, "to", v)
        try:
            self.graph[u].append(v)
        except:
            self.graph[u] = [v]

    def BFS(self, s):
        visited = {}
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            try:
                for i in self.graph[s]:
                    try:
                        visited[i] = visited[i]
                    except:
                        queue.append(i)
                        visited[i] = True
            except:
                continue
        print("")
        return

    def printall(self):
        for i in self.graph:
            print("Traversing ", i)
            print(self.BFS(i))
        return


graph = Graph()
file = []
with open("question2.txt") as f:
    for line in f:
        file.append(list(map(str, line.strip().split(','))))

for i in range(len(file)):
    for j in range(1, len(file[i])):
        graph.addEdge(int(file[i][0]), int(file[i][j]))

graph.printall()

# the shortest path
