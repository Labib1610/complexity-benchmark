import sys
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().strip().split()
    n, m, B = map(int, input_data[:3])
    edges = [[] for _ in range(n)]
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        edges[u].append(v)
        edges[v].append(u)
    
    pos = [0] * n
    visited = [False] * n
    order = []
    
    # DFS to get an ordering
    stack = [0]
    visited[0] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v in edges[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    
    # Assign positions 1..n in DFS order
    for i, node in enumerate(order):
        pos[node] = i + 1
    
    # Compute total cable length
    total = 0
    for u in range(n):
        for v in edges[u]:
            if u < v:
                total += abs(pos[u] - pos[v])
    
    if total <= B:
        print("YES")
        print(" ".join(map(str, pos)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()