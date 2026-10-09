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
    
    # BFS/DFS to color bipartite
    from collections import deque
    for i in range(n):
        if color[i] == -1:
            q = deque([i])
            color[i] = 0
            groups[0].append(i)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        groups[color[v]].append(v)
                        q.append(v)
                    elif color[v] == color[u]:
                        # Should not happen due to guarantee
                        pass
    
    size0 = len(groups[0])
    size1 = len(groups[1])
    
    # We need to pick a from group0 and b from group1 such that a+b = k, 0<=a<=size0, 0<=b<=size1
    # So a can be from max(0, k-size1) to min(k, size0)
    lo = max(0, k - size1)
    hi = min(k, size0)
    if lo > hi:
        print("NO")
        return
    
    take0 = lo
    take1 = k - take0
    
    chosen = groups[0][:take0] + groups[1][:take1]
    print("YES")
    print(" ".join(str(x+1) for x in chosen))

if __name__ == "__main__":
    solve()