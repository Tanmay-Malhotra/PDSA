class Graph:
    #constructor method, initializes graph when when object of graph class is created
    def __init__(self,num_vertices):
        self.num_vertices = num_vertices
        self.graph=[[0]* num_vertices for _ in range(num_vertices)]

    def add_edge(self,u,v):
        self.graph[u][v]=1
        self.graph[v][u]=1

    def dfs(self,v, visited,component):
        # v is current vertex
        visited[v] = True
        component.append(v)
        for i in range(self.num_vertices):
            #visited[i] stores 1 at ith position if the vertex is visited
            if self.graph[v][i]==1 and not visited[i]:
                self.dfs(i,visited,component)