import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    nL = int(next(it))
    nR = int(next(it))
    m = int(next(it))
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        
    if m == 0:
        print("YES")
        print()
        return
        
    deg_L = [0] * (nL + 1)
    deg_R = [0] * (nR + 1)
    for u, v in edges:
        deg_L[u] += 1
        deg_R[v] += 1
        
    Delta = max(max(deg_L), max(deg_R))
    
    # We use a greedy edge coloring algorithm for bipartite graphs.
    # Since the graph is bipartite, Vizing's theorem for bipartite graphs
    # guarantees that the edge chromatic number is exactly Delta.
    # We maintain for each vertex the set of available colors.
    # For each edge (u, v), we find a color c_u available in u and c_v available in v.
    # If c_u == c_v, we assign it. Otherwise, we find an alternating path starting
    # from v using colors c_u and c_v, and swap the colors along this path.
    # This makes c_u available at v, so we can assign c_u to the edge (u, v).
    
    avail_L = [set(range(1, Delta + 1)) for _ in range(nL + 1)]
    avail_R = [set(range(1, Delta + 1)) for _ in range(nR + 1)]
    
    # To quickly find an available color, we can just pop from the set.
    # We will add it back if not used.
    ans = [0] * m
    
    for i in range(m):
        u, v = edges[i]
        
        c_u = avail_L[u].pop()
        c_v = avail_R[v].pop()
        
        if c_u == c_v:
            ans[i] = c_u
        else:
            # Find alternating path starting from v using colors c_u and c_v
            path = []
            curr_v = v
            curr_color = c_u
            while True:
                # Find the edge incident to curr_v colored curr_color
                found = -1
                for j in range(i):
                    if ans[j] == curr_color:
                        uj, vj = edges[j]
                        if vj == curr_v:
                            found = j
                            break
                        if uj == curr_v:
                            found = j
                            break
                if found == -1:
                    break
                path.append(found)
                uj, vj = edges[found]
                # Move to the other endpoint of the edge
                curr_v = uj if vj == curr_v else vj
                curr_color = c_v if curr_color == c_u else c_u
                
            # Swap colors along the path
            for j in path:
                ans[j] = c_v if ans[j] == c_u else c_u
                
            avail_R[v].add(c_v)
            ans[i] = c_u
            
        avail_L[u].add(c_v)
        avail_R[v].add(c_u)
        
    print("YES")
    print(*(ans))

if __name__ == '__main__':
    solve()