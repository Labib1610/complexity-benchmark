import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        adj[u].add(v)
        adj[v].add(u)
    
    color = [0] * n  # 0 = unassigned, 1/2/3 = energy level
    
    def backtrack(pos):
        if pos == n:
            return True
        for c in range(1, 4):
            ok = True
            for nb in adj[pos]:
                if color[nb] == c:
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
        print(' '.join(str(c) for c in color))
    else:
        print("NO")

solve()