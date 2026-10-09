import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # 2-SAT: each sensor x has two nodes: 2*x (false/BYPASSED) and 2*x+1 (true/OPERATED)
    # Input: positive x means OPERATED (true), negative -x means BYPASSED (false)
    # Clause: (l1 OR l2) must be true
    # If l > 0: corresponds to sensor l being OPERATED -> node 2*l+1
    # If l < 0: corresponds to sensor -l being BYPASSED -> node 2*(-l)
    
    N = 2 * (n + 1)
    adj = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]
    
    def get_node(val):
        x = abs(val)
        if val > 0:
            return 2 * x + 1  # OPERATED
        else:
            return 2 * x      # BYPASSED
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        u = get_node(l1)
        v = get_node(l2)
        # Add implication: not u -> v
        adj[u ^ 1].append(v)
        radj[v].append(u ^ 1)
        # Add implication: not v -> u
        adj[v ^ 1].append(u)
        radj[u].append(v ^ 1)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * N
    order = []
    
    def dfs1(u):
        stack = [u]
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            # Push children in reverse order to process in correct order
            for v in adj[node]:
                if not visited[v]:
                    stack.append(v)
            order.append(node)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    comp = [-1] * N
    current_comp = 0
    
    def dfs2(u, label):
        stack = [u]
        while stack:
            node = stack.pop()
            if comp[node] != -1:
                continue
            comp[node] = label
            for v in radj[node]:
                if comp[v] == -1:
                    stack.append(v)
    
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, current_comp)
            current_comp += 1
    
    # Check for contradiction and build assignment
    assignment = [0] * (n + 1)
    for x in range(1, n + 1):
        if comp[2 * x] == comp[2 * x + 1]:
            print("NO")
            return
        assignment[x] = 1 if comp[2 * x + 1] > comp[2 * x] else 0
    
    print("YES")
    print(' '.join(map(str, assignment[1:])))

if __name__ == "__main__":
    solve()