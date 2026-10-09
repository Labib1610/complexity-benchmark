import sys

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

    deg = [0] * (nL + nR + 1)
    edges = []
    idx = 3
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1]) + nL
        idx += 2
        edges.append((u, v))
        deg[u] += 1
        deg[v] += 1

    max_deg = max(deg)
    
    # adj maps (node, color) -> (neighbor, edge_index)
    # Key as integer: u * (max_deg + 1) + c
    stride = max_deg + 1
    adj = {}
    ans = [0] * m

    for e_idx in range(m):
        u, v = edges[e_idx]

        # Find free color at u
        c_u = 1
        while (u * stride + c_u) in adj:
            c_u += 1

        # Find free color at v
        c_v = 1
        while (v * stride + c_v) in adj:
            c_v += 1

        if c_u != c_v:
            # Collect alternating path starting from v
            path_nodes = [v]
            path_edges = []
            curr = v
            c = c_u
            while (curr * stride + c) in adj:
                nxt, e = adj[curr * stride + c]
                path_nodes.append(nxt)
                path_edges.append(e)
                curr = nxt
                c = c_v if c == c_u else c_u

            # Remove old path edges from adj
            c = c_u
            for i in range(len(path_edges)):
                u_i = path_nodes[i]
                v_i = path_nodes[i + 1]
                del adj[u_i * stride + c]
                del adj[v_i * stride + c]
                c = c_v if c == c_u else c_u

            # Insert path edges back with flipped colors
            c = c_v
            for i in range(len(path_edges)):
                u_i = path_nodes[i]
                v_i = path_nodes[i + 1]
                e = path_edges[i]
                adj[u_i * stride + c] = (v_i, e)
                adj[v_i * stride + c] = (u_i, e)
                ans[e] = c
                c = c_u if c == c_v else c_u

        # Assign color c_u to the new edge (u, v)
        adj[u * stride + c_u] = (v, e_idx)
        adj[v * stride + c_u] = (u, e_idx)
        ans[e_idx] = c_u

    print("YES")
    print(*(ans[i] for i in range(m)))

if __name__ == '__main__':
    solve()