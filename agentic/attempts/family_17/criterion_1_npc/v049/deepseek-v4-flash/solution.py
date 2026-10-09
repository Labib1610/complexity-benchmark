import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    triples = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        triples.append((a,b,c))
    
    n = 3 * q
    
    # For each number, list of indices of triples containing it
    by_num = [[] for _ in range(n+1)]
    for idx, (a,b,c) in enumerate(triples):
        by_num[a].append(idx)
        by_num[b].append(idx)
        by_num[c].append(idx)
    
    used = [False] * (n+1)
    chosen = []
    
    # MRV: find smallest uncovered number with minimal candidates
    def find_next():
        best_num = -1
        best_count = None
        for num in range(1, n+1):
            if not used[num]:
                # count available triples for this num (those that are fully unused)
                cnt = 0
                for idx in by_num[num]:
                    a,b,c = triples[idx]
                    if not used[a] and not used[b] and not used[c]:
                        cnt += 1
                if cnt == 0:
                    return -1
                if best_count is None or cnt < best_count:
                    best_count = cnt
                    best_num = num
                    if cnt == 1:
                        break
        return best_num
    
    def backtrack():
        if len(chosen) == q:
            return True
        num = find_next()
        if num == -1:
            return False
        
        # sort candidate triples by fewest conflicts? simpler: just try in order
        for idx in by_num[num]:
            a,b,c = triples[idx]
            if used[a] or used[b] or used[c]:
                continue
            # choose
            used[a] = used[b] = used[c] = True
            chosen.append(idx)
            if backtrack():
                return True
            # undo
            chosen.pop()
            used[a] = used[b] = used[c] = False
        
        return False
    
    if backtrack():
        out = ["YES"]
        for idx in chosen:
            a,b,c = triples[idx]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()