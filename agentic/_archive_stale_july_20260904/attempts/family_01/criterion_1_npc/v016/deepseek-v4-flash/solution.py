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
    
    assignment = [0] * n
    
    def backtrack(idx):
        if idx == n:
            return True
        for phase in (1, 2, 3):
            ok = True
            for nb in adj[idx]:
                if assignment[nb] == phase:
                    ok = False
                    break
            if ok:
                assignment[idx] = phase
                if backtrack(idx + 1):
                    return True
                assignment[idx] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()