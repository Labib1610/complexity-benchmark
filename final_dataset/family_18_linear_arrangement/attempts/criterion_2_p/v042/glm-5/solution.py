import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    B = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Root at 1, compute subtree sizes iteratively
    parent = [0] * (n+1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if parent[v] == 0:
                parent[v] = u
                stack.append(v)
    
    size = [1] * (n+1)
    for u in reversed(order):
        if parent[u] > 0:
            size[parent[u]] += size[u]
    
    # Minimum total penalty = sum of subtree sizes of non-root nodes
    min_penalty = 0
    for u in range(2, n+1):
        min_penalty += size[u]
    
    if min_penalty > B:
        print("NO")
        return
    
    # Assign channels via DFS (preorder), contiguous blocks
    channels = [0] * (n+1)
    # Process children in decreasing subtree size order for determinism
    children = [[] for _ in range(n+1)]
    for u in range(2, n+1):
        children[parent[u]].append(u)
    for u in range(1, n+1):
        children[u].sort(key=lambda x: -size[x])
    
    # Iterative DFS assigning channels
    ch = 1
    stack = [1]
    while stack:
        u = stack.pop()
        channels[u] = ch
        ch += 1
        # Push children in reverse so largest is processed first
        for c in reversed(children[u]):
            stack.append(c)
    
    print("YES")
    print(' '.join(str(channels[i]) for i in range(1, n+1)))

solve()