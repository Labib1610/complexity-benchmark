import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    triples = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        triples.append((a-1, b-1, c-1))  # 0-indexed

    # Sort triples by some heuristic (e.g., by first value then second)
    triples.sort()

    full_mask = (1 << k) - 1
    chosen = []
    used1 = used2 = used3 = 0

    # Backtracking
    def backtrack(idx, used1, used2, used3, chosen):
        if len(chosen) == k:
            return used1 == full_mask and used2 == full_mask and used3 == full_mask
        if idx >= len(triples):
            return False
        # Prune: if remaining triples not enough
        if len(chosen) + (len(triples) - idx) < k:
            return False

        # Try skipping current triple
        if backtrack(idx+1, used1, used2, used3, chosen):
            return True

        # Try taking current triple if possible
        a, b, c = triples[idx]
        if not (used1 & (1 << a)) and not (used2 & (1 << b)) and not (used3 & (1 << c)):
            chosen.append(triples[idx])
            if backtrack(idx+1, used1 | (1 << a), used2 | (1 << b), used3 | (1 << c), chosen):
                return True
            chosen.pop()
        return False

    if backtrack(0, 0, 0, 0, []):
        print("YES")
        for a, b, c in chosen:
            print(a+1, b+1, c+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()