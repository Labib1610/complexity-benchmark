import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    edges = []
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1])
        idx += 2
        u -= 1; v -= 1
        if u > v:
            u, v = v, u
        edges.append((u, v))
    
    # For each pair of multipliers (a,b), cross product of (1,a,a^2) and (1,b,b^2) is zero iff a==b
    # So we need a proper 3-coloring of the graph
    
    color = [0] * n
    
    def backtrack(pos):
        if pos == n:
            return True
        for c in range(1, 4):
            ok = True
            for (u, v) in edges:
                if u == pos and v < pos and color[v] == c:
                    ok = False
                    break
                if v == pos and u < pos and color[u] == c:
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
        print(" ".join(str(c) for c in color))
    else:
        print("NO")

solve()