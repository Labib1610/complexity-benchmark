import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

n, m = map(int, input().split())
N = 2 * n  # each variable x gets 2 nodes: 2*(i-1) for False, 2*(i-1)+1 for True

def node(var):
    # var: integer, positive => True node, negative => False node
    v = abs(var)
    if var > 0:
        return 2 * (v - 1) + 1
    else:
        return 2 * (v - 1)

def neg_node(idx):
    return idx ^ 1

graph = [[] for _ in range(N)]
for _ in range(m):
    a, b = map(int, input().split())
    na = neg_node(node(a))
    nb = neg_node(node(b))
    graph[na].append(node(b))
    graph[nb].append(node(a))

# Tarjan SCC
index = 0
stack = []
onstack = [False] * N
idx = [-1] * N
low = [0] * N
scc_id = [-1] * N
scc_count = 0

def tarjan(u):
    global index, scc_count
    idx[u] = low[u] = index
    index += 1
    stack.append(u)
    onstack[u] = True
    for v in graph[u]:
        if idx[v] == -1:
            tarjan(v)
            low[u] = min(low[u], low[v])
        elif onstack[v]:
            low[u] = min(low[u], idx[v])
    if low[u] == idx[u]:
        while True:
            w = stack.pop()
            onstack[w] = False
            scc_id[w] = scc_count
            if w == u:
                break
        scc_count += 1

for i in range(N):
    if idx[i] == -1:
        tarjan(i)

# Check contradiction
for i in range(n):
    if scc_id[2*i] == scc_id[2*i+1]:
        print("NO")
        sys.exit()

# Assign values: scc_id order is reverse topological
assignment = [False] * n
for i in range(n):
    # if True node has higher scc_id than False node => assign True
    assignment[i] = scc_id[2*i+1] > scc_id[2*i]

print("YES")
print(" ".join("1" if assignment[i] else "0" for i in range(n)))