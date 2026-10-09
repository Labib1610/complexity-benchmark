import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    
    # x -> list of z (y is determined by x)
    x_to_zs = [[] for _ in range(k + 1)]
    x_to_y = [0] * (k + 1)
    
    idx = 2
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        idx += 3
        x_to_zs[x].append(z)
        x_to_y[x] = y
    
    # Check every x has at least one triad
    for x in range(1, k + 1):
        if not x_to_zs[x]:
            print("NO")
            return
    
    # Bipartite matching: left = x (1..k), right = z (1..k)
    # We need a perfect matching.
    match_z = [0] * (k + 1)  # which x is matched to z
    match_x = [0] * (k + 1)  # which z is matched to x
    
    # Build adjacency for faster iteration
    adj = x_to_zs  # adj[x] = list of z
    
    def try_kuhn(x, visited):
        for z in adj[x]:
            if visited[z]:
                continue
            visited[z] = True
            if match_z[z] == 0 or try_kuhn(match_z[z], visited):
                match_z[z] = x
                match_x[x] = z
                return True
        return False
    
    for x in range(1, k + 1):
        visited = [False] * (k + 1)
        if not try_kuhn(x, visited):
            print("NO")
            return
    
    print("YES")
    out = []
    for x in range(1, k + 1):
        z = match_x[x]
        y = x_to_y[x]
        out.append(f"{x} {y} {z}")
    sys.stdout.write("\n".join(out) + "\n")

solve()