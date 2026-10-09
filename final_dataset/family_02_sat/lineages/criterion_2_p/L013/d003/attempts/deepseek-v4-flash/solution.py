import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # each variable has two nodes: x_i and ¬x_i

def node(var):
    # var is signed int: positive -> ON, negative -> OFF
    if var > 0:
        return (var - 1) * 2      # x_i
    else:
        return (-var - 1) * 2 + 1 # ¬x_i

def neg_node(idx):
    return idx ^ 1

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

for _ in range(m):
    a, b = map(int, input().split())
    na = node(-a)
    nb = node(-b)
    a_node = node(a)
    b_node = node(b)
    # ¬a -> b
    g[na].append(b_node)
    gr[b_node].append(na)
    # ¬b -> a
    g[nb].append(a_node)
    gr[a_node].append(nb)

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

# Assign values
assignment = [False] * n
for i in range(n):
    # In Kosaraju, comp id order gives topological order of SCCs in reverse
    # If ¬x_i is after x_i in topological order, x_i is true
    assignment[i] = comp[2*i] > comp[2*i+1]

print("YES")
print(" ".join('1' if assignment[i] else '0' for i in range(n)))