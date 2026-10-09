import sys
sys.setrecursionlimit(10000000)

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
    
    cap = 45  # max plants per greenhouse
    max_budget = 800
    
    # Precompute edge counts between color assignments
    # We'll do backtracking with pruning.
    
    color = [-1] * n
    count = [0, 0, 0]
    budget_used = 0
    
    # Sort vertices by degree descending for better pruning
    order = list(range(n))
    order.sort(key=lambda x: bin(adj[x]).count('1'), reverse=True)
    
    # For pruning: compute max possible edges if we color remaining vertices optimally
    # Not necessary but we can do simple pruning.
    
    def backtrack(idx):
        nonlocal budget_used
        if idx == n:
            return True
        v = order[idx]
        # Try colors
        for c in range(3):
            if count[c] >= cap:
                continue
            # Check toxicity
            ok = True
            extra = 0
            # Count edges to already colored neighbors
            for u in range(n):
                if color[u] != -1 and (adj[v] >> u) & 1:
                    if color[u] == c:
                        ok = False
                        break
                    else:
                        extra += 1
            if not ok:
                continue
            # Check budget
            if budget_used + extra > max_budget:
                continue
            # Assign
            old_color = color[v]
            color[v] = c
            count[c] += 1
            budget_used += extra
            if backtrack(idx + 1):
                return True
            # Undo
            color[v] = old_color
            count[c] -= 1
            budget_used -= extra
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(c + 1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()