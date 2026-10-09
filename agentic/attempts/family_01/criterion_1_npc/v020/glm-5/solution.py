import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)
    
    # Build complement graph (non-edges)
    comp_adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if j not in adj[i]:
                comp_adj[i].add(j)
                comp_adj[j].add(i)
    
    # Find connected components in complement graph
    visited = [False] * n
    components = []
    
    for i in range(n):
        if not visited[i]:
            comp = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in comp_adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            components.append(comp)
    
    # Check if any component is too large
    for comp in components:
        if len(comp) > 3:
            print("NO")
            return
    
    # Separate components by size
    singles = []
    doubles = []
    triples = []
    
    for comp in components:
        if len(comp) == 1:
            singles.append(comp)
        elif len(comp) == 2:
            doubles.append(comp)
        else:
            triples.append(comp)
    
    # Check if we can form valid groups
    if len(triples) > 1:
        print("NO")
        return
    
    if len(triples) == 1:
        # All singles and doubles must pair up exactly
        if len(singles) != len(doubles):
            print("NO")
            return
    else:
        # No triples: singles and doubles must pair up
        if len(singles) != len(doubles):
            print("NO")
            return
    
    # Construct assignment
    assignment = [0] * n
    
    if triples:
        # Assign triple to drives 1, 2, 3
        t = triples[0]
        assignment[t[0]] = 1
        assignment[t[1]] = 2
        assignment[t[2]] = 3
    
    # Pair singles with doubles
    for i, d in enumerate(doubles):
        s = singles[i]
        # Assign double to drives 1, 2
        assignment[d[0]] = 1
        assignment[d[1]] = 2
        # Assign single to drive 3
        assignment[s[0]] = 3
    
    print("YES")
    print(' '.join(map(str, assignment)))

solve()