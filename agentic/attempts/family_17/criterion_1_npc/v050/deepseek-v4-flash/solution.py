import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    n = 3 ** q
    
    triples = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        triples.append((a, b, c))
    
    # If we don't have enough triples to cover all personnel, impossible
    if t < q:
        print("NO")
        return
    
    # If n is huge but t is small, impossible
    # Actually, we can check if the union of all triples covers all personnel
    # But n can be huge, so we can't store all. Instead, we check if any personnel
    # is missing from all triples.
    # Since n can be huge, we only need to check if the max id in triples is less than n
    # or if there are gaps.
    # But we can just try backtracking; if we can't cover, we'll fail.
    
    # Build adjacency: for each person, list of triple indices containing them
    # But n can be huge, so we use dict for only those appearing in triples.
    person_to_triples = {}
    for idx, (a, b, c) in enumerate(triples):
        for p in (a, b, c):
            if p not in person_to_triples:
                person_to_triples[p] = []
            person_to_triples[p].append(idx)
    
    # Check if any person from 1..n is missing from all triples
    # We can't iterate all n if n is huge, but we can check the max id
    # If max id < n, then persons > max id are missing -> impossible
    max_id = max(max(triple) for triple in triples) if triples else 0
    if max_id < n:
        print("NO")
        return
    
    # Also check if any person <= n is missing from triples
    # We can check by seeing if all numbers from 1..n appear in triples
    # But n can be huge, so we only check up to max_id (which is <= n)
    present = set()
    for triple in triples:
        present.update(triple)
    # Check if any number from 1..n is missing
    # We can't iterate all n, but we can check if there's a gap in present set
    # Since n can be huge, we only need to check up to max_id
    # If there's a missing number <= max_id, impossible
    for i in range(1, max_id + 1):
        if i not in present:
            print("NO")
            return
    
    used = [False] * (n + 1)  # This might be huge if n is huge, but n = 3^q, q up to 200 -> impossible to allocate
    # So we need a different approach: use a set for used persons
    used_set = set()
    chosen = []
    
    # We'll do backtracking with pruning
    # Sort triples maybe by size? Not needed.
    
    # We'll pick the smallest unused person each time
    # But we can't iterate all n if n is huge. We'll only consider persons that appear in triples.
    # Actually, we can maintain a pointer to the smallest unused person among those in triples.
    # But if n is huge and some persons are missing, we already returned NO.
    # So all persons 1..n appear in at least one triple.
    # But n can be huge, so we can't store used array of size n+1.
    # Instead, we use a set for used persons.
    
    # We'll sort triples by their smallest element to help with pruning.
    triples_sorted = sorted(triples, key=lambda x: (x[0], x[1], x[2]))
    
    # We'll also build a mapping from person to list of triple indices (in sorted order)
    person_to_triples_sorted = {}
    for idx, (a, b, c) in enumerate(triples_sorted):
        for p in (a, b, c):
            if p not in person_to_triples_sorted:
                person_to_triples_sorted[p] = []
            person_to_triples_sorted[p].append(idx)
    
    # We'll use a recursive function
    # We need to find the smallest unused person. Since n can be huge, we can't scan from 1 each time.
    # But we can maintain a pointer to the smallest unused person among those in triples.
    # Since all persons 1..n appear, we can just start from 1 and increment until we find unused.
    # But n can be huge, so we can't loop over all. However, we only need to find the smallest unused
    # among those that are still possible. We can maintain a set of unused persons that appear in triples.
    # But that set could be huge (up to n). However, n = 3^q, q up to 200 -> impossible.
    # So we need a smarter approach.
    
    # Observation: The number of triples is at most 20000, so the number of distinct persons is at most 60000.
    # But n can be much larger. If n > 60000, then there are persons not in any triple -> impossible.
    # So we can check: if n > 60000, then impossible because we have at most 60000 distinct persons.
    # Actually, n = 3^q, q up to 200, so n can be astronomically large. But t <= 20000, so distinct persons <= 60000.
    # If n > 60000, then there are persons not in any triple -> impossible.
    # So we can early return NO.
    
    distinct_persons = len(present)
    if distinct_persons < n:
        print("NO")
        return
    
    # Now n <= 60000, so we can allocate used array.
    used = [False] * (n + 1)
    
    # We'll sort triples by smallest element for better pruning.
    triples_sorted = sorted(triples, key=lambda x: (x[0], x[1], x[2]))
    
    # Build adjacency
    person_to_triples = {}
    for idx, (a, b, c) in enumerate(triples_sorted):
        for p in (a, b, c):
            if p not in person_to_triples:
                person_to_triples[p] = []
            person_to_triples[p].append(idx)
    
    chosen = []
    
    def backtrack(count):
        if count == q:
            return True
        # Find smallest unused person
        # We can scan from 1 to n, but n <= 60000, so it's fine
        for p in range(1, n + 1):
            if not used[p]:
                break
        else:
            return False  # no unused person, but count < q -> impossible
        
        # Try all triples containing p
        for idx in person_to_triples.get(p, []):
            a, b, c = triples_sorted[idx]
            if used[a] or used[b] or used[c]:
                continue
            # Use this triple
            used[a] = used[b] = used[c] = True
            chosen.append((a, b, c))
            if backtrack(count + 1):
                return True
            # Backtrack
            chosen.pop()
            used[a] = used[b] = used[c] = False
        return False
    
    if backtrack(0):
        print("YES")
        for triple in chosen:
            print(*triple)
    else:
        print("NO")

if __name__ == "__main__":
    solve()