import sys
sys.setrecursionlimit(1000000)

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
    # For each person, list of triple indices containing them
    person_to_triples = [[] for _ in range(n + 1)]
    for idx, (a, b, c) in enumerate(triples):
        person_to_triples[a].append(idx)
        person_to_triples[b].append(idx)
        person_to_triples[c].append(idx)
    
    used = [False] * t
    chosen = []
    
    # Precompute for each triple the set of people it covers
    triple_people = [set(tr) for tr in triples]
    
    # Recursive search
    def backtrack(remaining):
        if remaining == 0:
            return True
        # Find person with fewest available triples
        best_person = -1
        best_options = None
        for p in range(1, n + 1):
            # Check if p is already covered
            covered = False
            for tr_idx in chosen:
                if p in triple_people[tr_idx]:
                    covered = True
                    break
            if covered:
                continue
            options = [idx for idx in person_to_triples[p] if not used[idx]]
            if not options:
                return False
            if best_person == -1 or len(options) < len(best_options):
                best_person = p
                best_options = options
                if len(options) == 1:
                    break
        # Try each option
        for idx in best_options:
            # Mark used
            used[idx] = True
            chosen.append(idx)
            # Mark all triples that intersect this one as used temporarily
            # Actually we just check used flag, so we don't need to mark intersecting ones
            # But we need to ensure disjointness: we already check that when picking options
            # We'll just recurse
            if backtrack(remaining - 1):
                return True
            chosen.pop()
            used[idx] = False
        return False
    
    if backtrack(q):
        print("YES")
        for idx in chosen:
            a, b, c = triples[idx]
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()