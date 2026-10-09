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
    
    def get_node(c):
        idx = abs(c) - 1
        val = 1 if c > 0 else 0
        return 2 * idx + val

    for _ in range(m):
        c1 = int(next(it))
        c2 = int(next(it))
        u = get_node(c1)
        v = get_node(c2)
        adj[u ^ 1].append(v)
        adj[v ^ 1].append(u)

    N = 2 * n
    ids = [0] * N
    low = [0] * N
    on_stack = [False] * N
    stack = []
    current_id = 0
    scc_id = [0] * N
    scc_count = 0

    def dfs(u):
        nonlocal current_id, scc_count
        current_id += 1
        ids[u] = low[u] = current_id
        stack.append(u)
        on_stack[u] = True
        
        for v in adj[u]:
            if ids[v] == 0:
                dfs(v)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:
                low[u] = min(low[u], ids[v])
        
        if ids[u] == low[u]:
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc_id[w] = scc_count
                if w == u:
                    break
            scc_count += 1

    for i in range(N):
        if ids[i] == 0:
            dfs(i)
            
    assignment = [-1] * n
    possible = True
    
    for i in range(n):
        if scc_id[2*i] == scc_id[2*i+1]:
            possible = False
            break
        assignment[i] = 1 if scc_id[2*i] > scc_id[2*i+1] else 0

    if not possible:
        print("NO")
    else:
        print("YES")
        print(*(assignment))

if __name__ == "__main__":
    solve()