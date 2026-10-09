import sys

input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

# Build graph for 2-SAT
# Each machine i has two possible modes: 0 or 1
# Polarity p_i = 2*s_i - 1
# For interlock (c1, c2):
# condition: c1*p1 + c2*p2 > -(|c1|+|c2|)
# Let's transform to implications.

# For each machine i, variable x_i = s_i (0 or 1)
# p_i = 2*x_i - 1

# For an interlock (c1, c2):
# Let a = |c1|, b = |c2|
# sign1 = sign(c1), sign2 = sign(c2)
# condition: sign1*(2*x_a - 1) + sign2*(2*x_b - 1) > -(a+b)
# => 2*sign1*x_a - sign1 + 2*sign2*x_b - sign2 > -a - b
# => 2*sign1*x_a + 2*sign2*x_b > sign1 + sign2 - a - b

# We can check all 4 assignments for (x_a, x_b) and see which are invalid.
# Invalid assignments become forbidden, which we encode as 2-SAT clauses.

# 2-SAT: variable i has two literals: i*2 for false (0), i*2+1 for true (1)
# Clause (l1 OR l2) => add implications: not l1 -> l2, not l2 -> l1

N = 2 * n
g = [[] for _ in range(N)]
rg = [[] for _ in range(N)]

def add_imp(u, v):
    g[u].append(v)
    rg[v].append(u)

def add_clause(l1, l2):
    # l1 or l2
    add_imp(l1 ^ 1, l2)
    add_imp(l2 ^ 1, l1)

for c1, c2 in edges:
    a = abs(c1)
    b = abs(c2)
    s1 = 1 if c1 > 0 else -1
    s2 = 1 if c2 > 0 else -1
    # Check all 4 assignments
    for xa in (0, 1):
        for xb in (0, 1):
            val = s1 * (2*xa - 1) + s2 * (2*xb - 1)
            if not (val > -(a + b)):
                # invalid assignment: forbid (xa, xb)
                # clause: (x_a != xa) OR (x_b != xb)
                lit_a = (2 * (a-1)) + xa  # literal for x_a = xa
                lit_b = (2 * (b-1)) + xb  # literal for x_b = xb
                add_clause(lit_a ^ 1, lit_b ^ 1)

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
    for v in rg[u]:
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

# Build assignment
assignment = [0] * n
for i in range(n):
    # comp[2*i] < comp[2*i+1] => false (0) is chosen
    assignment[i] = 0 if comp[2*i] < comp[2*i+1] else 1

print("YES")
print(" ".join(map(str, assignment)))