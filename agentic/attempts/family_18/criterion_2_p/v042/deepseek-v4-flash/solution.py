import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Compute subtree sizes and min sum
    parent = [-1] * n
    order = [0]
    for u in order:
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                order.append(v)
    
    size = [1] * n
    min_sum = 0
    for u in reversed(order):
        if parent[u] != -1:
            size[parent[u]] += size[u]
            min_sum += size[u]
    
    if min_sum > B:
        print("NO")
        return
    
    # Assign channels in DFS order
    assignment = [0] * n
    current = 1
    stack = [0]
    visited = [False] * n
    visited[0] = True
    while stack:
        u = stack.pop()
        assignment[u] = current
        current += 1
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    solve()