import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q
    
    triplets = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triplets.append((a, b, c))
    
    # Build adjacency: for each module, list of triplet indices containing it
    adj = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(triplets):
        adj[a].append(idx)
        adj[b].append(idx)
        adj[c].append(idx)
    
    used = [False] * n
    chosen = []
    
    # Precompute mask for each triplet
    masks = []
    for a, b, c in triplets:
        masks.append((1 << a) | (1 << b) | (1 << c))
    
    # Recursive backtracking
    def backtrack(start):
        if len(chosen) == q:
            return True
        # Find first unused module
        first = -1
        for i in range(start, n):
            if not used[i]:
                first = i
                break
        if first == -1:
            return False
        
        # Try triplets containing this module
        for idx in adj[first]:
            a, b, c = triplets[idx]
            if used[a] or used[b] or used[c]:
                continue
            # Choose
            used[a] = used[b] = used[c] = True
            chosen.append((a+1, b+1, c+1))
            if backtrack(first + 1):
                return True
            # Backtrack
            chosen.pop()
            used[a] = used[b] = used[c] = False
        return False
    
    if backtrack(0):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()