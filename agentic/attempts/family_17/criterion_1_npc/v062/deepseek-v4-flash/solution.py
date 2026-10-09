import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    triads = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        triads.append((a, b, c))
    
    # Sort triads by first element for better pruning
    triads.sort()
    
    # Group triads by first person
    by_first = [[] for _ in range(3 * q + 1)]
    for idx, (a, b, c) in enumerate(triads):
        by_first[a].append(idx)
    
    used = [False] * (3 * q + 1)
    chosen = []
    
    def backtrack():
        if len(chosen) == q:
            return True
        # Find first unused person
        first_unused = None
        for i in range(1, 3 * q + 1):
            if not used[i]:
                first_unused = i
                break
        if first_unused is None:
            return False
        
        for idx in by_first[first_unused]:
            a, b, c = triads[idx]
            if used[a] or used[b] or used[c]:
                continue
            # choose
            used[a] = used[b] = used[c] = True
            chosen.append((a, b, c))
            if backtrack():
                return True
            # undo
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