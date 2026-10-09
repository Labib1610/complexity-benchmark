import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(2 * n)]
    
    # Helper to get node indices
    # Variable x (1 to n):
    #   2*(x-1)     -> x is True  (x > 0 in clause)
    #   2*(x-1) + 1 -> x is False (x < 0 in clause)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        
        # Clause (u OR v)
        # Map u to its corresponding literal node and negation
        if u > 0:
            u_node = 2 * (u - 1)
            u_neg = 2 * (u - 1) + 1
        else:
            u_node = 2 * (-u - 1) + 1
            u_neg = 2 * (-u - 1)
            
        if v > 0:
            v_node = 2 * (v - 1)
            v_neg = 2 * (v - 1) + 1
        else:
            v_node = 2 * (-v - 1) + 1
            v_neg = 2 * (-v - 1)
            
        # Add implications: not u -> v, not v -> u
        adj[u_neg].append(v_node)
        adj[v_neg].append(u_node)
        
    # Kosaraju's algorithm for SCC
    N = 2 * n
    visited = [False] * N
    order = []
    
    for i in range(N):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                node, idx = stack[-1]
                if not visited[node]:
                    visited[node] = True
                while idx < len(adj[node]) and visited[adj[node][idx]]:
                    idx += 1
                if idx < len(adj[node]):
                    stack[-1] = (node, idx + 1)
                    stack.append((adj[node][idx], 0))
                else:
                    stack.pop()
                    order.append(node)
    
    # Reverse graph
    rev_adj = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            rev_adj[v].append(u)
    
    visited = [False] * N
    comp_id = [-1] * N
    cid = 0
    
    for node in reversed(order):
        if not visited[node]:
            stack = [node]
            visited[node] = True
            comp_id[node] = cid
            while stack:
                cur = stack.pop()
                for nxt in rev_adj[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        comp_id[nxt] = cid
                        stack.append(nxt)
            cid += 1
    
    # Check validity
    for i in range(n):
        if comp_id[2 * i] == comp_id[2 * i + 1]:
            print("NO")
            return
    
    # Assign values
    result = [0] * n
    for i in range(n):
        # If node for True is in higher component than node for False, set True
        # Else set False
        if comp_id[2 * i] > comp_id[2 * i + 1]:
            result[i] = 1
        else:
            result[i] = 0
    
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    solve()