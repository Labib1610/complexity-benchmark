import sys

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    n = 3 * q
    blueprints = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        blueprints.append((a - 1, b - 1, c - 1))
    
    # Build adjacency: for each relic, list of blueprint indices containing it
    relic_to_bp = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(blueprints):
        relic_to_bp[a].append(idx)
        relic_to_bp[b].append(idx)
        relic_to_bp[c].append(idx)
    
    used = [False] * t
    chosen = []
    covered = 0
    
    # We'll use recursion with pruning
    def backtrack():
        nonlocal covered
        if covered == n:
            return True
        # Find first uncovered relic
        relic = -1
        for i in range(n):
            if not (covered >> i) & 1:
                relic = i
                break
        # Try blueprints containing this relic
        for bp_idx in relic_to_bp[relic]:
            if used[bp_idx]:
                continue
            a, b, c = blueprints[bp_idx]
            if (covered >> a) & 1 or (covered >> b) & 1 or (covered >> c) & 1:
                continue
            # Choose this blueprint
            used[bp_idx] = True
            chosen.append(bp_idx)
            covered |= (1 << a) | (1 << b) | (1 << c)
            if backtrack():
                return True
            # Undo
            covered &= ~((1 << a) | (1 << b) | (1 << c))
            chosen.pop()
            used[bp_idx] = False
        return False
    
    if backtrack():
        print("YES")
        for idx in chosen:
            a, b, c = blueprints[idx]
            print(a + 1, b + 1, c + 1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()