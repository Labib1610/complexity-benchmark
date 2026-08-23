import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    adj = [set() for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        adj[u].add(v)
        adj[v].add(u)
    
    # Check for K4: if any vertex has degree >= 3, check if 3 of its neighbors form a triangle
    for v in range(n):
        if len(adj[v]) >= 3:
            neighbors = list(adj[v])
            # Check all triples of neighbors
            for i in range(len(neighbors)):
                for j in range(i+1, len(neighbors)):
                    if neighbors[j] in adj[neighbors[i]]:
                        for k in range(j+1, len(neighbors)):
                            if neighbors[k] in adj[neighbors[i]] and neighbors[k] in adj[neighbors[j]]:
                                print("NO")
                                return
    
    # Greedy assignment: assign smallest available color
    color = [0] * n
    for v in range(n):
        used = set()
        for u in adj[v]:
            if color[u] != 0:
                used.add(color[u])
        for c in range(1, 4):
            if c not in used:
                color[v] = c
                break
    
    print("YES")
    print(' '.join(map(str, color)))

solve()