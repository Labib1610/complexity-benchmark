import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # 2-SAT: variable i (1-indexed) has two nodes: 2*i for True, 2*i+1 for False
    # We use 0-indexed internally: node 2*(i-1) = True, 2*(i-1)+1 = False
    # But let's use 1-indexed for variables: node 2*i = True, 2*i+1 = False, i in 1..n
    
    size = 2 * n + 2
    adj = [[] for _ in range(size)]
    radj = [[] for _ in range(size)]
    
    def node(var):
        # var > 0 means variable var is True -> node 2*var
        # var < 0 means variable -var is False -> node 2*(-var)+1
        if var > 0:
            return 2 * var
        else:
            return 2 * (-var) + 1
    
    def neg(x):
        return x ^ 1
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        u = node(l1)
        v = node(l2)
        # clause: (l1) OR (l2)
        # implications: not l1 -> l2, not l2 -> l1
        adj[neg(u)].append(v)
        adj[neg(v)].append(u)
        radj[v].append(neg(u))
        radj[u].append(neg(v))
    
    # Kosaraju's SCC
    visited = [False] * size
    order = []
    
    sys.setrecursionlimit(1 << 25)
    
    # Iterative DFS
    for i in range(2, 2 * n + 2):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                v, idx = stack[-1]
                if idx == 0:
                    visited[v] = True
                if idx < len(adj[v]):
                    w = adj[v][idx]
                    stack[-1] = (v, idx + 1)
                    if not visited[w]:
                        stack.append((w, 0))
                else:
                    stack.pop()
                    order.append(v)
    
    visited = [False] * size
    comp = [-1] * size
    
    cid = 0
    for u in reversed(order):
        if not visited[u]:
            stack = [u]
            visited[u] = True
            comp[u] = cid
            while stack:
                v = stack.pop()
                for w in radj[v]:
                    if not visited[w]:
                        visited[w] = True
                        comp[w] = cid
                        stack.append(w)
            cid += 1
    
    assignment = [0] * (n + 1)
    for i in range(1, n + 1):
        t = 2 * i
        f = 2 * i + 1
        if comp[t] == comp[f]:
            print("NO")
            return
        assignment[i] = 1 if comp[t] > comp[f] else 0
    
    print("YES")
    print(' '.join(str(assignment[i]) for i in range(1, n + 1)))

solve()