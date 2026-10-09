import sys
from collections import defaultdict
import heapq

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    T = set()
    for i in range(t):
        T.add(int(input_data[idx])); idx += 1
    
    if t <= 1:
        print(0)
        return
    
    adj = defaultdict(list)
    edges = []
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to count terminals in each subtree
    # Root at first terminal
    root = next(iter(T))
    parent = {}
    parent_edge_weight = {}
    visited = set()
    stack = [(root, 0, False)]  # node, parent, processed
    order = []
    
    # Iterative DFS
    stack2 = [root]
    visited.add(root)
    parent[root] = 0
    
    while stack2:
        node = stack2.pop()
        order.append(node)
        for nb, w in adj[node]:
            if nb not in visited:
                visited.add(nb)
                parent[nb] = node
                parent_edge_weight[nb] = w
                stack2.append(nb)
    
    # Count terminals in subtree
    subtree_terminals = [0] * (n + 1)
    for node in T:
        subtree_terminals[node] = 1
    
    # Process in reverse order (leaves first)
    for node in reversed(order):
        p = parent[node]
        if p != 0:
            subtree_terminals[p] += subtree_terminals[node]
    
    # An edge (parent[node], node) is needed if subtree_terminals[node] > 0 
    # and (t - subtree_terminals[node]) > 0
    total = 0
    for node in order:
        if node == root:
            continue
        st = subtree_terminals[node]
        if st > 0 and (t - st) > 0:
            total += parent_edge_weight[node]
    
    print(total)

solve()