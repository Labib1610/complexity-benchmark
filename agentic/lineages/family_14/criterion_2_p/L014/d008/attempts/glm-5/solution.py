import sys
sys.setrecursionlimit(500000)

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    key_holders = set()
    for _ in range(t):
        key_holders.add(int(next(it)))
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
        adj[u].append((v, len(edges) - 1))
        adj[v].append((u, len(edges) - 1))
    
    # DFS to compute tin, tout, and parent info
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    parent_edge = [-1] * (n + 1)  # edge index leading to this node
    parent_node = [0] * (n + 1)
    timer = 0
    
    stack = [(1, 0, -1, 0)]  # (node, state, parent, parent_edge_idx)
    # state 0 = enter, state 1 = exit
    
    while stack:
        u, state, p, pe = stack.pop()
        if state == 0:
            tin[u] = timer
            timer += 1
            parent_node[u] = p
            parent_edge[u] = pe
            stack.append((u, 1, p, pe))
            for v, ei in adj[u]:
                if v == p:
                    continue
                stack.append((v, 0, u, ei))
        else:
            tout[u] = timer
            timer += 1
    
    def is_ancestor(u, v):
        return tin[u] <= tin[v] and tout[v] <= tout[u]
    
    # For each key holder, find LCA path and mark edges
    critical = [False] * m
    
    # Process each key holder (except the first one which we use as reference)
    key_list = list(key_holders)
    root = key_list[0]
    
    for key in key_list[1:]:
        # Mark path from key to root
        v = key
        while v != root:
            pe = parent_edge[v]
            if pe != -1:
                critical[pe] = True
            v = parent_node[v]
    
    # Sum weights of critical edges
    total = 0
    for i in range(m):
        if critical[i]:
            total += edges[i][2]
    
    print(total)

if __name__ == "__main__":
    solve()