import sys
sys.setrecursionlimit(1 << 25)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        
        u = abs(l1) - 1
        v = abs(l2) - 1
        
        # Determine node indices for the literals
        # If l1 > 0 (valve u is 1), then literal is u, negation is u+n
        # If l1 < 0 (valve u is 0), then literal is u+n, negation is u
        if l1 > 0:
            nu, nnu = u, u + n
        else:
            nu, nnu = u + n, u
            
        if l2 > 0:
            nv, nnv = v, v + n
        else:
            nv, nnv = v + n, v
            
        # Add implications: not l1 -> l2 and not l2 -> l1
        adj[nnu].append(nv)
        adj[nnv].append(nu)
        
    # Kosaraju's algorithm for SCC
    order = []
    visited = [False] * (2 * n)
    
    for i in range(2 * n):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                node, state = stack.pop()
                if state == 0:
                    if visited[node]:
                        continue
                    visited[node] = True
                    stack.append((node, 1))
                    for nei in adj[node]:
                        if not visited[nei]:
                            stack.append((nei, 0))
                else:
                    order.append(node)
    
    comp_id = [-1] * (2 * n)
    rev_adj = [[] for _ in range(2 * n)]
    for u in range(2 * n):
        for v in adj[u]:
            rev_adj[v].append(u)
            
    cid = 0
    for u in reversed(order):
        if comp_id[u] == -1:
            stack = [u]
            comp_id[u] = cid
            while stack:
                node = stack.pop()
                for nei in rev_adj[node]:
                    if comp_id[nei] == -1:
                        comp_id[nei] = cid
                        stack.append(nei)
            cid += 1
            
    assignment = [0] * n
    possible = True
    
    for i in range(n):
        if comp_id[i] == comp_id[i + n]:
            possible = False
            break
        assignment[i] = 1 if comp_id[i] < comp_id[i + n] else 0
        
    if not possible:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    solve()