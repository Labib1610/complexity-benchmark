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
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        triples.append((a, b, c))
    
    n = 3 * q
    # triples_by_num[num] = list of triple indices containing num
    triples_by_num = [[] for _ in range(n + 1)]
    for idx, (a, b, c) in enumerate(triples):
        triples_by_num[a].append(idx)
        triples_by_num[b].append(idx)
        triples_by_num[c].append(idx)
    
    used = [False] * (n + 1)
    chosen = []
    
    # Precompute for each triple the three numbers
    triple_nums = [ (a,b,c) for (a,b,c) in triples ]
    
    # For pruning: count how many triples cover each number
    # We'll just do simple recursion with smallest unused number
    
    def backtrack():
        if len(chosen) == q:
            return True
        # find smallest unused number
        first = 1
        while first <= n and used[first]:
            first += 1
        if first > n:
            return False  # no unused numbers but not enough chosen
        
        # Try each triple containing first
        for idx in triples_by_num[first]:
            a, b, c = triple_nums[idx]
            if used[a] or used[b] or used[c]:
                continue
            # choose this triple
            used[a] = used[b] = used[c] = True
            chosen.append((a, b, c))
            if backtrack():
                return True
            # backtrack
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