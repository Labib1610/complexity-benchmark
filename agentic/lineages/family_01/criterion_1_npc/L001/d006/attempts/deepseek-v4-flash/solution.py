import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n
    
    def backtrack(pos):
        if pos == n:
            return True
        # Try colors 1, 2, 3 in increasing order for lexicographic minimality
        for c in (1, 2, 3):
            ok = True
            for nb in adj[pos]:
                if nb < pos and color[nb] == c:
                    ok = False
                    break
            if ok:
                color[pos] = c
                if backtrack(pos + 1):
                    return True
                color[pos] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()