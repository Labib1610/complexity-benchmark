import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    NE = int(input_data[0])
    NC = int(input_data[1])
    M = int(input_data[2])
    
    if M == 0:
        print("YES")
        print("")
        return
        
    tests = []
    for i in range(M):
        u = int(input_data[3 + 2*i])
        v = int(input_data[3 + 2*i + 1])
        tests.append((u, v))
        
    deg_E = [0] * (NE + 1)
    deg_C = [0] * (NC + 1)
    
    for u, v in tests:
        deg_E[u] += 1
        deg_C[v] += 1
        
    D = max(max(deg_E), max(deg_C))
    
    # We use a greedy edge coloring algorithm.
    # Since the bipartite graph has maximum degree D, we can color edges in D colors.
    # We process edges in an arbitrary order. For each edge (u, v), we find the 
    # smallest available color for u and the smallest for v. If they are the same, 
    # we use it. If they differ, we use the color for u and recolor the chain of 
    # edges starting from v with the color of u.
    
    color_E = [0] * (NE + 1)
    color_C = [0] * (NC + 1)
    
    # To efficiently find the smallest unused color for a vertex, we maintain
    # a pointer to the next candidate color. Since each vertex has at most D edges,
    # the colors used will be in 1..D.
    ptr_E = [1] * (NE + 1)
    ptr_C = [1] * (NC + 1)
    
    # We need to quickly find an edge incident to a chamber C that has a specific color.
    # Since we process edges and might recolor them, we maintain a dictionary
    # mapping (chamber, color) -> emitter.
    edge_by_C_color = [dict() for _ in range(NC + 1)]
    
    ans = [0] * M
    
    for i in range(M):
        u, v = tests[i]
        
        # Find smallest available color for u
        while color_E[u] == ptr_E[u]:
            ptr_E[u] += 1
        cu = ptr_E[u]
        
        # Find smallest available color for v
        while color_C[v] == ptr_C[v]:
            ptr_C[v] += 1
        cv = ptr_C[v]
        
        if cu == cv:
            c = cu
        else:
            c = cu
            # We need to recolor the chain starting from v
            curr_v = v
            curr_c = cv
            while True:
                # Find the emitter connected to curr_v with color curr_c
                next_u = edge_by_C_color[curr_v].get(curr_c)
                
                # Assign color curr_c to the edge (next_u, curr_v) conceptually
                # by updating the color of curr_v
                color_C[curr_v] = curr_c
                
                # Update the mapping for the new color
                edge_by_C_color[curr_v][curr_c] = next_u
                
                if next_u is None:
                    # Reached the end of the chain
                    break
                
                # The edge (next_u, curr_v) previously had color curr_c for next_u,
                # which must have been equal to color_E[next_u].
                # Now we swap the color, so next_u gets color c.
                color_E[next_u] = c
                
                # Prepare for the next step in the chain
                curr_c, c = c, curr_c
                curr_v = next_u
            
            # After the loop, the last vertex in the chain (which is an emitter) 
            # has been updated. We also need to update the color of the original chamber v.
            # Wait, the loop updates color_C for all chambers in the chain.
            # The original chamber v is the first curr_v, so its color_C is updated inside the loop.
            pass
            
        # Assign color c to the current edge
        ans[i] = c
        color_E[u] = c
        color_C[v] = c
        edge_by_C_color[v][c] = u
        
    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    solve()