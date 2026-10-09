import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    t = int(next(iterator))
    
    is_audit = [0] * (n + 1)
    for _ in range(t):
        is_audit[int(next(iterator))] = 1
        
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    parent = [0] * (n + 1)
    weight_to_parent = [0] * (n + 1)
    order = []
    stack = [1]
    
    # Handle n = 1 edge case
    if n == 1:
        print(0)
        return
        
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                weight_to_parent[v] = w
                stack.append(v)
                
    count = [0] * (n + 1)
    for i in range(n, -1, -1):
        if i == 0:
            break
        u = order[i - 1]
        if is_audit[u]:
            count[u] += 1
        p = parent[u]
        if p != -1:
            count[p] += count[u]
            
    total_cost = 0
    for i in range(1, n + 1):
        u = order[i - 1]
        p = parent[u]
        if p != -1:
            if count[u] > 0 and count[u] < t:
                total_cost += weight_to_parent[u]
                
    print(total_cost)

if __name__ == '__main__':
    solve()