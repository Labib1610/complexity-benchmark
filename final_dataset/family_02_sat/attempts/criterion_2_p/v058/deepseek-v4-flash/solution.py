import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # each variable has two nodes: x_i and not x_i

def node(var):
    # var > 0 means x_var, var < 0 means not x_var
    if var > 0:
        return (var - 1) * 2      # even index for x_i
    else:
        return (-var - 1) * 2 + 1 # odd index for not x_i

g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]

for _ in range(m):
    a, b = map(int, input().split())
    # clause (a OR b) => (!a -> b) and (!b -> a)
    u = node(-a)
    v = node(b)
    g[u].append(v)
    gr[v].append(u)

    u = node(-b)
    v = node(a)
    g[u].append(v)
    gr[v].append(u)

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
    if comp[2*i] == comp[2*i+1]:
        print("NO")
        sys.exit()

# Assign values
assignment = [0] * n
for i in range(n):
    # If not x_i is after x_i in topological order, assign True
    assignment[i] = 1 if comp[2*i] > comp[2*i+1] else 0

print("YES")
print(" ".join(map(str, assignment)))