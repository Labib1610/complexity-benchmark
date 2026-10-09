import sys
sys.setrecursionlimit(1000000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q
    
    triads = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triads.append((a, b, c))
    
    # For each item, list of triad indices that contain it
    item_to_triads = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(triads):
        item_to_triads[a].append(idx)
        item_to_triads[b].append(idx)
        item_to_triads[c].append(idx)
    
    used = [False] * t
    chosen = []
    covered = [False] * n
    remaining_count = n
    
    # Precompute triad item lists for quick access
    triad_items = [set(tri) for tri in triads]
    
    def backtrack():
        nonlocal remaining_count
        if remaining_count == 0:
            return True
        # Find uncovered item with fewest candidate triads
        best_item = -1
        best_list = None
        for i in range(n):
            if not covered[i]:
                cand = [idx for idx in item_to_triads[i] if not used[idx]]
                if best_item == -1 or len(cand) < len(best_list):
                    best_item = i
                    best_list = cand
                    if len(best_list) == 0:
                        return False
                    if len(best_list) == 1:
                        break
        # Try each candidate triad
        for idx in best_list:
            a, b, c = triads[idx]
            if covered[a] or covered[b] or covered[c]:
                continue
            # Place triad
            used[idx] = True
            chosen.append(idx)
            for x in (a, b, c):
                covered[x] = True
            remaining_count -= 3
            
            if backtrack():
                return True
            
            # Undo
            remaining_count += 3
            for x in (a, b, c):
                covered[x] = False
            chosen.pop()
            used[idx] = False
        return False
    
    if backtrack():
        print("YES")
        for idx in chosen:
            a, b, c = triads[idx]
            print(a+1, b+1, c+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()