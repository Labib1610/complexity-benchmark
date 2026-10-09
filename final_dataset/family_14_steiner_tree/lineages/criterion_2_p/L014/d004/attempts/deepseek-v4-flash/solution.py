import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    patents = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # Since m = n-1 and no cycles, it's a tree.
    # We'll root at 1 and do DFS to count patents in subtrees.
    parent = [0]*(n+1)
    parent_w = [0]*(n+1)
    order = [1]
    parent[1] = -1
    for u in order:
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_w[v] = w
                order.append(v)
    
    sub_patents = [0]*(n+1)
    for p in patents:
        sub_patents[p] = 1
    
    total_cost = 0
    # Process in reverse order (post-order)
    for u in reversed(order):
        if u == 1:
            continue
        p = parent[u]
        sub_patents[p] += sub_patents[u]
        if sub_patents[u] > 0 and sub_patents[u] < t:
            total_cost += parent_w[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()