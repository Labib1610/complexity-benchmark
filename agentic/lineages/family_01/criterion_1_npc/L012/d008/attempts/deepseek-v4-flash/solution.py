import sys
sys.setrecursionlimit(10000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n  # 0 = uncolored, 1,2,3 = colors
    
    # Check if we can color the remaining nodes given current partial assignment
    def can_color_remaining():
        # Simple backtracking for remaining nodes
        # Find first uncolored node
        uncolored = [i for i in range(n) if color[i] == 0]
        if not uncolored:
            return True
        # Try to color them
        def backtrack(idx):
            if idx == len(uncolored):
                return True
            node = uncolored[idx]
            used = {color[nei] for nei in adj[node] if color[nei] != 0}
            for c in (1,2,3):
                if c not in used:
                    color[node] = c
                    if backtrack(idx+1):
                        return True
                    color[node] = 0
            return False
        return backtrack(0)
    
    # Main backtracking for lexicographically smallest
    def dfs(pos):
        if pos == n:
            return True
        for c in (1,2,3):
            # Check neighbors
            ok = True
            for nei in adj[pos]:
                if color[nei] == c:
                    ok = False
                    break
            if not ok:
                continue
            color[pos] = c
            # Prune: check if remaining can still be colored
            if can_color_remaining():
                if dfs(pos+1):
                    return True
            color[pos] = 0
        return False
    
    if dfs(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()