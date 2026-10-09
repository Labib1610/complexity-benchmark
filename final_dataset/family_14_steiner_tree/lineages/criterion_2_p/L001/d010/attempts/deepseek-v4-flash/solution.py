import sys
sys.setrecursionlimit(300000)
INF = 10**18

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = [False]*(n+1)
    for x in map(int, input().split()):
        critical[x] = True
    adj = [[] for _ in range(n+1)]
    deg = [0]*(n+1)
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        deg[u] += 1
        deg[v] += 1
    
    parent = [0]*(n+1)
    order = [1]
    parent[1] = -1
    for u in order:
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                order.append(v)
    
    dp0 = [0]*(n+1)
    dp1 = [0]*(n+1)
    
    for u in reversed(order):
        c0 = 0
        c1 = 0
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            if u == 0:  # not possible here, we compute later
                pass
            # We'll compute based on u's state
        # Actually we need to compute both states
        # Let's compute dp0[u], dp1[u]
        sum0 = 0
        sum1 = 0
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            # child's dp
            child0 = dp0[v]
            child1 = dp1[v]
            # if u=0
            if deg[v] == 1:
                # leaf child must be 1
                sum0 += child1
            else:
                sum0 += min(child0, child1)
            # if u=1
            sum1 += min(child0, child1 + w)
        # enforce constraints
        if critical[u] or deg[u] > 2:
            dp0[u] = INF
        else:
            dp0[u] = sum0
        dp1[u] = sum1
    
    # root is 1
    ans = min(dp0[1], dp1[1])
    # But if root is leaf and dp0 chosen, invalid because no parent to make edge different
    if deg[1] == 1:
        ans = dp1[1]
    print(ans)

if __name__ == "__main__":
    solve()