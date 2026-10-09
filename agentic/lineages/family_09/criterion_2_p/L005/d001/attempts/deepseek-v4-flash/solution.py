import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
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
    
    size0 = len(groups[0])
    size1 = len(groups[1])
    
    # We can take from group0 and group1
    # Need exactly k total
    # Try to take as many as possible from group0, then fill from group1
    take0 = min(size0, k)
    take1 = k - take0
    if take1 > size1:
        # Try taking more from group1 first
        take1 = min(size1, k)
        take0 = k - take1
        if take0 > size0:
            print("NO")
            return
    
    ans = groups[0][:take0] + groups[1][:take1]
    print("YES")
    print(" ".join(str(x+1) for x in ans))

if __name__ == "__main__":
    solve()