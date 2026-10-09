import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    leased = set(map(int, input().split()))
    
    g = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))
        edges.append((u, v, w))
    
    # If only one leased rack, cost is 0
    if t == 1:
        print(0)
        return
    
    visited = [False] * (n + 1)
    count = [0] * (n + 1)
    
    # DFS to count important nodes in each subtree
    stack = [(1, -1, 0)]  # (node, parent, state)
    parent = [0] * (n + 1)
    parent_edge_weight = [0] * (n + 1)
    order = []
    
    while stack:
        node, par, state = stack.pop()
        if state == 0:
            visited[node] = True
            parent[node] = par
            order.append(node)
            stack.append((node, par, 1))
            for nei, w in g[node]:
                if nei != par:
                    parent_edge_weight[nei] = w
                    stack.append((nei, node, 0))
        else:
            cnt = 1 if node in leased else 0
            for nei, _ in g[node]:
                if nei != parent[node]:
                    cnt += count[nei]
            count[node] = cnt
    
    total_cost = 0
    for node in range(2, n + 1):
        if count[node] > 0 and (t - count[node]) > 0:
            total_cost += parent_edge_weight[node]
    
    print(total_cost)

if __name__ == "__main__":
    solve()