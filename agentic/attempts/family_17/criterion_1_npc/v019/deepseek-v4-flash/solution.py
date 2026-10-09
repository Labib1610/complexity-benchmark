import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q
    triples = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))
    
    # For each item, list of triple indices that contain it
    item_to_triples = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(triples):
        item_to_triples[a].append(idx)
        item_to_triples[b].append(idx)
        item_to_triples[c].append(idx)
    
    used = [False] * n
    chosen = []
    
    def backtrack():
        if len(chosen) == q:
            return True
        # Find first unused item
        first = -1
        for i in range(n):
            if not used[i]:
                first = i
                break
        if first == -1:
            return False
        
        # Try all triples containing first
        for idx in item_to_triples[first]:
            a, b, c = triples[idx]
            if used[a] or used[b] or used[c]:
                continue
            # Use this triple
            used[a] = used[b] = used[c] = True
            chosen.append((a+1, b+1, c+1))
            if backtrack():
                return True
            # Backtrack
            chosen.pop()
            used[a] = used[b] = used[c] = False
        return False
    
    if backtrack():
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()