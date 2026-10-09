import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # Root the tree at 1
    parent = [0]*(n+1)
    weight = [0]*(n+1)
    order = [1]
    parent[1] = -1
    for node in order:
        for nei, w in adj[node]:
            if nei != parent[node]:
                parent[nei] = node
                weight[nei] = w
                order.append(nei)
    
    # Post-order processing
    has_target = [False]*(n+1)
    for node in targets:
        has_target[node] = True
    
    total_cost = 0
    # Process in reverse order (children before parents)
    for node in reversed(order):
        if node == 1:
            continue
        if has_target[node]:
            total_cost += weight[node]
            # propagate up
            p = parent[node]
            if p != -1:
                has_target[p] = True
    
    print(total_cost)

if __name__ == "__main__":
    solve()