import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)
    
    assignment = [0] * n
    
    def backtrack(idx):
        if idx == n:
            return True
        for color in (1, 2, 3):
            ok = True
            for neighbor in adj[idx]:
                if assignment[neighbor] == color:
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