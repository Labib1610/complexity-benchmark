import sys

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    n = 3 * q
    crews = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        crews.append((a, b, c))

    # Convert each crew to a bitmask
    crew_masks = []
    for a, b, c in crews:
        mask = (1 << (a-1)) | (1 << (b-1)) | (1 << (c-1))
        crew_masks.append(mask)

    # We'll do exact cover with backtracking + heuristic (choose smallest column)
    # Represent columns as bit positions
    full_mask = (1 << n) - 1

    # Dancing links style – but here we use recursion with bitmask search
    # We'll keep an array of chosen crew indices

    # Precompute for each specialist which crews include them
    specialist_to_crews = [[] for _ in range(n)]
    for idx, mask in enumerate(crew_masks):
        m = mask
        while m:
            lsb = m & -m
            pos = (lsb.bit_length() - 1)
            specialist_to_crews[pos].append(idx)
            m ^= lsb

    chosen = []

    def backtrack(covered):
        if covered == full_mask:
            return True
        # Find specialist with smallest number of candidate crews
        best_pos = -1
        best_options = None
        for i in range(n):
            if (covered >> i) & 1:
                continue
            # candidates = crews that include i and don't conflict with covered
            cand = [ci for ci in specialist_to_crews[i] if (crew_masks[ci] & covered) == 0]
            if best_options is None or len(cand) < len(best_options):
                best_pos = i
                best_options = cand
                if len(cand) == 0:
                    return False
        # Try each candidate crew
        for ci in best_options:
            mask = crew_masks[ci]
            chosen.append(ci)
            if backtrack(covered | mask):
                return True
            chosen.pop()
        return False

    if backtrack(0):
        print("YES")
        for ci in chosen:
            a, b, c = crews[ci]
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()