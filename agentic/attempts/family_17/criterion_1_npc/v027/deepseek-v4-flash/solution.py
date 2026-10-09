import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q

    chords = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        chords.append((a, b, c))

    # Precompute chords per frequency
    freq_to_chords = [[] for _ in range(n + 1)]
    for idx, (a, b, c) in enumerate(chords):
        freq_to_chords[a].append(idx)
        freq_to_chords[b].append(idx)
        freq_to_chords[c].append(idx)

    used = [False] * (n + 1)
    selected = []

    def backtrack():
        if len(selected) == q:
            return True
        # Find first unused frequency
        first = None
        for f in range(1, n + 1):
            if not used[f]:
                first = f
                break
        if first is None:
            return False

        for idx in freq_to_chords[first]:
            a, b, c = chords[idx]
            if used[a] or used[b] or used[c]:
                continue
            # Use this chord
            used[a] = used[b] = used[c] = True
            selected.append((a, b, c))
            if backtrack():
                return True
            # Backtrack
            selected.pop()
            used[a] = used[b] = used[c] = False
        return False

    if backtrack():
        print("YES")
        for a, b, c in selected:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()