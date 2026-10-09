import sys
from collections import deque

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
    
    # Try multiple orders
    orders = []
    
    # DFS order
    parent = [-1]*n
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
    orders.append(order)
    
    # BFS order
    order = []
    q = deque([0])
    parent = [-1]*n
    parent[0] = 0
    while q:
        u = q.popleft()
        order.append(u)
        for v in edges[u]:
            if parent[v] == -1:
                parent[v] = u
                q.append(v)
    orders.append(order)
    
    # Reverse DFS
    orders.append(orders[0][::-1])
    # Reverse BFS
    orders.append(orders[1][::-1])
    
    for order in orders:
        pos = [0]*n
        for i, node in enumerate(order):
            pos[node] = i+1
        total = 0
        for u in range(n):
            for v in edges[u]:
                if u < v:
                    total += abs(pos[u] - pos[v])
        if total <= B:
            print("YES")
            print(" ".join(str(pos[i]) for i in range(n)))
            return
    
    print("NO")

if __name__ == "__main__":
    solve()