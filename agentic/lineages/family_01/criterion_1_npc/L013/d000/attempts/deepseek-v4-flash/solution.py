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
    
    assignment = [0] * n
    
    def backtrack(idx):
        if idx == n:
            return True
        for color in (1, 2, 3):
            ok = True
            for nb in adj[idx]:
                if assignment[nb] == color:
                    ok = False
                    break
            if ok:
                assignment[idx] = color
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