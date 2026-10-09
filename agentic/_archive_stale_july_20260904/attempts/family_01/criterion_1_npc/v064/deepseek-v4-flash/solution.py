n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

colors = [0] * n

def is_valid(node, color):
    for neighbor in adj[node]:
        if colors[neighbor] == color:
            return False
    return True

def backtrack(idx):
    if idx == n:
        return True
    for color in (1, 2, 3):
        if is_valid(idx, color):
            colors[idx] = color
            if backtrack(idx + 1):
                return True
            colors[idx] = 0
    return False

if backtrack(0):
    print("YES")
    print(" ".join(map(str, colors)))
else:
    print("NO")