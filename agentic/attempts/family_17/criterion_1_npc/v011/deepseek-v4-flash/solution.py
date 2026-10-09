import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q

    cases = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        cases.append((a, b, c))

    # For each artifact, list of case indices that contain it
    artifact_to_cases = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(cases):
        artifact_to_cases[a].append(idx)
        artifact_to_cases[b].append(idx)
        artifact_to_cases[c].append(idx)

    used = [False] * n
    chosen = []

    # Precompute case masks for speed
    case_masks = []
    for a, b, c in cases:
        case_masks.append((1 << a) | (1 << b) | (1 << c))

    # Recursive backtracking
    def backtrack(remaining):
        if remaining == 0:
            return True
        # Find artifact with fewest available cases
        best_artifact = -1
        best_options = None
        for art in range(n):
            if not used[art]:
                options = [ci for ci in artifact_to_cases[art] if not (used[art] or used[cases[ci][1]] or used[cases[ci][2]])]
                # Actually we need to check all three not used
                options = []
                for ci in artifact_to_cases[art]:
                    a, b, c = cases[ci]
                    if not used[a] and not used[b] and not used[c]:
                        options.append(ci)
                if best_artifact == -1 or len(options) < len(best_options):
                    best_artifact = art
                    best_options = options
                    if len(options) == 0:
                        return False
        # Try each option
        for ci in best_options:
            a, b, c = cases[ci]
            used[a] = used[b] = used[c] = True
            chosen.append(ci)
            if backtrack(remaining - 3):
                return True
            chosen.pop()
            used[a] = used[b] = used[c] = False
        return False

    if backtrack(n):
        print("YES")
        for ci in chosen:
            a, b, c = cases[ci]
            print(a + 1, b + 1, c + 1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()