import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * (n + 1)
    groups = [[], []]
    
    for start in range(1, n + 1):
        if color[start] == -1:
            color[start] = 0
            stack = [start]
            while stack:
                u = stack.pop()
                groups[color[u]].append(u)
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        stack.append(v)
    
    if len(groups[0]) >= k:
        print("YES")
        print(' '.join(map(str, groups[0][:k])))
    elif len(groups[1]) >= k:
        print("YES")
        print(' '.join(map(str, groups[1][:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()