import sys
sys.setrecursionlimit(300000)

inp = sys.stdin.readline
n, m, t = map(int, inp().split())
flags = list(map(int, inp().split()))
flag_set = set(flags)

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, inp().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

# We'll find the minimal subgraph connecting all flags.
# Approach: DFS from any flag, count flags in subtree.
# If a subtree contains at least one flag, we need the edge to its parent.
# Remove all edges that lead to subtrees with no flags.

visited = [False] * (n + 1)
total_energy = 0

def dfs(u, parent, parent_weight):
    global total_energy
    visited[u] = True
    cnt = 1 if u in flag_set else 0
    for v, w in adj[u]:
        if v == parent:
            continue
        if not visited[v]:
            sub_cnt = dfs(v, u, w)
            if sub_cnt > 0:
                cnt += sub_cnt
                total_energy += w
    return cnt

# start from first flag
start = flags[0]
dfs(start, -1, 0)

print(total_energy)