import sys

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    n = 3 * q
    reactions = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        reactions.append((a-1, b-1, c-1))
    
    # Build adjacency: for each cluster, list of reaction indices that contain it
    adj = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(reactions):
        adj[a].append(idx)
        adj[b].append(idx)
        adj[c].append(idx)
    
    used = [False] * t
    chosen = []
    covered = 0
    full_mask = (1 << n) - 1
    
    # We'll use a recursive backtracking with bitmask for covered clusters
    # But n up to 600, so bitmask of 600 bits is fine in Python int.
    
    def backtrack(mask):
        nonlocal covered
        if mask == full_mask:
            return True
        # Find first uncovered cluster
        # We can find the lowest uncovered bit
        # Since n <= 600, we can loop
        for i in range(n):
            if not (mask >> i) & 1:
                first = i
                break
        # Try reactions containing this cluster
        for ridx in adj[first]:
            if used[ridx]:
                continue
            a, b, c = reactions[ridx]
            if (mask >> a) & 1 or (mask >> b) & 1 or (mask >> c) & 1:
                continue
            # Use it
            used[ridx] = True
            chosen.append(ridx)
            new_mask = mask | (1 << a) | (1 << b) | (1 << c)
            if backtrack(new_mask):
                return True
            # Backtrack
            chosen.pop()
            used[ridx] = False
        return False
    
    if backtrack(0):
        print("YES")
        for ridx in chosen:
            a, b, c = reactions[ridx]
            print(a+1, b+1, c+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()