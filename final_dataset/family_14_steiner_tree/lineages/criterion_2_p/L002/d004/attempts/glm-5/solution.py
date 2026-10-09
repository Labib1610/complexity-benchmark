import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    targets = set()
    for _ in range(t):
        targets.add(int(input_data[idx])); idx += 1
    
    edges = []
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    edges.sort()
    parent = list(range(n + 1))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    tree_adj = [[] for _ in range(n + 1)]
    tree_cost = [0] * (n + 1)
    total_mst = 0
    
    for w, u, v in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
            tree_adj[u].append((v, w))
            tree_adj[v].append((u, w))
            total_mst += w
    
    is_target = [False] * (n + 1)
    for x in targets:
        is_target[x] = True
    
    setrecursionlimit(600000)
    
    # Iterative DFS to compute removable edges (edges where one side has no targets)
    removable = 0
    visited = [False] * (n + 1)
    stack = []
    
    for start in range(1, n + 1):
        if not visited[start] and tree_adj[start]:
            visited[start] = True
            stack.append((start, 0, 0, 0))  # node, child_idx, parent, edge_weight
            
            while stack:
                node, ci, par, ew = stack[-1]
                if ci < len(tree_adj[node]):
                    stack[-1] = (node, ci + 1, par, ew)
                    child, cw = tree_adj[node][ci]
                    if child != par and not visited[child]:
                        visited[child] = True
                        stack.append((child, 0, node, cw))
                else:
                    stack.pop()
                    cnt = 1 if is_target[node] else 0
                    for child, cw in tree_adj[node]:
                        if child != par:
                            cnt += subtree_target_count[child]
                    subtree_target_count[node] = cnt
                    
                    if par != 0:
                        if cnt == 0 or cnt == t:
                            removable += ew
    
    print(total_mst - removable)

solve()