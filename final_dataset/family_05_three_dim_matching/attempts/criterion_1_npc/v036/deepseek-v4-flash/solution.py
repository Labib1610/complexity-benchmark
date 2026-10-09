import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    triples = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        triples.append((x-1, y-1, z-1))
    
    # Sort by some heuristic: maybe by how many resources they cover? All cover 3.
    # We'll sort by frequency of each resource to try rare ones first.
    freq_x = [0]*k
    freq_y = [0]*k
    freq_z = [0]*k
    for x,y,z in triples:
        freq_x[x] += 1
        freq_y[y] += 1
        freq_z[z] += 1
    # Sort triples by sum of frequencies (rarer first)
    triples.sort(key=lambda t: freq_x[t[0]] + freq_y[t[1]] + freq_z[t[2]])
    
    used_x = 0
    used_y = 0
    used_z = 0
    chosen = []
    
    # Precompute for each triple its bitmask
    masks = []
    for x,y,z in triples:
        masks.append((1<<x, 1<<y, 1<<z))
    
    # For pruning: for each resource, list of triples that use it
    triples_by_x = [[] for _ in range(k)]
    triples_by_y = [[] for _ in range(k)]
    triples_by_z = [[] for _ in range(k)]
    for idx, (x,y,z) in enumerate(triples):
        triples_by_x[x].append(idx)
        triples_by_y[y].append(idx)
        triples_by_z[z].append(idx)
    
    full_mask = (1<<k) - 1
    
    # Recursive search
    def dfs(depth):
        nonlocal used_x, used_y, used_z
        if depth == k:
            return True
        # Choose the resource with fewest remaining options
        # Find an unused x, y, z with minimal candidate triples
        best = None
        best_count = float('inf')
        # Check x
        for i in range(k):
            if not (used_x >> i) & 1:
                cnt = 0
                for idx in triples_by_x[i]:
                    mx, my, mz = masks[idx]
                    if (used_y & my) == 0 and (used_z & mz) == 0:
                        cnt += 1
                if cnt < best_count:
                    best_count = cnt
                    best = ('x', i)
        # Check y
        for i in range(k):
            if not (used_y >> i) & 1:
                cnt = 0
                for idx in triples_by_y[i]:
                    mx, my, mz = masks[idx]
                    if (used_x & mx) == 0 and (used_z & mz) == 0:
                        cnt += 1
                if cnt < best_count:
                    best_count = cnt
                    best = ('y', i)
        # Check z
        for i in range(k):
            if not (used_z >> i) & 1:
                cnt = 0
                for idx in triples_by_z[i]:
                    mx, my, mz = masks[idx]
                    if (used_x & mx) == 0 and (used_y & my) == 0:
                        cnt += 1
                if cnt < best_count:
                    best_count = cnt
                    best = ('z', i)
        
        if best_count == 0:
            return False
        
        typ, val = best
        if typ == 'x':
            candidates = triples_by_x[val]
            for idx in candidates:
                mx, my, mz = masks[idx]
                if (used_y & my) == 0 and (used_z & mz) == 0:
                    used_x |= mx
                    used_y |= my
                    used_z |= mz
                    chosen.append(triples[idx])
                    if dfs(depth+1):
                        return True
                    chosen.pop()
                    used_x ^= mx
                    used_y ^= my
                    used_z ^= mz
        elif typ == 'y':
            candidates = triples_by_y[val]
            for idx in candidates:
                mx, my, mz = masks[idx]
                if (used_x & mx) == 0 and (used_z & mz) == 0:
                    used_x |= mx
                    used_y |= my
                    used_z |= mz
                    chosen.append(triples[idx])
                    if dfs(depth+1):
                        return True
                    chosen.pop()
                    used_x ^= mx
                    used_y ^= my
                    used_z ^= mz
        else:
            candidates = triples_by_z[val]
            for idx in candidates:
                mx, my, mz = masks[idx]
                if (used_x & mx) == 0 and (used_y & my) == 0:
                    used_x |= mx
                    used_y |= my
                    used_z |= mz
                    chosen.append(triples[idx])
                    if dfs(depth+1):
                        return True
                    chosen.pop()
                    used_x ^= mx
                    used_y ^= my
                    used_z ^= mz
        return False
    
    if dfs(0):
        print("YES")
        for x,y,z in chosen:
            print(x+1, y+1, z+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()