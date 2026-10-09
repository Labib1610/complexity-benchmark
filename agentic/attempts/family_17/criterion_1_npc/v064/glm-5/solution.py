import sys
input = sys.stdin.readline

def solve():
    q, t = map(int, input().split())
    n = 3 * q
    
    adj = [[] for _ in range(n + 1)]
    recipes = []
    
    for _ in range(t):
        a, b, c = map(int, input().split())
        recipes.append((a, b, c))
        adj[a].append((b, c))
        adj[b].append((a, c))
        adj[c].append((a, b))
    
    match = [0] * (n + 1)
    
    def dfs(u, visited):
        for v, w in adj[u]:
            if visited[v]: continue
            visited[v] = True
            if match[v] == 0 or dfs(match[v], visited):
                match[v] = u
                match[u] = v
                return True
        return False

    for u in range(1, n + 1):
        if match[u] == 0:
            visited = [False] * (n + 1)
            visited[u] = True
            if not dfs(u, visited):
                print("NO")
                return

    print("YES")
    printed = [False] * (n + 1)
    for a, b, c in recipes:
        if match[a] == b and match[b] == a:
            if not printed[a]:
                print(a, b, match[c])
                printed[a] = printed[b] = printed[match[c]] = True
        elif match[a] == c and match[c] == a:
            if not printed[a]:
                print(a, c, match[b])
                printed[a] = printed[c] = printed[match[b]] = True

if __name__ == '__main__':
    solve()