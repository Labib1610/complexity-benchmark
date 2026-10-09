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
        mask = (1 << a) | (1 << b) | (1 << c)
        triples.append(mask)
    
    # Group triples by the smallest index person they contain
    by_person = [[] for _ in range(n)]
    for idx, mask in enumerate(triples):
        # find first set bit
        first = (mask & -mask).bit_length() - 1
        by_person[first].append(idx)
    
    full_mask = (1 << n) - 1
    memo = {}
    chosen = []
    
    def dfs(mask):
        if mask == 0:
            return True
        if mask in memo:
            return False
        # find first uncovered person
        first = (mask & -mask).bit_length() - 1
        for idx in by_person[first]:
            triple_mask = triples[idx]
            if (triple_mask & mask) == triple_mask:
                chosen.append(idx)
                if dfs(mask ^ triple_mask):
                    return True
                chosen.pop()
        memo[mask] = False
        return False
    
    if dfs(full_mask):
        print("YES")
        for idx in chosen:
            m = triples[idx]
            # extract the three ids
            ids = []
            for i in range(n):
                if m & (1 << i):
                    ids.append(str(i + 1))
            print(" ".join(ids))
    else:
        print("NO")

if __name__ == "__main__":
    solve()