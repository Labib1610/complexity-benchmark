import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n  # 0 = unassigned, 1,2,3 = environments
    
    def backtrack(idx):
        if idx == n:
            return True
        for c in (1, 2, 3):
            ok = True
            for nb in adj[idx]:
                if color[nb] == c:
                    ok = False
                    break
            if ok:
                color[idx] = c
                if backtrack(idx + 1):
                    return True
                color[idx] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()