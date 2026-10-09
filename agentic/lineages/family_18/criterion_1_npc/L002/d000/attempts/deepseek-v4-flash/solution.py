import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
    
    # adjacency list for quick cost calculation
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    best_perm = None
    used = [False] * n
    perm = [0] * n
    pos = [0] * n  # position of each unit in current permutation
    
    def backtrack(idx, cost):
        nonlocal best_perm
        if cost > B:
            return
        if idx == n:
            best_perm = perm[:]
            return True
        for slot in range(n):
            if not used[slot]:
                used[slot] = True
                perm[idx] = slot
                pos[idx] = slot  # actually pos[unit] = slot, but here idx is unit
                # compute added cost
                added = 0
                # We need to know which unit is at idx; unit = idx
                unit = idx
                for nb in adj[unit]:
                    if used[nb]:  # nb already placed
                        added += abs(pos[unit] - pos[nb])
                if cost + added <= B:
                    if backtrack(idx + 1, cost + added):
                        return True
                used[slot] = False
        return False
    
    # Try all starting positions
    if backtrack(0, 0):
        print("YES")
        # best_perm[unit] = slot
        print(' '.join(str(s + 1) for s in best_perm))
    else:
        print("NO")

if __name__ == "__main__":
    main()