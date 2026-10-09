import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    color = [-1] * n
    
    # Precompute possible colors for each node
    possible = [0b111] * n  # bits 0,1,2 represent colors 1,2,3
    
    # Backtracking with MRV heuristic
    def backtrack(idx):
        if idx == n:
            return True
        # Choose uncolored vertex with fewest possibilities
        best = -1
        best_mask = 0
        for i in range(n):
            if color[i] == -1:
                mask = possible[i]
                if best == -1 or bin(mask).count("1") < bin(best_mask).count("1"):
                    best = i
                    best_mask = mask
        if best == -1:
            return True
        # Try each possible color
        for c in range(3):
            if (best_mask >> c) & 1:
                # Check if valid
                ok = True
                for v in range(n):
                    if (adj[best] >> v) & 1 and color[v] == c:
                        ok = False
                        break
                if not ok:
                    continue
                color[best] = c
                # Save possible states
                old_possible = [possible[i] for i in range(n)]
                # Update constraints
                for v in range(n):
                    if (adj[best] >> v) & 1:
                        possible[v] &= ~(1 << c)
                if backtrack(idx + 1):
                    return True
                # Restore
                color[best] = -1
                for i in range(n):
                    possible[i] = old_possible[i]
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(c + 1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()