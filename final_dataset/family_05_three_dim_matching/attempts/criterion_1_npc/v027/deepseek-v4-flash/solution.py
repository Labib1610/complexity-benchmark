import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    reactions = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        reactions.append((x-1, y-1, z-1))
    
    # For each base fluid, store list of (catalyst, thermal) pairs
    by_base = [[] for _ in range(k)]
    for x, y, z in reactions:
        by_base[x].append((y, z))
    
    # We'll try to assign each base fluid a distinct catalyst and thermal profile
    used_cat = [False] * k
    used_therm = [False] * k
    assignment = [None] * k  # assignment[x] = (y, z)
    
    # Sort base fluids by number of options (smallest first) for pruning
    order = sorted(range(k), key=lambda i: len(by_base[i]))
    
    def dfs(idx):
        if idx == k:
            return True
        x = order[idx]
        for y, z in by_base[x]:
            if not used_cat[y] and not used_therm[z]:
                used_cat[y] = True
                used_therm[z] = True
                assignment[x] = (y, z)
                if dfs(idx + 1):
                    return True
                used_cat[y] = False
                used_therm[z] = False
                assignment[x] = None
        return False
    
    if dfs(0):
        print("YES")
        for x in range(k):
            y, z = assignment[x]
            print(x+1, y+1, z+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()