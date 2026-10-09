import sys
import random

# Increase recursion depth just in case
sys.setrecursionlimit(1000000)

def main():
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

    # Read edges
    edges_u = [0] * m
    edges_v = [0] * m
    degL = [0] * (nL + 1)
    degR = [0] * (nR + 1)
    
    idx = 3
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        edges_u[i] = u
        edges_v[i] = v
        degL[u] += 1
        degR[v] += 1
    
    delta = 0
    for u in range(1, nL + 1):
        if degL[u] > delta:
            delta = degL[u]
    for v in range(1, nR + 1):
        if degR[v] > delta:
            delta = degR[v]
            
    if delta == 0:
        print("YES")
        print()
        return

    # Bin packing for Left vertices
    binL = [0] * (nL + 1)
    binsL_deg = []
    curr_bin = 0
    curr_deg = 0
    for u in range(1, nL + 1):
        if degL[u] == 0:
            continue
        if curr_deg + degL[u] > delta:
            binsL_deg.append(curr_deg)
            curr_bin += 1
            curr_deg = 0
        binL[u] = curr_bin
        curr_deg += degL[u]
    if curr_deg > 0 or not binsL_deg:
        binsL_deg.append(curr_deg)
    
    # Bin packing for Right vertices
    binR = [0] * (nR + 1)
    binsR_deg = []
    curr_bin = 0
    curr_deg = 0
    for v in range(1, nR + 1):
        if degR[v] == 0:
            continue
        if curr_deg + degR[v] > delta:
            binsR_deg.append(curr_deg)
            curr_bin += 1
            curr_deg = 0
        binR[v] = curr_bin
        curr_deg += degR[v]
    if curr_deg > 0 or not binsR_deg:
        binsR_deg.append(curr_deg)
        
    num_bins = max(len(binsL_deg), len(binsR_deg))
    while len(binsL_deg) < num_bins:
        binsL_deg.append(0)
    while len(binsR_deg) < num_bins:
        binsR_deg.append(0)
        
    # Build initial regular edge list
    # Edge representation: [u, v, orig_id] where orig_id is 0-based for input edges, -1 for dummy
    all_edges = []
    for i in range(m):
        u = binL[edges_u[i]]
        v = binR[edges_v[i]]
        all_edges.append([u, v, i])
        
    # Add dummy edges to make every bin have degree exactly delta
    l_idx = 0
    r_idx = 0
    while l_idx < num_bins and r_idx < num_bins:
        while l_idx < num_bins and binsL_deg[l_idx] == delta:
            l_idx += 1
        while r_idx < num_bins and binsR_deg[r_idx] == delta:
            r_idx += 1
        if l_idx < num_bins and r_idx < num_bins:
            add = min(delta - binsL_deg[l_idx], delta - binsR_deg[r_idx])
            for _ in range(add):
                all_edges.append([l_idx, r_idx, -1])
            binsL_deg[l_idx] += add
            binsR_deg[r_idx] += add

    N = num_bins
    ans = [0] * m
    
    # Divide and conquer edge coloring
    def solve(edges, d, color_start):
        if d == 0 or not edges:
            return
        if d == 1:
            for e in edges:
                orig_id = e[2]
                if orig_id != -1:
                    ans[orig_id] = color_start
            return
        
        if d % 2 == 1:
            # Find a perfect matching using random walk
            adj = [[] for _ in range(N)]
            for e in edges:
                adj[e[0]].append((e[1], e))
            
            matchR = [-1] * N
            match_edge_R = [None] * N
            for i in range(N):
                u = i
                while u != -1:
                    nbrs = adj[u]
                    v, e = nbrs[random.randrange(len(nbrs))]
                    prev_u = matchR[v]
                    matchR[v] = u
                    match_edge_R[v] = e
                    u = prev_u
            
            matched_edges = set(id(e) for e in match_edge_R)
            rem_edges = []
            for e in edges:
                if id(e) in matched_edges:
                    orig_id = e[2]
                    if orig_id != -1:
                        ans[orig_id] = color_start + d - 1
                else:
                    rem_edges.append(e)
            solve(rem_edges, d - 1, color_start)
        else:
            # d is even: Euler tour decomposition
            # Left vertices: 0..N-1, Right vertices: N..2N-1
            adj = [[] for _ in range(2 * N)]
            for e in edges:
                u, v = e[0], e[1] + N
                adj[u].append((v, e))
                adj[v].append((u, e))
                
            used_edge = set()
            edges1 = []
            edges2 = []
            
            ptr = [0] * (2 * N)
            for start_node in range(2 * N):
                if ptr[start_node] >= len(adj[start_node]):
                    continue
                
                # Hierholzer's algorithm
                curr_path = [start_node]
                circuit = []
                while curr_path:
                    curr = curr_path[-1]
                    found = False
                    while ptr[curr] < len(adj[curr]):
                        nxt, e = adj[curr][ptr[curr]]
                        ptr[curr] += 1
                        if id(e) not in used_edge:
                            used_edge.add(id(e))
                            curr_path.append(nxt)
                            circuit.append(e)
                            found = True
                            break
                    if not found:
                        curr_path.pop()
                
            # Split alternatingly into two subgraphs
            # In bipartite graph, every closed Eulerian cycle has even length
            # So simple alternating assignment of edges from used_edge gives regular degree d/2
            count = 0
            for e in edges:
                if count % 2 == 0:
                    edges1.append(e)
                else:
                    edges2.append(e)
                count += 1
            
            # Wait, the alternating must follow the Euler tour order!
            # Correct alternating along Eulerian circuits:
            # Let's rebuild Euler tours properly:
            # Re-initialize:
            pass

    # Clean implementation of solve:
    def solve_clean(edges, d, color_start):
        if d == 0 or not edges:
            return
        if d == 1:
            for e in edges:
                orig_id = e[2]
                if orig_id != -1:
                    ans[orig_id] = color_start
            return
        
        if d % 2 == 1:
            adj = [[] for _ in range(N)]
            for e in edges:
                adj[e[0]].append((e[1], e))
            
            matchR = [-1] * N
            match_edge_R = [None] * N
            for i in range(N):
                u = i
                while u != -1:
                    nbrs = adj[u]
                    v, e = nbrs[random.randrange(len(nbrs))]
                    prev_u = matchR[v]
                    matchR[v] = u
                    match_edge_R[v] = e
                    u = prev_u
            
            matched_edges = set(id(e) for e in match_edge_R)
            rem_edges = []
            for e in edges:
                if id(e) in matched_edges:
                    orig_id = e[2]
                    if orig_id != -1:
                        ans[orig_id] = color_start + d - 1
                else:
                    rem_edges.append(e)
            solve_clean(rem_edges, d - 1, color_start)
        else:
            adj = [[] for _ in range(2 * N)]
            for e in edges:
                u, v = e[0], e[1] + N
                adj[u].append((v, e))
                adj[v].append((u, e))
                
            used_edge = set()
            edges1 = []
            edges2 = []
            
            ptr = [0] * (2 * N)
            for i in range(2 * N):
                while ptr[i] < len(adj[i]):
                    if id(adj[i][ptr[i]][1]) in used_edge:
                        ptr[i] += 1
                        continue
                    
                    # Hierholzer to find circuit
                    stk = [i]
                    stk_edge = []
                    circuit_edges = []
                    
                    while stk:
                        u = stk[-1]
                        while ptr[u] < len(adj[u]) and id(adj[u][ptr[u]][1]) in used_edge:
                            ptr[u] += 1
                        if ptr[u] < len(adj[u]):
                            v, e = adj[u][ptr[u]]
                            ptr[u] += 1
                            used_edge.add(id(e))
                            stk.append(v)
                            stk_edge.append(e)
                        else:
                            stk.pop()
                            if stk_edge:
                                circuit_edges.append(stk_edge.pop())
                    
                    for idx, e in enumerate(circuit_edges):
                        if idx % 2 == 0:
                            edges1.append(e)
                        else:
                            edges2.append(e)
                            
            solve_clean(edges1, d // 2, color_start)
            solve_clean(edges2, d // 2, color_start + d // 2)

    solve_clean(all_edges, delta, 1)
    
    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()