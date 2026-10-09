import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(2 * n)]
    rev_adj = [[] for _ in range(2 * n)]
    
    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx + 1])
        idx += 2
        
        u = 2 * (l1 - 1) if l1 > 0 else 2 * (-l1 - 1) + 1
        v = 2 * (l2 - 1) if l2 > 0 else 2 * (-l2 - 1) + 1
        
        neg_u = u ^ 1
        neg_v = v ^ 1
        
        adj[neg_u].append(v)
        adj[neg_v].append(u)
        rev_adj[v].append(neg_u)
        rev_adj[u].append(neg_v)
        
    num_nodes = 2 * n
    visited = [False] * num_nodes
    order = []
    edge_idx = [0] * num_nodes
    
    for start in range(num_nodes):
        if visited[start]:
            continue
        visited[start] = True
        stack = [start]
        while stack:
            u = stack[-1]
            if edge_idx[u] < len(adj[u]):
                v = adj[u][edge_idx[u]]
                edge_idx[u] += 1
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
            else:
                order.append(stack.pop())
                
    scc = [-1] * num_nodes
    scc_cnt = 0
    for start in reversed(order):
        if scc[start] != -1:
            continue
        scc[start] = scc_cnt
        stack = [start]
        while stack:
            u = stack.pop()
            for v in rev_adj[u]:
                if scc[v] == -1:
                    scc[v] = scc_cnt
                    stack.append(v)
        scc_cnt += 1
        
    ans = [0] * n
    for i in range(n):
        pos = 2 * i
        neg = 2 * i + 1
        if scc[pos] == scc[neg]:
            print("NO")
            return
        ans[i] = 1 if scc[pos] > scc[neg] else 0
        
    print("YES")
    print(*(ans))

if __name__ == '__main__':
    solve()