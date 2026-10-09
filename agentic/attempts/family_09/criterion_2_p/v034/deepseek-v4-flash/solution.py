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
    left = []
    right = []
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            stack = [i]
            left.append(i)
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        if color[v] == 0:
                            left.append(v)
                        else:
                            right.append(v)
                        stack.append(v)
    
    if len(left) >= k:
        ans = left[:k]
    else:
        ans = left + right[:k - len(left)]
    
    print("YES")
    print(" ".join(str(x+1) for x in ans))

if __name__ == "__main__":
    solve()