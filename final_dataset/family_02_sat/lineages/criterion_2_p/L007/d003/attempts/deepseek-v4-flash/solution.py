import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())

# 2-SAT: variable i (0-indexed) -> node 2*i (false), 2*i+1 (true)
N = 2 * n
g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

def add_imp(u, v):
    g[u].append(v)
    gr[v].append(u)

def add_clause(a, b):
    # a or b
    # (not a -> b), (not b -> a)
    add_imp(a ^ 1, b)
    add_imp(b ^ 1, a)

for _ in range(m):
    l1, l2 = map(int, input().split())
    # literal for l1: if l1>0, literal = 2*(l1-1)+1 (true), else 2*(|l1|-1) (false)
    # We want clause: (not neg1) or (not neg2)
    # neg1 is true when yield of l1 is negative
    if l1 > 0:
        neg1 = 2 * (l1 - 1)      # x=false -> negative
    else:
        neg1 = 2 * (-l1 - 1) + 1 # x=true -> negative
    if l2 > 0:
        neg2 = 2 * (l2 - 1)
    else:
        neg2 = 2 * (-l2 - 1) + 1
    # clause: not neg1 or not neg2
    add_clause(neg1 ^ 1, neg2 ^ 1)

# Kosaraju SCC
visited = [False] * N
order = []
def dfs1(u):
    visited[u] = True
    for v in g[u]:
        if not visited[v]:
            dfs1(v)
    order.append(u)

for i in range(N):
    if not visited[i]:
        dfs1(i)

comp = [-1] * N
def dfs2(u, cid):
    comp[u] = cid
    for v in gr[u]:
        if comp[v] == -1:
            dfs2(v, cid)

cid = 0
for u in reversed(order):
    if comp[u] == -1:
        dfs2(u, cid)
        cid += 1

# Check satisfiability
for i in range(n):
    if comp[2*i] == comp[2*i+1]:
        print("NO")
        sys.exit()

print("YES")
res = []
for i in range(n):
    # If true node has higher comp id, assign true
    if comp[2*i+1] > comp[2*i]:
        res.append('1')
    else:
        res.append('0')
print(' '.join(res))