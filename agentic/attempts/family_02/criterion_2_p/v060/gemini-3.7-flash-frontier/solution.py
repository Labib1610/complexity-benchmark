import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    num_nodes = 2 * n
    adj = [[] for _ in range(num_nodes)]
    rev_adj = [[] for _ in range(num_nodes)]
    
    idx = 2
    for _ in range(m):
        l1 = int(data[idx])
        l2 = int(data[idx+1])
        idx += 2
        
        u = 2 * (l1 - 1) if l1 > 0 else 2 * (-l1 - 1) + 1
        v = 2 * (l2 - 1) if l2 > 0 else 2 * (-l2 - 1) + 1
        
        not_u = u ^ 1
        not_v = v ^ 1
        
        adj[not_u].append(v)
        adj[not_v].append(u)
        rev_adj[v].append(not_u)
        rev_adj[u].append(not_v)
        
    order = []
    visited = [False] * num_nodes
    
    for i in range(num_nodes):
        if not visited[i]:
            stack = [(i, 0)]
            visited[i] = True
            while stack:
                node, edge_idx = stack[-1]
                if edge_idx < len(adj[node]):
                    nxt = adj[node][edge_idx]
                    stack[-1] = (node, edge_idx + 1)
                    if not visited[nxt]:
                        visited[nxt] = True
                        stack.append((nxt, 0))
                else:
                    order.append(node)
                    stack.pop()
                    
    scc = [-1] * num_nodes
    scc_count = 0
    
    for i in reversed(order):
        if scc[i] == -1:
            stack = [i]
            scc[i] = scc_count
            while stack:
                node = stack.pop()
                for nxt in rev_adj[node]:
                    if scc[nxt] == -1:
                        scc[nxt] = scc_count
                        stack.append(nxt)
            scc_count += 1
            
    res = [0] * n
    for i in range(n):
        if scc[2 * i] == scc[2 * i + 1]:
            print("NO")
            return
        if scc[2 * i] > scc[2 * i + 1]:
            res[i] = 1
        else:
            res[i] = 0
            
    print("YES")
    print(*(res))

if __name__ == '__main__':
    main()