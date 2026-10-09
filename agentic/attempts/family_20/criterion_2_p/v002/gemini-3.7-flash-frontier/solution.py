import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    nL = int(input_data[0])
    nR = int(input_data[1])
    m = int(input_data[2])
    
    if m == 0:
        print("YES")
        print()
        return

    N = nL + nR
    to = [{} for _ in range(N + 1)]
    edge_col = [0] * m
    
    idx = 3
    for eid in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1]) + nL
        idx += 2
        
        # Find smallest free color for u
        c1 = 1
        while c1 in to[u]:
            c1 += 1
            
        # Find smallest free color for v
        c2 = 1
        while c2 in to[v]:
            c2 += 1
            
        if c1 == c2:
            to[u][c1] = (v, eid)
            to[v][c1] = (u, eid)
            edge_col[eid] = c1
            continue
            
        # Trace alternating path from v
        path_vertices = [v]
        path_edges = []
        curr = v
        c = c1
        while c in to[curr]:
            nxt, e = to[curr][c]
            path_edges.append(e)
            path_vertices.append(nxt)
            curr = nxt
            c = c2 if c == c1 else c1
            
        # Flip edge colors along the path
        for e in path_edges:
            edge_col[e] = c2 if edge_col[e] == c1 else c1
            
        # Swap c1 and c2 mappings at all vertices on the path
        for w in path_vertices:
            has_c1 = c1 in to[w]
            has_c2 = c2 in to[w]
            if has_c1 and has_c2:
                to[w][c1], to[w][c2] = to[w][c2], to[w][c1]
            elif has_c1:
                to[w][c2] = to[w].pop(c1)
            elif has_c2:
                to[w][c1] = to[w].pop(c2)
                
        # Insert the new edge with color c1
        to[u][c1] = (v, eid)
        to[v][c1] = (u, eid)
        edge_col[eid] = c1

    print("YES")
    print(*(edge_col[i] for i in range(m)))

if __name__ == '__main__':
    solve()