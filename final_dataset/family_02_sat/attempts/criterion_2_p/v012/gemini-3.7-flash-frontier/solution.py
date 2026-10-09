import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # 2*n vertices:
    # 2*i for x_{i+1}
    # 2*i + 1 for not x_{i+1}
    
    num_vars = 2 * n
    adj = [[] for _ in range(num_vars)]
    radj = [[] for _ in range(num_vars)]
    
    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx+1])
        idx += 2
        
        # Convert l1 to vertex
        if l1 > 0:
            v1 = 2 * (l1 - 1)
            nv1 = 2 * (l1 - 1) + 1
        else:
            v1 = 2 * (-l1 - 1) + 1
            nv1 = 2 * (-l1 - 1)
            
        if l2 > 0:
            v2 = 2 * (l2 - 1)
            nv2 = 2 * (l2 - 1) + 1
        else:
            v2 = 2 * (-l2 - 1) + 1
            nv2 = 2 * (-l2 - 1)
            
        # (l1 or l2) is equivalent to:
        # not l1 -> l2
        # not l2 -> l1
        adj[nv1].append(v2)
        radj[v2].append(nv1)
        
        adj[nv2].append(v1)
        radj[v1].append(nv2)
        
    # Kosaraju's Algorithm (iterative)
    order = []
    visited = [False] * num_vars
    
    for i in range(num_vars):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            it = [0] * num_vars
            
            while stack:
                u = stack[-1]
                neighbors = adj[u]
                if it[u] < len(neighbors):
                    v = neighbors[it[u]]
                    it[u] += 1
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
                else:
                    order.append(u)
                    stack.pop()
                    
    scc = [-1] * num_vars
    scc_count = 0
    
    for u in reversed(order):
        if scc[u] == -1:
            stack = [u]
            scc[u] = scc_count
            while stack:
                curr = stack.pop()
                for v in radj[curr]:
                    if scc[v] == -1:
                        scc[v] = scc_count
                        stack.append(v)
            scc_count += 1
            
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