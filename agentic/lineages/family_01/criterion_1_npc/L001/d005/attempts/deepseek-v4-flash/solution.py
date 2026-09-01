import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)
    
    color = [0] * n
    
    def backtrack(i):
        if i == n:
            return True
        for c in (1, 2, 3):
            ok = True
            for nb in adj[i]:
                if color[nb] == c:
                    ok = False
                    break
            if ok:
                color[i] = c
                if backtrack(i + 1):
                    return True
                color[i] = 0
        return False
    
    if backtrack(0):
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, color)) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()