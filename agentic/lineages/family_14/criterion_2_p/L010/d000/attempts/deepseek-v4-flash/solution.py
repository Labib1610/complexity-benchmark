import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    spores = set(map(int, input().split()))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Root the tree at 0
    parent = [-1] * n
    parent_w = [0] * n
    order = [0]
    stack = [0]
    parent[0] = -2  # mark root
    while stack:
        u = stack.pop()
        for v, w in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                parent_w[v] = w
                stack.append(v)
                order.append(v)
    
    has_spore = [False] * n
    for s in spores:
        has_spore[s-1] = True
    
    # Process in reverse order (post-order)
    total_cost = 0
    for u in reversed(order):
        if u == 0:
            continue
        if has_spore[u]:
            total_cost += parent_w[u]
            # propagate up
            p = parent[u]
            while p != -2 and not has_spore[p]:
                has_spore[p] = True
                total_cost += parent_w[p]
                p = parent[p]
    
    print(total_cost)

if __name__ == "__main__":
    solve()