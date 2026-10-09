import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    num_nodes = 2 * n
    head = [-1] * num_nodes
    to = []
    nxt = []
    
    head_rev = [-1] * num_nodes
    to_rev = []
    nxt_rev = []
    
    def add_edge(u, v):
        nxt.append(head[u])
        to.append(v)
        head[u] = len(to) - 1
        
        nxt_rev.append(head_rev[v])
        to_rev.append(u)
        head_rev[v] = len(to_rev) - 1

    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx+1])
        idx += 2
        
        # Literal to node:
        # positive x -> 2*(x-1)
        # negative -x -> 2*(x-1) + 1
        u = 2 * (abs(l1) - 1) + (0 if l1 > 0 else 1)
        v = 2 * (abs(l2) - 1) + (0 if l2 > 0 else 1)
        
        # (l1 or l2) <=> (not l1 => l2) and (not l2 => l1)
        not_u = u ^ 1
        not_v = v ^ 1
        
        add_edge(not_u, v)
        add_edge(not_v, u)
        
    # Kosaraju's Algorithm (iterative)
    # Pass 1: find post-order
    visited = [False] * num_nodes
    order = []
    
    for i in range(num_nodes):
        if not visited[i]:
            stack = [(i, head[i])]
            visited[i] = True
            while stack:
                u, e = stack[-1]
                if e != -1:
                    stack[-1] = (u, nxt[e])
                    v = to[e]
                    if not visited[v]:
                        visited[v] = True
                        stack.append((v, head[v]))
                else:
                    stack.pop()
                    order.append(u)
                    
    # Pass 2: find SCCs
    scc = [-1] * num_nodes
    scc_count = 0
    
    for i in reversed(order):
        if scc[i] == -1:
            stack = [i]
            scc[i] = scc_count
            while stack:
                u = stack.pop()
                e = head_rev[u]
                while e != -1:
                    v = to_rev[e]
                    if scc[v] == -1:
                        scc[v] = scc_count
                        stack.append(v)
                    e = nxt_rev[e]
            scc_count += 1
            
    # Check validity and construct answer
    ans = []
    for i in range(n):
        pos = 2 * i
        neg = 2 * i + 1
        if scc[pos] == scc[neg]:
            print("NO")
            return
        # In Kosaraju, larger scc index means topological sink
        if scc[pos] > scc[neg]:
            ans.append("1")
        else:
            ans.append("0")
            
    print("YES")
    print(" ".join(ans))

if __name__ == '__main__':
    main()