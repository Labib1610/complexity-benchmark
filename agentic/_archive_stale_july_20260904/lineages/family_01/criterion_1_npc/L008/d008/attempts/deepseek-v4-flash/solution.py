n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Precompute allowed pairs
allowed = {}
for a in (1,2,3):
    for b in (1,2,3):
        left = (17*a**3 + 27*b**2) % 64
        right = (17*b**3 + 27*a**2) % 64
        if left != right:
            allowed[(a,b)] = True

# Build adjacency list
adj = [[] for _ in range(n)]
for u,v in edges:
    u-=1; v-=1
    adj[u].append(v)
    adj[v].append(u)

assign = [0]*n
found = False

def dfs(idx):
    global found
    if found:
        return
    if idx == n:
        found = True
        return
    for val in (1,2,3):
        # Check all neighbors already assigned
        ok = True
        for nb in adj[idx]:
            if assign[nb] != 0:
                if (val, assign[nb]) not in allowed:
                    ok = False
                    break
        if ok:
            assign[idx] = val
            dfs(idx+1)
            if found:
                return
            assign[idx] = 0

dfs(0)

if not found:
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, assign)))