import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    specs = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        specs.append((x, y, z))
    
    # Group specs by x (host) for faster lookup
    by_x = [[] for _ in range(k + 1)]
    for idx, (x, y, z) in enumerate(specs):
        by_x[x].append((y, z, idx))
    
    used_y = [False] * (k + 1)
    used_z = [False] * (k + 1)
    chosen = []
    
    # Backtracking: assign a host for each host id 1..k
    def dfs(host):
        if host == k + 1:
            return True
        for y, z, idx in by_x[host]:
            if not used_y[y] and not used_z[z]:
                used_y[y] = True
                used_z[z] = True
                chosen.append((host, y, z))
                if dfs(host + 1):
                    return True
                chosen.pop()
                used_y[y] = False
                used_z[z] = False
        return False
    
    if dfs(1):
        print("YES")
        for x, y, z in chosen:
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()