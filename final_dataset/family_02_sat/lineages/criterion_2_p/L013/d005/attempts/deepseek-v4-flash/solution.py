import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # each variable has two nodes: x_i and not x_i

# node mapping: 
# variable i (1-indexed) -> node 2*(i-1) for False, 2*(i-1)+1 for True
def node(var, val):
    # var: 1..n, val: True/False
    idx = 2 * (var - 1)
    return idx + (1 if val else 0)

def neg_node(u):
    return u ^ 1

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

for _ in range(m):
    a, b = map(int, input().split())
    # literal: positive means True, negative means False
    def lit_to_node(l):
        var = abs(l)
        val = l > 0
        return node(var, val)
    u = lit_to_node(a)
    v = lit_to_node(b)
    # clause (u OR v) => (!u -> v) and (!v -> u)
    g[neg_node(u)].append(v)
    g[neg_node(v)].append(u)
    gr[v].append(neg_node(u))
    gr[u].append(neg_node(v))

# Kosaraju SCC
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

# Check satisfiability
for i in range(n):
    if comp[node(i+1, True)] == comp[node(i+1, False)]:
        print("NO")
        sys.exit()

# Assign values
assignment = [False] * n
for i in range(n):
    # If True node comes after False node in topological order of SCCs, set True
    assignment[i] = comp[node(i+1, True)] > comp[node(i+1, False)]

print("YES")
print(" ".join("1" if x else "0" for x in assignment))