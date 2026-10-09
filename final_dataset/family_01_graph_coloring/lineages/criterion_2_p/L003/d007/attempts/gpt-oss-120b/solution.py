import sys

def mat_mul(A, B):
    # 4x4 matrices
    C = [[0]*4 for _ in range(4)]
    for i in range(4):
        for k in range(4):
            aik = A[i][k]
            if aik:
                for j in range(4):
                    C[i][j] += aik * B[k][j]
    return C

def is_zero(M):
    for row in M:
        for v in row:
            if v != 0:
                return False
    return True

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))

    # matrices
    A = [[-8, -5, 4, 5],
         [-10, -6, 5, 6],
         [-16, -10, 8, 10],
         [-10, -6, 5, 6]]
    B = [[6, 1, -2, -2],
         [10, -4, -2, 0],
         [10, 13, -6, -10],
         [13, -12, -1, 4]]

    # which ordered pairs give zero product
    zero = [[False]*2 for _ in range(2)]   # zero[x][y] for mode x+1 , y+1
    mats = [[A, B], [A, B]]
    for x in range(2):
        for y in range(2):
            if is_zero(mat_mul(mats[x][0], mats[y][1])):  # careful indexing
                pass
    # simpler: compute directly
    zero[0][0] = is_zero(mat_mul(A, A))
    zero[0][1] = is_zero(mat_mul(A, B))
    zero[1][0] = is_zero(mat_mul(B, A))
    zero[1][1] = is_zero(mat_mul(B, B))

    # 2-SAT graph
    N = n * 2
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        rg[v].append(u)

    def var(i, val):          # i: 0‑based, val 0 for true(1), 1 for false(2)
        return 2*i + val

    # for each edge add clauses for forbidden ordered pairs
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        for a in (0,1):
            for b in (0,1):
                if zero[a][b]:
                    # (s_u = a+1) AND (s_v = b+1) forbidden
                    # clause: (s_u != a+1) OR (s_v != b+1)
                    # literals: not (u==a)  -> (v != b)
                    #           not (v==b)  -> (u != a)
                    add_imp(var(u, a), var(v, 1-b))
                    add_imp(var(v, b), var(u, 1-a))

    # Kosaraju
    sys.setrecursionlimit(1 << 25)
    visited = [False]*N
    order = []
    def dfs(v):
        visited[v] = True
        for to in g[v]:
            if not visited[to]:
                dfs(to)
        order.append(v)
    for i in range(N):
        if not visited[i]:
            dfs(i)

    comp = [-1]*N
    def rdfs(v, cid):
        comp[v] = cid
        for to in rg[v]:
            if comp[to] == -1:
                rdfs(to, cid)

    cid = 0
    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, cid)
            cid += 1

    # check satisfiability
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return

    # build answer
    ans = []
    for i in range(n):
        # true literal (mode 1) has index 2*i, false (mode 2) 2*i+1
        if comp[2*i] > comp[2*i+1]:
            ans.append('1')
        else:
            ans.append('2')
    print("YES")
    print(' '.join(ans))

if __name__ == "__main__":
    solve()