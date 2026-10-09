from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    M = int(data[1])
    T = int(data[2])
    m = int(data[3])
    
    edges = []
    index = 4
    for _ in range(m):
        a = int(data[index]) - 1
        b = int(data[index+1]) - 1
        edges.append((a, b))
        index += 2
    
    # Build graph
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for a, b in edges:
        graph[a].append(b)
        indegree[b] += 1
        
    # Topological sort with layer tracking
    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
            
    layers = []
    while queue:
        current_layer = []
        for _ in range(len(queue)):
            node = queue.popleft()
            current_layer.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        layers.append(current_layer)
        
    if len(layers) > T:
        print("NO")
        return
        
    result = [0] * n
    for cycle in range(len(layers)):
        procedures_in_cycle = layers[cycle]
        if len(procedures_in_cycle) > M:
            print("NO")
            return
        for proc in procedures_in_cycle:
            result[proc] = cycle + 1
            
    # For remaining unassigned (should not happen in valid DAG)
    for i in range(n):
        if result[i] == 0:
            print("NO")
            return
            
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()