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
    
    # DFS to get order and compute minimal sum
    parent = [-1] * n
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v in edges[u]:
            if parent[v] == -1:
                parent[v] = u
                stack.append(v)
    
    # Assign slots in DFS order
    slot = [0] * n
    for i, node in enumerate(order):
        slot[node] = i + 1
    
    # Compute total length
    total = 0
    for u in range(n):
        for v in edges[u]:
            if u < v:
                total += abs(slot[u] - slot[v])
    
    if total <= B:
        print("YES")
        print(" ".join(str(slot[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()