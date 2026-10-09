import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    t = int(next(iterator))
    
    required = [False] * (n + 1)
    for _ in range(t):
        required[int(next(iterator))] = True
        
    if t <= 1:
        print(0)
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    # BFS to build parent pointers and topological order from root
    root = 1
    parent = [0] * (n + 1)
    edge_weight = [0] * (n + 1)
    order = []
    
    stack = [root]
    parent[root] = -1
    
    # We can use a queue or stack for tree traversal order
    # Simple BFS with a list as queue:
    queue = [root]
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                edge_weight[v] = w
                queue.append(v)
                
    req_count = [1 if required[i] else 0 for i in range(n + 1)]
    total_cost = 0
    
    for u in reversed(queue):
        if parent[u] != -1:
            p = parent[u]
            req_count[p] += req_count[u]
            if 0 < req_count[u] < t:
                total_cost += edge_weight[u]
                
    print(total_cost)

if __name__ == '__main__':
    main()