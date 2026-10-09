import sys

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    n = 3 * q
    triples = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        triples.append((a-1, b-1, c-1))
    
    # For each artifact, list of triples containing it
    by_artifact = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(triples):
        by_artifact[a].append(idx)
        by_artifact[b].append(idx)
        by_artifact[c].append(idx)
    
    # Precompute bitmask for each triple
    masks = []
    for a, b, c in triples:
        masks.append((1 << a) | (1 << b) | (1 << c))
    
    full_mask = (1 << n) - 1
    chosen = []
    
    # Recursive backtracking
    def dfs(covered):
        if covered == full_mask:
            return True
        # Find uncovered artifact with fewest options
        best_artifact = -1
        best_options = None
        for i in range(n):
            if not (covered >> i) & 1:
                options = [idx for idx in by_artifact[i] if not (covered & masks[idx])]
                if best_artifact == -1 or len(options) < len(best_options):
                    best_artifact = i
                    best_options = options
                    if len(options) == 0:
                        return False
                    if len(options) == 1:
                        break
        # Try each option
        for idx in best_options:
            chosen.append(idx)
            if dfs(covered | masks[idx]):
                return True
            chosen.pop()
        return False
    
    if dfs(0):
        print("YES")
        for idx in chosen:
            a, b, c = triples[idx]
            print(a+1, b+1, c+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()