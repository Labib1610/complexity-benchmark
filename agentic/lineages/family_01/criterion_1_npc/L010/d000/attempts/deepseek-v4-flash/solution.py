import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    color = [0] * n
    
    def backtrack(i):
        if i == n:
            return True
        for c in range(1, 4):
            ok = True
            for j in range(n):
                if (adj[i] >> j) & 1 and color[j] == c:
                    ok = False
                    break
            if ok:
                color[i] = c
                if backtrack(i + 1):
                    return True
                color[i] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()