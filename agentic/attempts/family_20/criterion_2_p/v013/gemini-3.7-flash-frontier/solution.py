import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    nA = int(input_data[0])
    nB = int(input_data[1])
    m = int(input_data[2])
    
    if m == 0:
        print("YES")
        print()
        return

    # Edges: u in 0..nA-1, v in nA..nA+nB-1
    orig_u = [0] * m
    orig_v = [0] * m
    idx = 3
    for i in range(m):
        orig_u[i] = int(input_data[idx]) - 1
        orig_v[i] = int(input_data[idx + 1]) - 1 + nA
        idx += 2

    # Calculate degrees to find max degree T
    degA = [0] * nA
    degB = [0] * nB
    for i in range(m):
        degA[orig_u[i]] += 1
        degB[orig_v[i] - nA] += 1
    
    T = max(max(degA, default=0), max(degB, default=0))
    if T == 0:
        print("YES")
        print()
        return

    ans = [0] * m

    # Subproblems: (list of original edge indices, max_degree delta, color_offset)
    stack = [ (list(range(m)), T, 0) ]

    while stack:
        edges, delta, color_offset = stack.pop()
        if not edges:
            continue
        if delta <= 1:
            for e in edges:
                ans[e] = color_offset + 1
            continue
        
        # Build local graph
        # Collect degrees for vertices present in this subproblem
        deg = {}
        for e in edges:
            u = orig_u[e]
            v = orig_v[e]
            deg[u] = deg.get(u, 0) + 1
            deg[v] = deg.get(v, 0) + 1
        
        odd_A = []
        odd_B = []
        for node, d in deg.items():
            if d % 2 != 0:
                if node < nA:
                    odd_A.append(node)
                else:
                    odd_B.append(node)
        
        # Balance odd vertices between A and B
        dummy_node_id = nA + nB
        if len(odd_A) > len(odd_B):
            diff = len(odd_A) - len(odd_B)
            for _ in range(diff):
                odd_B.append(dummy_node_id)
                dummy_node_id += 1
        elif len(odd_B) > len(odd_A):
            diff = len(odd_B) - len(odd_A)
            for _ in range(diff):
                odd_A.append(dummy_node_id)
                dummy_node_id += 1
        
        # Build adjacency list: adj[u] = list of (v, edge_idx, edge_internal_id)
        adj = {}
        total_edges = len(edges) + len(odd_A)
        
        for i, e in enumerate(edges):
            u = orig_u[e]
            v = orig_v[e]
            if u not in adj: adj[u] = []
            if v not in adj: adj[v] = []
            adj[u].append((v, e, i))
            adj[v].append((u, e, i))
            
        for i in range(len(odd_A)):
            u = odd_A[i]
            v = odd_B[i]
            if u not in adj: adj[u] = []
            if v not in adj: adj[v] = []
            e_id = len(edges) + i
            adj[u].append((v, -1, e_id))
            adj[v].append((u, -1, e_id))
            
        used = [False] * total_edges
        head = {node: 0 for node in adj}
        
        E1 = []
        E2 = []
        
        for start_node in adj:
            if head[start_node] < len(adj[start_node]):
                # Hierholzer's algorithm
                st = [start_node]
                edge_st = []
                flag = 0
                
                while st:
                    u = st[-1]
                    neighbors = adj[u]
                    idx_h = head[u]
                    
                    found = False
                    while idx_h < len(neighbors):
                        v, orig_e, int_e = neighbors[idx_h]
                        idx_h += 1
                        if not used[int_e]:
                            used[int_e] = True
                            head[u] = idx_h
                            st.append(v)
                            edge_st.append(orig_e)
                            found = True
                            break
                    
                    if not found:
                        head[u] = idx_h
                        st.pop()
                        if edge_st:
                            e_popped = edge_st.pop()
                            if e_popped != -1:
                                if flag == 0:
                                    E1.append(e_popped)
                                else:
                                    E2.append(e_popped)
                            flag ^= 1
                            
        d1 = (delta + 1) // 2
        d2 = delta // 2
        stack.append((E2, d2, color_offset + d1))
        stack.append((E1, d1, color_offset))

    print("YES")
    print(*(ans[i] for i in range(m)))

if __name__ == '__main__':
    solve()