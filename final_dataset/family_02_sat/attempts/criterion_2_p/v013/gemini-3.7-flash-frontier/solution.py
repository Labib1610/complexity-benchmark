import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(2 * n)]
    radj = [[] for _ in range(2 * n)]
    
    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx + 1])
        idx += 2
        
        u = 2 * (l1 - 1) if l1 > 0 else 2 * (-l1 - 1) + 1
        v = 2 * (l2 - 1) if l2 > 0 else 2 * (-l2 - 1) + 1
        
        # not u -> v
        adj[u ^ 1].append(v)
        radj[v].append(u ^ 1)
        # not v -> u
        adj[v ^ 1].append(u)
        radj[u].append(v ^ 1)
        
    # Iterative Kosaraju's algorithm
    order = []
    visited = [False] * (2 * n)
    for i in range(2 * n):
        if not visited[i]:
            st = [(i, 0)]
            visited[i] = True
            while st:
                u, edge_idx = st[-1]
                if edge_idx < len(adj[u]):
                    st[-1] = (u, edge_idx + 1)
                    nxt = adj[u][edge_idx]
                    if not visited[nxt]:
                        visited[nxt] = True
                        st.append((nxt, 0))
                else:
                    order.append(u)
                    st.pop()
                    
    scc = [-1] * (2 * n)
    scc_cnt = 0
    for u in reversed(order):
        if scc[u] == -1:
            st = [u]
            scc[u] = scc_cnt
            while st:
                curr = st.pop()
                for nxt in radj[curr]:
                    if scc[nxt] == -1:
                        scc[nxt] = scc_cnt
                        st.append(nxt)
            scc_cnt += 1
            
    res = []
    for i in range(n):
        if scc[2 * i] == scc[2 * i + 1]:
            print("NO")
            return
        if scc[2 * i] > scc[2 * i + 1]:
            res.append(1)
        else:
            res.append(0)
            
    print("YES")
    print(*(res))

if __name__ == '__main__':
    solve()