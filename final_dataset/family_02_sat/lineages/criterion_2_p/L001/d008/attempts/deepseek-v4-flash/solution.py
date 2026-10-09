import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n
    g = [[] for _ in range(N)]
    gr = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        gr[v].append(u)

    def node(var, val):
        # var: 1..n, val: True/False
        if val:
            return var - 1
        else:
            return var - 1 + n

    for _ in range(m):
        l1, l2 = map(int, input().split())
        # lit1 = not increment(l1)
        # if l1 > 0: increment = not s[|l1|] => not increment = s[|l1|]
        # if l1 < 0: increment = s[|l1|] => not increment = not s[|l1|]
        if l1 > 0:
            lit1 = node(l1, True)
        else:
            lit1 = node(-l1, False)
        if l2 > 0:
            lit2 = node(l2, True)
        else:
            lit2 = node(-l2, False)
        # clause: lit1 OR lit2
        # ¬lit1 -> lit2
        add_imp(lit1 ^ 1, lit2)
        # ¬lit2 -> lit1
        add_imp(lit2 ^ 1, lit1)

    # Kosaraju
    visited = [False] * N
    order = []
    def dfs1(u):
        visited[u] = True
        for w in g[u]:
            if not visited[w]:
                dfs1(w)
        order.append(u)

    for i in range(N):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * N
    def dfs2(u, cid):
        comp[u] = cid
        for w in gr[u]:
            if comp[w] == -1:
                dfs2(w, cid)

    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1

    for i in range(n):
        if comp[i] == comp[i + n]:
            print("NO")
            return

    # Assign values: comp[x] > comp[x+n] => true
    ans = []
    for i in range(n):
        if comp[i] > comp[i + n]:
            ans.append('1')
        else:
            ans.append('0')
    print("YES")
    print(" ".join(ans))

if __name__ == "__main__":
    solve()