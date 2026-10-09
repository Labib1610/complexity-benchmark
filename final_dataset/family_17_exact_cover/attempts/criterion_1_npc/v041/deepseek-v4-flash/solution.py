import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q
    triples = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        triples.append((a, b, c))
    
    # Precompute triples per member
    triples_by_member = [[] for _ in range(n + 1)]
    for idx, (a, b, c) in enumerate(triples):
        triples_by_member[a].append(idx)
        triples_by_member[b].append(idx)
        triples_by_member[c].append(idx)
    
    used = [False] * (n + 1)
    chosen = []
    
    # Sort triples by sum of ids to help pruning
    triples_sorted = sorted(range(t), key=lambda i: triples[i])
    
    # We'll use recursion with backtracking
    # To speed up, we can reorder triples list so that triples with smallest first unused member come first
    # But simpler: at each step, find first unused member, then try all triples containing it.
    
    def dfs():
        # Find first unused member
        first = -1
        for i in range(1, n + 1):
            if not used[i]:
                first = i
                break
        if first == -1:
            return True
        # Try all triples containing 'first'
        for idx in triples_by_member[first]:
            a, b, c = triples[idx]
            if not used[a] and not used[b] and not used[c]:
                used[a] = used[b] = used[c] = True
                chosen.append((a, b, c))
                if dfs():
                    return True
                chosen.pop()
                used[a] = used[b] = used[c] = False
        return False
    
    if dfs():
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()