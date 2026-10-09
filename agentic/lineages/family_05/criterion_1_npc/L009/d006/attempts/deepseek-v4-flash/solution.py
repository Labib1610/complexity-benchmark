import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    # We'll store edges: (x, y) -> list of z
    edges = defaultdict(list)
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        edges[(x, y)].append(z)
    
    # We need to select exactly k edges such that:
    # - each x appears exactly once
    # - each y appears exactly once
    # - each z appears exactly once
    # This is a 3D matching problem, but since k <= 22, we can do backtracking with pruning.
    
    # Build list of all possible (x,y) pairs that have at least one z
    pairs = [(x, y) for (x, y), zlist in edges.items() if zlist]
    
    used_x = [False] * k
    used_y = [False] * k
    used_z = [False] * k
    chosen = []
    
    # Sort pairs by number of z options to try fewer branches first
    pairs.sort(key=lambda p: len(edges[p]))
    
    def backtrack(idx):
        if idx == k:
            return True
        x, y = pairs[idx]
        if used_x[x] or used_y[y]:
            return backtrack(idx + 1)
        for z in edges[(x, y)]:
            if not used_z[z]:
                used_x[x] = True
                used_y[y] = True
                used_z[z] = True
                chosen.append((x, y, z))
                if backtrack(idx + 1):
                    return True
                chosen.pop()
                used_x[x] = False
                used_y[y] = False
                used_z[z] = False
        return False
    
    # But this simple backtracking over pairs may miss combinations where we skip some pairs.
    # Better: recursive search over all pairs, choosing or skipping.
    
    used_x = [False] * k
    used_y = [False] * k
    used_z = [False] * k
    chosen = []
    
    def dfs(i):
        if len(chosen) == k:
            return True
        if i == len(pairs):
            return False
        # Option 1: skip this pair
        if dfs(i + 1):
            return True
        # Option 2: take this pair if possible
        x, y = pairs[i]
        if not used_x[x] and not used_y[y]:
            for z in edges[(x, y)]:
                if not used_z[z]:
                    used_x[x] = True
                    used_y[y] = True
                    used_z[z] = True
                    chosen.append((x, y, z))
                    if dfs(i + 1):
                        return True
                    chosen.pop()
                    used_x[x] = False
                    used_y[y] = False
                    used_z[z] = False
        return False
    
    if dfs(0):
        print("YES")
        for x, y, z in chosen:
            print(x + 1, y + 1, z + 1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()