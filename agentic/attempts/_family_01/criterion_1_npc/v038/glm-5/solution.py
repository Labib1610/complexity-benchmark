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
    
    color = [0] * n
    
    def select_vertex():
        best = -1
        best_sat = -1
        best_deg = -1
        for v in range(n):
            if color[v] == 0:
                sat = len({color[u] for u in adj[v] if color[u] != 0})
                deg = len(adj[v])
                if sat > best_sat or (sat == best_sat and deg > best_deg):
                    best_sat = sat
                    best_deg = deg
                    best = v
        return best
    
    def backtrack(count):
        if count == n:
            return True
        v = select_vertex()
        for c in range(1, 4):
            ok = True
            for u in adj[v]:
                if color[u] == c:
                    ok = False
                    break
            if ok:
                color[v] = c
                if backtrack(count + 1):
                    return True
                color[v] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()