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
    
    # Since m = n-1 and graph is connected, it's a tree.
    # We'll root at 1 and do DFS to count patents in subtrees.
    parent = [0]*(n+1)
    parent_w = [0]*(n+1)
    order = [1]
    parent[1] = -1
    for node in order:
        for nei, w in adj[node]:
            if nei != parent[node]:
                parent[nei] = node
                parent_w[nei] = w
                order.append(nei)
    
    sub_patents = [0]*(n+1)
    for p in patents:
        sub_patents[p] = 1
    
    total_cost = 0
    # Process in reverse order (post-order)
    for node in reversed(order):
        if node == 1:
            continue
        if sub_patents[node] > 0 and sub_patents[node] < t:
            total_cost += parent_w[node]
        sub_patents[parent[node]] += sub_patents[node]
    
    print(total_cost)

if __name__ == "__main__":
    solve()