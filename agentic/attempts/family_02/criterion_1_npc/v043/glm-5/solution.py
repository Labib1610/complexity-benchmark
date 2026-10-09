import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        reqs = []
        for __ in range(3):
            val = int(next(it))
            idx = abs(val) - 1
            pos = 1 if val > 0 else 0
            reqs.append((idx, pos))
        
        for i in range(3):
            idx_i, pos_i = reqs[i]
            # We need to force at least one requirement to be met.
            # Add edge from the negation of req_i to all other reqs.
            # Index in implication graph: idx * 2 + (1 - pos) is the negation's node.
            u = idx_i * 2 + (1 - pos_i)
            for j in range(3):
                if i == j:
                    continue
                idx_j, pos_j = reqs[j]
                v = idx_j * 2 + pos_j
                adj[u].append(v)
    
    N = 2 * n
    visited = [False] * N
    order = []
    
    def dfs(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
        order.append(u)
    
    for i in range(N):
        if not visited[i]:
            dfs(i)
    
    comp_id = [-1] * N
    adj_rev = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            adj_rev[v].append(u)
            
    current_comp = 0
    for u in reversed(order):
        if comp_id[u] == -1:
            stack = [u]
            comp_id[u] = current_comp
            while stack:
                curr = stack.pop()
                for prev in adj_rev[curr]:
                    if comp_id[prev] == -1:
                        comp_id[prev] = current_comp
                        stack.append(prev)
            current_comp += 1
            
    assignment = [0] * n
    possible = True
    
    # Check validity and assign
    for i in range(n):
        node_true = i * 2 + 1
        node_false = i * 2 + 0
        if comp_id[node_true] == comp_id[node_false]:
            possible = False
            break
        # Node with larger component ID gets assigned True
        if comp_id[node_true] > comp_id[node_false]:
            assignment[i] = 1
        else:
            assignment[i] = 0
            
    if not possible:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, assignment)) + "\n")

if __name__ == '__main__':
    solve()