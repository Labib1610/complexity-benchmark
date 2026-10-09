import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    essential = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    parent = [0] * (n + 1)
    parent_w = [0] * (n + 1)
    order = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    for node in order:
        for nxt, w in adj[node]:
            if not visited[nxt]:
                visited[nxt] = True
                parent[nxt] = node
                parent_w[nxt] = w
                order.append(nxt)
    
    has_essential = [False] * (n + 1)
    for e in essential:
        has_essential[e] = True
    
    total_cost = 0
    for node in reversed(order):
        if node == 1:
            continue
        if has_essential[node]:
            total_cost += parent_w[node]
            has_essential[parent[node]] = True
        else:
            # check if any child had essential
            # we can check by propagating up: if node has essential in its subtree
            # We already propagated from children before reaching here due to reversed order
            if has_essential[node]:
                total_cost += parent_w[node]
                has_essential[parent[node]] = True
    
    print(total_cost)

if __name__ == "__main__":
    solve()