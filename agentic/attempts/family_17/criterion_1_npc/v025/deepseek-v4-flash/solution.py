import sys
sys.setrecursionlimit(1000000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx]); b = int(input_data[idx+1]); c = int(input_data[idx+2])
        idx += 3
        triples.append((a, b, c))
    
    n = 3 * q
    full_mask = (1 << (n + 1)) - 1  # bits 1..n set
    
    # Build masks
    masks = []
    for a, b, c in triples:
        masks.append((1 << a) | (1 << b) | (1 << c))
    
    # Map each zone to list of triple indices
    zone_to_triples = [[] for _ in range(n + 1)]
    for i, m in enumerate(masks):
        # extract zones
        for z in range(1, n + 1):
            if m & (1 << z):
                zone_to_triples[z].append(i)
    
    used = [False] * t
    chosen = []
    
    # Recursive search
    def dfs(covered_mask):
        if covered_mask == full_mask:
            return True
        # find zone with fewest available triples
        best_zone = -1
        best_list = None
        for z in range(1, n + 1):
            if not (covered_mask & (1 << z)):
                avail = [i for i in zone_to_triples[z] if not used[i] and (masks[i] & covered_mask) == 0]
                if best_zone == -1 or len(avail) < len(best_list):
                    best_zone = z
                    best_list = avail
                    if len(best_list) == 0:
                        return False
                    if len(best_list) == 1:
                        break
        for i in best_list:
            m = masks[i]
            # mark used
            used[i] = True
            chosen.append(triples[i])
            if dfs(covered_mask | m):
                return True
            chosen.pop()
            used[i] = False
        return False
    
    if dfs(0):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()