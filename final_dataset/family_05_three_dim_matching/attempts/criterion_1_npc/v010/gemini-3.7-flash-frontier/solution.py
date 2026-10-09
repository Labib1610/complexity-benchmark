import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    t = int(input_data[1])

    triples = []
    masks = []
    idx = 2
    for _ in range(t):
        x = int(input_data[idx]) - 1
        y = int(input_data[idx + 1]) - 1
        z = int(input_data[idx + 2]) - 1
        idx += 3
        triples.append((x, k + y, 2 * k + z))
        mask = (1 << x) | (1 << (k + y)) | (1 << (2 * k + z))
        masks.append(mask)

    if t < k:
        print("NO")
        return

    chosen = []

    def search(active_options, covered_mask):
        if len(chosen) == k:
            return True

        # Count available options for each item among active_options
        item_counts = [0] * (3 * k)
        for opt in active_options:
            u, v, w = triples[opt]
            item_counts[u] += 1
            item_counts[v] += 1
            item_counts[w] += 1

        # Find uncovered item with minimum positive options (or 0 if dead end)
        best_item = -1
        min_count = float("inf")

        for item in range(3 * k):
            if not (covered_mask & (1 << item)):
                c = item_counts[item]
                if c == 0:
                    return False  # An uncovered item has 0 options available
                if c < min_count:
                    min_count = c
                    best_item = item

        if best_item == -1:
            return False

        # Branch on options covering best_item
        branch_options = [
            opt for opt in active_options if triples[opt][0] == best_item or triples[opt][1] == best_item or triples[opt][2] == best_item
        ]

        for opt in branch_options:
            opt_mask = masks[opt]
            chosen.append(opt)

            # Filter active options: must not conflict with opt
            next_active = [o for o in active_options if not (masks[o] & opt_mask)]

            if search(next_active, covered_mask | opt_mask):
                return True

            chosen.pop()

        return False

    initial_active = list(range(t))
    if search(initial_active, 0):
        print("YES")
        out = []
        for opt in chosen:
            u, v, w = triples[opt]
            out.append(f"{u + 1} {v - k + 1} {w - 2 * k + 1}")
        print("\n".join(out))
    else:
        print("NO")


if __name__ == "__main__":
    solve()