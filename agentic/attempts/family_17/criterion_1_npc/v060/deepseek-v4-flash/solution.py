import sys
sys.setrecursionlimit(1000000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx]) - 1
        b = int(input_data[idx+1]) - 1
        c = int(input_data[idx+2]) - 1
        idx += 3
        mask = (1 << a) | (1 << b) | (1 << c)
        triples.append((mask, (a+1, b+1, c+1)))
    
    total_mask = (1 << (3*q)) - 1
    
    # Candidates for each fragment
    cand = [[] for _ in range(3*q)]
    for i, (mask, _) in enumerate(triples):
        for f in range(3*q):
            if mask & (1 << f):
                cand[f].append(i)
    
    # Sort candidate lists by size for better pruning
    for f in range(3*q):
        cand[f].sort(key=lambda i: bin(triples[i][0]).count("1"))
    
    used = [False] * t
    chosen = []
    
    def backtrack(covered):
        if covered == total_mask:
            return True
        # Choose uncovered fragment with minimum candidates
        best_f = -1
        best_candidates = None
        for f in range(3*q):
            if not (covered >> f) & 1:
                possible = [i for i in cand[f] if not used[i] and (covered & triples[i][0]) == 0]
                if len(possible) == 0:
                    return False
                if best_f == -1 or len(possible) < len(best_candidates):
                    best_f = f
                    best_candidates = possible
                    if len(possible) == 1:
                        break
        # Try each candidate
        for idx in best_candidates:
            mask, nums = triples[idx]
            used[idx] = True
            chosen.append(nums)
            if backtrack(covered | mask):
                return True
            chosen.pop()
            used[idx] = False
        return False
    
    if backtrack(0):
        print("YES")
        for nums in chosen:
            print(*nums)
    else:
        print("NO")

if __name__ == "__main__":
    solve()