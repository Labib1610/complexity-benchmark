import sys
from sys import setrecursionlimit
setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx+=1
    m = int(input_data[idx]); idx+=1
    B = int(input_data[idx]); idx+=1
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(input_data[idx]); idx+=1
        v = int(input_data[idx]); idx+=1
        adj[u].append(v)
        adj[v].append(u)
    
    # Root at node 1, compute subtree sizes, then DFS preorder with largest subtree last
    parent = [0]*(n+1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if parent[v]==0:
                parent[v]=u
                stack.append(v)
    
    size = [1]*(n+1)
    for u in reversed(order):
        if parent[u]>0:
            size[parent[u]] += size[u]
    
    # Build children lists sorted by size ascending (so largest processed last => placed last)
    children = [[] for _ in range(n+1)]
    for u in range(2, n+1):
        children[parent[u]].append(u)
    for u in range(1, n+1):
        children[u].sort(key=lambda x: size[x])  # ascending, largest last
    
    pos = [0]*(n+1)
    counter = [1]
    # iterative DFS preorder
    stack = [(1, False)]
    while stack:
        u, processed = stack.pop()
        if not processed:
            pos[u] = counter[0]
            counter[0]+=1
            stack.append((u, True))
            # push children in reverse so first child processed first
            for c in reversed(children[u]):
                stack.append((c, False))
    
    total = 0
    for u in range(2, n+1):
        total += abs(pos[u]-pos[parent[u]])
    
    if total <= B:
        print("YES")
        print(' '.join(str(pos[i]) for i in range(1, n+1)))
    else:
        print("NO")

solve()