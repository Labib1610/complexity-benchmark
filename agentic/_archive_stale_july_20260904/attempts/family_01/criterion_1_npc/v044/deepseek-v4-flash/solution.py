import sys

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

    def backtrack(i):
        if i == n:
            return True
        for c in range(3):  # shifts 1,2,3 -> 0,1,2 internally
            ok = True
            for nb in adj[i]:
                if color[nb] == c:
                    ok = False
                    break
            if ok:
                color[i] = c
                if backtrack(i + 1):
                    return True
                color[i] = -1
        return False

    if backtrack(0):
        print("YES")
        print(" ".join(str(c + 1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()