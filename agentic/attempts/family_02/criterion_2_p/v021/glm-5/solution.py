import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(2 * n + 1)]
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        u = l1
        v = l2
        # Add implication: not u -> v
        adj[-u + n].append(v + n)
        # Add implication: not v -> u
        adj[-v + n].append(u + n)
    
    # Kosaraju's algorithm for SCC
    N = 2 * n + 1
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
                for v in adj[node]:
                    if not visited[v]:
                        stack.append((v, 0))
            else:
                order.append(node)
    
    for i in range(N):
        if i != n and not visited[i]:
            dfs1(i)
    
    # Reverse graph
    rev_adj = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            rev_adj[v].append(u)
    
    comp_id = [-1] * N
    current_id = 0
    
    def dfs2(u, cid):
        stack = [u]
        comp_id[u] = cid
        while stack:
            node = stack.pop()
            for v in rev_adj[node]:
                if comp_id[v] == -1:
                    comp_id[v] = cid
                    stack.append(v)
    
    for u in reversed(order):
        if comp_id[u] == -1:
            dfs2(u, current_id)
            current_id += 1
    
    # Check satisfiability
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        if comp_id[i + n] == comp_id[-i + n]:
            print("NO")
            return
        result[i] = 1 if comp_id[i + n] > comp_id[-i + n] else 0
    
    print("YES")
    print(' '.join(map(str, result[1:])))

if __name__ == '__main__':
    solve()