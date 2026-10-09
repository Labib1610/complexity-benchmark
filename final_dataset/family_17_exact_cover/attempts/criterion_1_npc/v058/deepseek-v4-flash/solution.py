import sys

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    triples = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        triples.append((a, b, c))
    
    # Sort triples by first element for better pruning
    triples.sort()
    
    used = [False] * (3*q + 1)
    chosen = []
    
    # Precompute for each person the list of triples containing them
    by_person = [[] for _ in range(3*q + 1)]
    for idx, (a, b, c) in enumerate(triples):
        by_person[a].append(idx)
        by_person[b].append(idx)
        by_person[c].append(idx)
    
    def backtrack(count):
        if count == q:
            return True
        # Find first unused person
        first = 1
        while first <= 3*q and used[first]:
            first += 1
        if first > 3*q:
            return False
        
        # Try triples containing first
        for idx in by_person[first]:
            a, b, c = triples[idx]
            if not used[a] and not used[b] and not used[c]:
                used[a] = used[b] = used[c] = True
                chosen.append((a, b, c))
                if backtrack(count + 1):
                    return True
                chosen.pop()
                used[a] = used[b] = used[c] = False
        return False
    
    if backtrack(0):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()