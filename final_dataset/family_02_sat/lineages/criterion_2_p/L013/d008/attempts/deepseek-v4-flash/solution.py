import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # each variable has two nodes: x_i and not x_i

# node mapping: 
# variable i (0-indexed): 
#   i*2   -> x_i is True
#   i*2+1 -> x_i is False

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

def add_imp(u, v):
    g[u].append(v)
    gr[v].append(u)

def add_clause(a, b):
    # clause: a OR b
    # ~a => b, ~b => a
    add_imp(a ^ 1, b)
    add_imp(b ^ 1, a)

for _ in range(m):
    l1, l2 = map(int, input().split())
    a = abs(l1) - 1
    b = abs(l2) - 1
    # literal representation:
    # if l > 0: literal = 2*a   (x_a True)
    # if l < 0: literal = 2*a+1 (x_a False)
    lit1 = 2*a if l1 > 0 else 2*a + 1
    lit2 = 2*b if l2 > 0 else 2*b + 1
    # We need NOT (lit1 is False AND lit2 is False)
    # i.e. lit1 OR lit2
    add_clause(lit1, lit2)

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
    # if comp[2*i] > comp[2*i+1], x_i is True
    res.append('1' if comp[2*i] > comp[2*i+1] else '0')
print(' '.join(res))