import sys

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    n = 3 * q
    triples = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        triples.append((a, b, c))

    # For each crystal, list of triples containing it
    covering = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(triples):
        covering[a].append(i)
        covering[b].append(i)
        covering[c].append(i)

    used_triples = [False] * t
    used_crystals = [False] * (n + 1)
    chosen = []

    # Backtracking search with heuristic: pick the smallest unused crystal
    def backtrack():
        if len(chosen) == q:
            return True
        # Find first unused crystal
        try:
            v = next(i for i in range(1, n + 1) if not used_crystals[i])
        except StopIteration:
            return False
        for idx in covering[v]:
            if used_triples[idx]:
                continue
            a, b, c = triples[idx]
            if used_crystals[a] or used_crystals[b] or used_crystals[c]:
                continue
            # Use this triple
            used_triples[idx] = True
            used_crystals[a] = used_crystals[b] = used_crystals[c] = True
            chosen.append((a, b, c))
            if backtrack():
                return True
            # Backtrack
            chosen.pop()
            used_crystals[a] = used_crystals[b] = used_crystals[c] = False
            used_triples[idx] = False
        return False

    if backtrack():
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()