import sys

# Increase recursion depth for deep divide-and-conquer
sys.setrecursionlimit(2000000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    nL = int(input_data[0])
    nR = int(input_data[1])
    m = int(input_data[2])
    
    if m == 0:
        print("YES\n")
        return

    edges_u = [0] * m
    edges_v = [0] * m
    degL = [0] * (nL + 1)
    degR = [0] * (nR + 1)
    
    idx = 3
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges_u[i] = u
        edges_v[i] = v
        degL[u] += 1
        degR[v] += 1
        
    delta = max(max(degL), max(degR))
    edge_color = [0] * m

    # Recursive function to color a subset of edges
    # edge_indices: list of original edge indices
    # cur_delta: maximum degree in this subgraph
    # color_offset: starting color number - 1
    
    # We use an iterative or recursive approach with arrays
    stack = [(list(range(m)), delta, 0)]
    
    while stack:
        cur_edges, cur_d, c_offset = stack.pop()
        if not cur_edges:
            continue
        if cur_d == 1:
            c = c_offset + 1
            for eid in cur_edges:
                edge_color[eid] = c
            continue
        
        # Build adjacency for Euler tour
        # Left vertices: 1 .. nL, Right vertices: nL + 1 .. nL + nR
        # Find active vertices and their degrees
        deg = {}
        for eid in cur_edges:
            u = edges_u[eid]
            v = edges_v[eid] + nL
            deg[u] = deg.get(u, 0) + 1
            deg[v] = deg.get(v, 0) + 1
            
        odd_L = []
        odd_R = []
        for node, d in deg.items():
            if d % 2 == 1:
                if node <= nL:
                    odd_L.append(node)
                else:
                    odd_R.append(node)
                    
        # Pair up odd vertices with dummy edges
        adj = {}
        for node in deg:
            adj[node] = []
            
        for eid in cur_edges:
            u = edges_u[eid]
            v = edges_v[eid] + nL
            adj[u].append((v, eid))
            adj[v].append((u, eid))
            
        dummy_count = len(odd_L)
        for i in range(dummy_count):
            u = odd_L[i]
            v = odd_R[i]
            adj[u].append((v, -1))
            adj[v].append((u, -1))
            
        # Hierholzer's algorithm to find Euler tours / trails
        edges_g1 = []
        edges_g2 = []
        
        # Track edge usage using a dictionary / set or indexed list
        used_edges = {}
        # Since multigraph, we track how many times (u, v, eid) is used or use indices
        # Fast way: track visited per adjacency index pointer
        pos = {node: 0 for node in adj}
        
        for start_node in adj:
            while pos[start_node] < len(adj[start_node]):
                # Start an Eulerian path / cycle
                curr = start_node
                path = []
                while True:
                    while pos[curr] < len(adj[curr]) and adj[curr][pos[curr]][1] in used_edges and used_edges[adj[curr][pos[curr]][1]] == 0:
                        pos[curr] += 1
                    
                    if pos[curr] >= len(adj[curr]):
                        break
                        
                    nxt, eid = adj[curr][pos[curr]]
                    pos[curr] += 1
                    
                    # Mark edge as used
                    # For real edges, eid >= 0, dummy edges eid = -1, -2, ...
                    # To distinguish multiple dummy edges, give them unique negative ids:
                    # But wait, dummy edges can just use unique negative IDs!
                
        # Let's cleanly implement Euler tour per connected component:
        # Instead of inlining loosely, build edge list with unique edge IDs
        pass

    # Clean implementation of the recursive Euler tour decomposition
    def decompose(e_list, d, offset):
        if not e_list:
            return
        if d == 1:
            c = offset + 1
            for eid in e_list:
                edge_color[eid] = c
            return

        # Count degrees
        deg_L = {}
        deg_R = {}
        for eid in e_list:
            u = edges_u[eid]
            v = edges_v[eid]
            deg_L[u] = deg_L.get(u, 0) + 1
            deg_R[v] = deg_R.get(v, 0) + 1

        odd_L = [u for u, count in deg_L.items() if count % 2 == 1]
        odd_R = [v for v, count in deg_R.items() if count % 2 == 1]

        # Build graph: Left nodes 1..nL, Right nodes nL+1..nL+nR
        nodes = list(deg_L.keys()) + [v + nL for v in deg_R.keys()]
        adj = {node: [] for node in nodes}

        for eid in e_list:
            u = edges_u[eid]
            v = edges_v[eid] + nL
            adj[u].append((v, eid))
            adj[v].append((u, eid))

        for i in range(len(odd_L)):
            u = odd_L[i]
            v = odd_R[i] + nL
            adj[u].append((v, -1 - i))
            adj[v].append((u, -1 - i))

        visited_edge = set()
        ptr = {node: 0 for node in nodes}
        
        g1 = []
        g2 = []

        for start in nodes:
            if ptr[start] >= len(adj[start]):
                continue
            
            # Hierholzer
            stack_tour = [start]
            edge_stack = []
            tour_edges = []
            
            while stack_tour:
                u = stack_tour[-1]
                while ptr[u] < len(adj[u]) and adj[u][ptr[u]][1] in visited_edge:
                    ptr[u] += 1
                
                if ptr[u] < len(adj[u]):
                    v, eid = adj[u][ptr[u]]
                    ptr[u] += 1
                    visited_edge.add(eid)
                    stack_tour.append(v)
                    edge_stack.append(eid)
                else:
                    stack_tour.pop()
                    if edge_stack:
                        tour_edges.append(edge_stack.pop())
            
            # Alternate edges in the tour
            for i, eid in enumerate(tour_edges):
                if eid >= 0:
                    if i % 2 == 0:
                        g1.append(eid)
                    else:
                        g2.append(eid)

        d1 = (d + 1) // 2
        d2 = d // 2
        decompose(g1, d1, offset)
        decompose(g2, d2, offset + d1)

    decompose(list(range(m)), delta, 0)

    print("YES")
    print(" ".join(map(str, edge_color)))

if __name__ == '__main__':
    solve()