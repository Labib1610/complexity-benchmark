import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q
    protocols = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        mask = (1 << a) | (1 << b) | (1 << c)
        protocols.append((a, b, c, mask))
    
    all_mask = (1 << n) - 1
    
    # Precompute for each sector the list of protocol indices that cover it
    sector_to_protocols = [[] for _ in range(n)]
    for idx, (a, b, c, mask) in enumerate(protocols):
        sector_to_protocols[a].append(idx)
        sector_to_protocols[b].append(idx)
        sector_to_protocols[c].append(idx)
    
    # Sort protocols by first sector for deterministic order
    protocols.sort(key=lambda x: (x[0], x[1], x[2]))
    # Rebuild sector_to_protocols after sorting
    sector_to_protocols = [[] for _ in range(n)]
    for idx, (a, b, c, mask) in enumerate(protocols):
        sector_to_protocols[a].append(idx)
        sector_to_protocols[b].append(idx)
        sector_to_protocols[c].append(idx)
    
    chosen = []
    
    # Recursive backtracking
    def dfs(covered, remaining):
        if remaining == 0:
            return covered == all_mask
        if covered == all_mask:
            return remaining == 0
        
        # Find the uncovered sector with the fewest available protocols
        best_sector = -1
        best_options = None
        for s in range(n):
            if not (covered >> s) & 1:
                options = [idx for idx in sector_to_protocols[s] if (protocols[idx][3] & covered) == 0]
                if best_sector == -1 or len(options) < len(best_options):
                    best_sector = s
                    best_options = options
                    if len(options) == 0:
                        return False
                    if len(options) == 1:
                        break
        
        for idx in best_options:
            a, b, c, mask = protocols[idx]
            if mask & covered:
                continue
            chosen.append((a+1, b+1, c+1))
            if dfs(covered | mask, remaining - 1):
                return True
            chosen.pop()
        return False
    
    if dfs(0, q):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()