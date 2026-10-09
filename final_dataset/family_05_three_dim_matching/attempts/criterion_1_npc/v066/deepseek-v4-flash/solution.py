import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    profiles = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        profiles.append((x-1, y-1, z-1))
    
    # Group profiles by specialist
    by_spec = [[] for _ in range(k)]
    for x, y, z in profiles:
        by_spec[x].append((y, z))
    
    # For each specialist, sort profiles by facility and dossier for deterministic order
    for i in range(k):
        by_spec[i].sort()
    
    used_fac = 0
    used_dos = 0
    chosen = [None] * k
    
    # Precompute for each specialist the list of (facility, dossier) pairs
    # We'll do recursive search with pruning
    
    def dfs(spec_idx):
        if spec_idx == k:
            return True
        # Find the specialist with fewest available profiles among remaining
        best = -1
        best_list = None
        for i in range(k):
            if chosen[i] is None:
                # Count available profiles for this specialist
                cnt = 0
                for y, z in by_spec[i]:
                    if not (used_fac >> y) & 1 and not (used_dos >> z) & 1:
                        cnt += 1
                if cnt == 0:
                    return False
                if best == -1 or cnt < best:
                    best = cnt
                    best_list = i
        # Try each profile for best_list
        for y, z in by_spec[best_list]:
            if not (used_fac >> y) & 1 and not (used_dos >> z) & 1:
                chosen[best_list] = (best_list, y, z)
                used_fac |= (1 << y)
                used_dos |= (1 << z)
                if dfs(spec_idx + 1):
                    return True
                used_fac ^= (1 << y)
                used_dos ^= (1 << z)
                chosen[best_list] = None
        return False
    
    if dfs(0):
        print("YES")
        for x, y, z in chosen:
            print(x+1, y+1, z+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()