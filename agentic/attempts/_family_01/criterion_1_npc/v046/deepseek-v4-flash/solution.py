n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * n

def dfs(node, c):
    color[node] = c
    for nei in adj[node]:
        if color[nei] == c:
            return False
        if color[nei] == -1:
            if not dfs(nei, 3 - c):  # alternate between 1 and 2
                return False
    return True

# Try to color with 3 colors using backtracking
def can_color(node):
    if node == n:
        return True
    for c in range(1, 4):
        if all(color[nei] != c for nei in adj[node]):
            old = color[node]
            color[node] = c
            if can_color(node + 1):
                return True
            color[node] = old
    return False

if can_color(0):
    print("YES")
    print(" ".join(str(color[i]) for i in range(n)))
else:
    print("NO")