from queue import PriorityQueue
def best(start,target,graph):
    visited=[False]*len(graph)
    pq=PriorityQueue()
    pq.put((0,start))
    visited[start]=True
    while not pq.empty():
        u=pq.get()[1]
        print(u,end="   ")
        if u==target:
            break
        for v,c in graph[u]:
            if not visited[v]:
                visited[v]=True
                pq.put((c,v))
    print()
def add_edge(graph,x,y,c):
    graph[x].append((y,c))
    graph[y].append((x,c))
if __name__=="__main__":
    v=6
    graph=[[] for _ in range(v)]
    add_edge(graph, 0, 1, 3)
    add_edge(graph, 0, 2, 6)
    add_edge(graph, 0, 3, 5)
    add_edge(graph, 1, 4, 9)
    add_edge(graph, 2, 5, 12)
    add_edge(graph, 3, 4, 7)
    add_edge(graph, 4, 5, 5)
    
    source = 0
    target = 5
    print("Best-first search path:")
    best(source, target, graph)



