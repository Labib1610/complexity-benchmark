import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Read transactions
    transactions = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        transactions.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
    
    # Try to 3-color the graph where nodes are transactions
    # Two transactions are adjacent if they share an account
    
    # Build adjacency list for transaction graph
    graph = [[] for _ in range(m)]
    for account in range(1, n + 1):
        txns = adj[account]
        for i in range(len(txns)):
            for j in range(i + 1, len(txns)):
                graph[txns[i]].append(txns[j])
                graph[txns[j]].append(txns[i])
    
    # 3-coloring using backtracking
    color = [0] * m  # 0 means uncolored
    
    def is_safe(node, c):
        for neighbor in graph[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node == m:
            return True
            
        for c in range(1, 4):
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
                
        return False
    
    if backtrack(0):
        print("YES")
        print(*color)
    else:
        print("NO")

solve()