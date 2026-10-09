import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    groups = [[], []]
    
    for i in range(n):
        if color[i] == -1:
            stack = [i]
            color[i] = 0
            groups[0].append(i)
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        groups[color[v]].append(v)
                        stack.append(v)
    
    # Choose the larger group
    if len(groups[0]) < len(groups[1]):
        groups[0], groups[1] = groups[1], groups[0]
    
    if len(groups[0]) >= k:
        print("YES")
        print(" ".join(str(x + 1) for x in groups[0][:k]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()