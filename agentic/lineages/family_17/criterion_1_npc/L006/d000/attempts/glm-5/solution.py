import sys
input = sys.stdin.readline

def solve():
    q_str = input().split()
    while len(q_str) < 2:
        q_str += input().split()
    q = int(q_str[0])
    t = int(q_str[1])
    
    triples = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        triples.append((a, b, c))
    
    n = 3 * q
    
    # Build adjacency list for each pair
    pair_to_triples = {}
    for idx, (a, b, c) in enumerate(triples):
        pairs = [(a, b), (a, c), (b, c)]
        for p in pairs:
            if p not in pair_to_triples:
                pair_to_triples[p] = []
            pair_to_triples[p].append(idx)
    
    # For each triple, store its pairs
    triple_pairs = []
    for a, b, c in triples:
        triple_pairs.append([(a, b), (a, c), (b, c)])
    
    # State: which triples are used (bitmask if small, set if large)
    # We'll use memoization with frozenset of used triples
    
    # For efficiency, we'll use a greedy approach with backtracking
    # Since n <= 600, we need to be careful
    
    # Let's try a different approach: for each artifact, track which triples contain it
    artifact_to_triples = [[] for _ in range(n + 1)]
    for idx, (a, b, c) in enumerate(triples):
        artifact_to_triples[a].append(idx)
        artifact_to_triples[b].append(idx)
        artifact_to_triples[c].append(idx)
    
    used = [False] * t
    covered = [False] * (n + 1)
    result = []
    
    # Find the artifact with fewest options
    def find_best_artifact():
        best = -1
        best_count = float('inf')
        for i in range(1, n + 1):
            if not covered[i]:
                count = 0
                for idx in artifact_to_triples[i]:
                    if not used[idx]:
                        count += 1
                if count < best_count:
                    best_count = count
                    best = i
                    if count == 0:
                        return best, 0
        return best, best_count
    
    def backtrack(remaining):
        if remaining == 0:
            return True
        
        art, count = find_best_artifact()
        if count == 0:
            return False
        
        # Try each triple containing art
        for idx in artifact_to_triples[art]:
            if used[idx]:
                continue
            a, b, c = triples[idx]
            if covered[a] or covered[b] or covered[c]:
                continue
            
            # Use this triple
            used[idx] = True
            covered[a] = covered[b] = covered[c] = True
            result.append((a, b, c))
            
            if backtrack(remaining - 1):
                return True
            
            # Backtrack
            result.pop()
            covered[a] = covered[b] = covered[c] = False
            used[idx] = False
        
        return False
    
    if backtrack(q):
        print("YES")
        for triple in result:
            print(triple[0], triple[1], triple[2])
    else:
        print("NO")

solve()