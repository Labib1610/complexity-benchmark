import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    flagged = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # DFS to count flagged nodes in subtree and sum weights of necessary edges
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                stack.append(v)
    
    sub_count = [0] * (n + 1)
    for u in flagged:
        sub_count[u] = 1
    
    total = 0
    for u in reversed(order):
        if u != 1:
            if sub_count[u] > 0 and t - sub_count[u] > 0:
                total += parent_weight[u]
            if parent[u] != -1:
                sub_count[parent[u]] += sub_count[u]
    
    print(total)

if __name__ == "__main__":
    solve()