import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    ok = True
    
    from collections import deque
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
                    elif color[v] == color[u]:
                        ok = False
                        break
                if not ok:
                    break
        if not ok:
            break
    
    if not ok:
        print("NO")
        return
    
    cand1 = [1 if c == 0 else 2 for c in color]
    cand2 = [2 if c == 0 else 1 for c in color]
    
    # choose lexicographically smaller
    if cand1 < cand2:
        ans = cand1
    else:
        ans = cand2
    
    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    solve()