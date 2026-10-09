import sys
sys.setrecursionlimit(300000)

def solve():
    n, m, B = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    assignment = [0] * n
    pos = [0] * n
    visited = [False] * n
    order = []
    
    # DFS to get order
    stack = [0]
    visited[0] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    
    # Assign labels 1..n in DFS order
    for i, node in enumerate(order):
        assignment[node] = i + 1
        pos[node] = i + 1
    
    # Compute total friction
    total = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                total += abs(pos[u] - pos[v])
    
    if total <= B:
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()