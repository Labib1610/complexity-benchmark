import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # pairs_by_sat[x] = list of (y, z)
    pairs_by_sat = [[] for _ in range(k+1)]
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        pairs_by_sat[x].append((y, z))
    
    # Sort satellites by number of pairs (ascending)
    order = list(range(1, k+1))
    order.sort(key=lambda x: len(pairs_by_sat[x]))
    
    used_freq = [False]*(k+1)
    used_key = [False]*(k+1)
    assignment = [None]*(k+1)  # assignment[sat] = (y, z)
    
    def dfs(idx):
        if idx == k:
            return True
        sat = order[idx]
        for y, z in pairs_by_sat[sat]:
            if not used_freq[y] and not used_key[z]:
                used_freq[y] = True
                used_key[z] = True
                assignment[sat] = (y, z)
                if dfs(idx+1):
                    return True
                used_freq[y] = False
                used_key[z] = False
                assignment[sat] = None
        return False
    
    if dfs(0):
        print("YES")
        for sat in range(1, k+1):
            y, z = assignment[sat]
            print(sat, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()