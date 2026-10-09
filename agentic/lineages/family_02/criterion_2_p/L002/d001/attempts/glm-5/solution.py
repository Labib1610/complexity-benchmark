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
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        
        u = abs(l1) - 1
        v = abs(l2) - 1
        
        # Determine the states that trigger the interlock
        # If l > 0, reference is mode 1, so trigger state is mode 0 (index 0)
        # If l < 0, reference is mode 0, so trigger state is mode 1 (index 1)
        su = 0 if l1 > 0 else 1
        sv = 0 if l2 > 0 else 1
        
        # The forbidden combination is (u in mode su) AND (v in mode sv).
        # We add implications: (u in su) -> (v not in sv)
        # and (v in sv) -> (u not in su).
        
        # Node indices: machine i, mode 0 is 2*i, mode 1 is 2*i + 1
        u_su = 2 * u + su
        v_not_sv = 2 * v + (1 - sv)
        adj[u_su].append(v_not_sv)
        
        v_sv = 2 * v + sv
        u_not_su = 2 * u + (1 - su)
        adj[v_sv].append(u_not_su)
    
    # Kosaraju's algorithm for SCC
    N = 2 * n
    visited = [False] * N
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack.pop()
            if idx == 0:
                if visited[node]:
                    continue
                visited[node] = True
                stack.append((node, 1))
                for i in range(len(adj[node]) - 1, -1, -1):
                    v = adj[node][i]
                    if not visited[v]:
                        stack.append((v, 0))
            else:
                order.append(node)

    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    # Build reverse graph
    rev_adj = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            rev_adj[v].append(u)
    
    comp_id = [-1] * N
    current_id = 0
    
    def dfs2(u, cid):
        stack = [u]
        while stack:
            node = stack.pop()
            if comp_id[node] != -1:
                continue
            comp_id[node] = cid
            for v in rev_adj[node]:
                if comp_id[v] == -1:
                    stack.append(v)
    
    for u in reversed(order):
        if comp_id[u] == -1:
            dfs2(u, current_id)
            current_id += 1
    
    # Check for unsatisfiability
    assignment = [0] * n
    possible = True
    
    for i in range(n):
        node0 = 2 * i
        node1 = 2 * i + 1
        if comp_id[node0] == comp_id[node1]:
            possible = False
            break
        # If comp_id is larger, it appears earlier in topological order
        # We want to assign True to the node that appears earlier
        if comp_id[node0] > comp_id[node1]:
            assignment[i] = 0
        else:
            assignment[i] = 1
    
    if not possible:
        print("NO")
    else:
        print("YES")
        print(*(assignment))

if __name__ == "__main__":
    solve()