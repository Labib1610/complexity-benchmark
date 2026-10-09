import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    t = int(next(iterator))
    
    is_target = [False] * (n + 1)
    for _ in range(t):
        is_target[int(next(iterator))] = True
        
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    if t <= 1:
        print(0)
        return

    parent = [0] * (n + 1)
    weight_to_parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    stack = [1]
    parent[1] = -1
    
    while stack:
        u = stack.pop()
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                weight_to_parent[v] = w
                depth[v] = depth[u] + 1
                stack.append(v)
                
    max_depth = max(depth)
    cnt = [0] * (max_depth + 1)
    for i in range(1, n + 1):
        if is_target[i]:
            cnt[depth[i]] += 1
            
    total_energy = 0
    for u in range(2, n + 1):
        if cnt[depth[u]] > 0:
            total_energy += weight_to_parent[u]
            cnt[depth[parent[u]]] += cnt[depth[u]]
            
    print(total_energy)

if __name__ == '__main__':
    solve()