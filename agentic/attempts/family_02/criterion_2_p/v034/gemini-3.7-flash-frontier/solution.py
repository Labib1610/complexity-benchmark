import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    # Literals:
    # For toggle i (1-indexed):
    # positive i -> 2 * (i - 1)
    # negative i -> 2 * (i - 1) + 1
    # Negation of literal u is u ^ 1
    
    num_nodes = 2 * n
    adj = [[] for _ in range(num_nodes)]
    rev_adj = [[] for _ in range(num_nodes)]
    
    idx = 2
    for _ in range(m):
        u_raw = int(data[idx])
        v_raw = int(data[idx+1])
        idx += 2
        
        u = (abs(u_raw) - 1) * 2 if u_raw > 0 else (abs(u_raw) - 1) * 2 + 1
        v = (abs(v_raw) - 1) * 2 if v_raw > 0 else (abs(v_raw) - 1) * 2 + 1
        
        # Clause (u or v) -> (~u -> v) and (~v -> u)
        not_u = u ^ 1
        not_v = v ^ 1
        
        adj[not_u].append(v)
        adj[not_v].append(u)
        rev_adj[v].append(not_u)
        rev_adj[u].append(not_v)
        
    # Kosaraju's Algorithm (Iterative)
    order = []
    visited = [False] * num_nodes
    
    for i in range(num_nodes):
        if not visited[i]:
            stack = [i]
            edge_idx = [0] * num_nodes
            visited[i] = True
            while stack:
                curr = stack[-1]
                if edge_idx[curr] < len(adj[curr]):
                    nxt = adj[curr][edge_idx[curr]]
                    edge_idx[curr] += 1
                    if not visited[nxt]:
                        visited[nxt] = True
                        stack.append(nxt)
                else:
                    order.append(curr)
                    stack.pop()
                    
    scc = [-1] * num_nodes
    scc_count = 0
    
    for node in reversed(order):
        if scc[node] == -1:
            # BFS or DFS on transposed graph
            q = [node]
            scc[node] = scc_count
            head = 0
            while head < len(q):
                curr = q[head]
                head += 1
                for prev in rev_adj[curr]:
                    if scc[prev] == -1:
                        scc[prev] = scc_count
                        q.append(prev)
            scc_count += 1
            
    # Check satisfiability
    res = []
    for i in range(n):
        pos = 2 * i
        neg = 2 * i + 1
        if scc[pos] == scc[neg]:
            print("NO")
            return
        # If scc[pos] < scc[neg], pos is topologically after neg in the original implication graph
        # because components are numbered in topological order of SCCs via Kosaraju
        if scc[pos] < scc[neg]:
            res.append("1")
        else:
            res.append("0")
            
    print("YES")
    print(" ".join(res))

if __name__ == '__main__':
    main()