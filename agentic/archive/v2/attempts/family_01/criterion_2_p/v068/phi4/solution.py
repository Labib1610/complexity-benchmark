import sys
input = sys.stdin.readline

n, m = map(int, input().split())
if n == 1:
    print("YES")
    print(1)
    sys.exit()

adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    adj[u].append(v)
    adj[v].append(u)

colors = [0] * n

def dfs(node, color):
    if colors[node] != 0:
        return colors[node] == color
    colors[node] = color
    for neighbor in adj[node]:
        if not dfs(neighbor, 3 - color):
            return False
    return True

for i in range(n):
    if colors[i] == 0 and not dfs(i, 1):
        print("NO")
        sys.exit()

print("YES")
assignment = [colors[i] for i in range(n)]
print(' '.join(map(str, assignment)))