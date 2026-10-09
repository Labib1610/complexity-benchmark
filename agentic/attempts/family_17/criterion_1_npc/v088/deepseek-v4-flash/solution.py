import sys

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    triples = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        triples.append((a, b, c))
    
    n = 3 * q
    # For each number, list of triple indices containing it
    num_to_triples = [[] for _ in range(n + 1)]
    for idx, (a, b, c) in enumerate(triples):
        num_to_triples[a].append(idx)
        num_to_triples[b].append(idx)
        num_to_triples[c].append(idx)
    
    used = [False] * t
    covered = [False] * (n + 1)
    chosen = []
    
    def backtrack():
        if len(chosen) == q:
            return True
        # Find uncovered number with fewest candidate triples
        best_num = -1
        best_candidates = None
        for num in range(1, n + 1):
            if not covered[num]:
                cand = [idx for idx in num_to_triples[num] if not used[idx]]
                if not cand:
                    return False
                if best_candidates is None or len(cand) < len(best_candidates):
                    best_candidates = cand
                    best_num = num
                    if len(cand) == 1:
                        break
        if best_num == -1:
            return False
        
        for idx in best_candidates:
            a, b, c = triples[idx]
            # Check if all numbers are uncovered
            if covered[a] or covered[b] or covered[c]:
                continue
            # Use this triple
            used[idx] = True
            covered[a] = covered[b] = covered[c] = True
            chosen.append((a, b, c))
            
            if backtrack():
                return True
            
            # Backtrack
            chosen.pop()
            covered[a] = covered[b] = covered[c] = False
            used[idx] = False
        
        return False
    
    if backtrack():
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()