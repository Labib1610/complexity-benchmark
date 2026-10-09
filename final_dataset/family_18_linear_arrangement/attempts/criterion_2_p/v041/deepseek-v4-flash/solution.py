import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

n, m, B = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

parent = [-1]*n
order = []
stack = [0]
parent[0] = 0
while stack:
    u = stack.pop()
    order.append(u)
    for v in adj[u]:
        if v == parent[u]:
            continue
        parent[v] = u
        stack.append(v)

sub = [1]*n
for u in reversed(order):
    for v in adj[u]:
        if v == parent[u]:
            continue
        sub[u] += sub[v]

min_total = sum(sub[i] for i in range(n) if i != 0)

if min_total > B:
    print("NO")
else:
    # Assign labels via preorder (same order as the DFS order we built)
    labels = [0]*n
    for idx, node in enumerate(order):
        labels[node] = idx+1
    print("YES")
    print(' '.join(map(str, labels)))