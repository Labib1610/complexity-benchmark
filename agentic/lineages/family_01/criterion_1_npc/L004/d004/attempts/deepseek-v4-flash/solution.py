import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n, m = int(input_data[0]), int(input_data[1])
    edges = []
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        edges.append((u, v))
    
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    colors = [0] * n
    
    def backtrack(pos):
        if pos == n:
            return True
        for c in range(1, 4):
            ok = True
            for nb in adj[pos]:
                if colors[nb] == c:
                    ok = False
                    break
            if ok:
                colors[pos] = c
                if backtrack(pos + 1):
                    return True
                colors[pos] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()