import sys

# Increase recursion depth
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
        
    for i in range(1, n + 1):
        if len(adj[i]) != 3:
            print("NO")
            return

    edge_color = [0] * m
    vertex_mask = [0] * (n + 1)
    
    # Pre-calculate possible colors for bitmask:
    # color 1 -> mask 1
    # color 2 -> mask 2
    # color 3 -> mask 4
    c_to_mask = [0, 1, 2, 4]
    
    def get_avail(e):
        u, v = edges[e]
        used = vertex_mask[u] | vertex_mask[v]
        avail = []
        if not (used & 1): avail.append(1)
        if not (used & 2): avail.append(2)
        if not (used & 4): avail.append(3)
        return avail

    # Find connected components
    visited = [False] * (n + 1)
    components = []
    for i in range(1, n + 1):
        if not visited[i]:
            comp_nodes = []
            q = [i]
            visited[i] = True
            for node in q:
                comp_nodes.append(node)
                for e_idx in adj[node]:
                    u, v = edges[e_idx]
                    nxt = v if u == node else u
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
            components.append(comp_nodes)

    def backtrack(comp_edges_set):
        assigned_history = []
        
        while True:
            forced_found = False
            best_edge = -1
            min_avail_count = 4
            best_avails = None
            
            for e in comp_edges_set:
                if edge_color[e] == 0:
                    avails = get_avail(e)
                    cnt = len(avails)
                    if cnt == 0:
                        # Conflict
                        for ae in reversed(assigned_history):
                            c = edge_color[ae]
                            edge_color[ae] = 0
                            u, v = edges[ae]
                            m_val = c_to_mask[c]
                            vertex_mask[u] ^= m_val
                            vertex_mask[v] ^= m_val
                        return False
                    if cnt == 1:
                        # Unit propagate
                        c = avails[0]
                        edge_color[e] = c
                        u, v = edges[e]
                        m_val = c_to_mask[c]
                        vertex_mask[u] |= m_val
                        vertex_mask[v] |= m_val
                        assigned_history.append(e)
                        forced_found = True
                        break
                    if cnt < min_avail_count:
                        min_avail_count = cnt
                        best_edge = e
                        best_avails = avails
                        
            if forced_found:
                continue
            
            if best_edge == -1:
                # All edges colored successfully
                return True
            
            # Need to branch on best_edge
            for c in best_avails:
                edge_color[best_edge] = c
                u, v = edges[best_edge]
                m_val = c_to_mask[c]
                vertex_mask[u] |= m_val
                vertex_mask[v] |= m_val
                
                if backtrack(comp_edges_set):
                    return True
                
                edge_color[best_edge] = 0
                vertex_mask[u] ^= m_val
                vertex_mask[v] ^= m_val
            
            # If all branches failed, unroll assigned_history
            for ae in reversed(assigned_history):
                c = edge_color[ae]
                edge_color[ae] = 0
                u, v = edges[ae]
                m_val = c_to_mask[c]
                vertex_mask[u] ^= m_val
                vertex_mask[v] ^= m_val
            return False

    for comp in components:
        # Collect edges in this component
        comp_edges = set()
        for u in comp:
            for e in adj[u]:
                comp_edges.add(e)
        
        # Break symmetry at the first vertex
        v0 = comp[0]
        e0, e1, e2 = adj[v0]
        
        # Assign e0 -> 1, e1 -> 2, e2 -> 3
        edge_color[e0] = 1
        edge_color[e1] = 2
        edge_color[e2] = 3
        
        for c, e in [(1, e0), (2, e1), (3, e2)]:
            u, v = edges[e]
            m_val = c_to_mask[c]
            vertex_mask[u] |= m_val
            vertex_mask[v] |= m_val
            
        if not backtrack(comp_edges):
            print("NO")
            return

    print("YES")
    print(*(edge_color[i] for i in range(m)))

if __name__ == '__main__':
    solve()