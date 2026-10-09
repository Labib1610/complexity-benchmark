import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n, m = int(input_data[0]), int(input_data[1])
    edges = []
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        edges.append((u, v))
    
    # adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n  # 0 = unassigned, 1,2,3 = blocks
    
    # Precompute conflict sets for each vertex
    conflict_masks = [0] * n
    for u in range(n):
        mask = 0
        for v in adj[u]:
            mask |= (1 << v)
        conflict_masks[u] = mask
    
    # Backtracking to find lexicographically smallest coloring
    def backtrack(pos):
        if pos == n:
            return True
        # Try colors 1,2,3 in order for lexicographic smallest
        for c in range(1, 4):
            ok = True
            for v in adj[pos]:
                if color[v] == c:
                    ok = False
                    break
            if ok:
                color[pos] = c
                if backtrack(pos + 1):
                    return True
                color[pos] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()