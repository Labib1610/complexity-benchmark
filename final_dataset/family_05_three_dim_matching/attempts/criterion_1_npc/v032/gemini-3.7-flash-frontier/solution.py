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
    idx = 2
    for _ in range(t):
        x = int(input_data[idx]) - 1
        y = int(input_data[idx + 1]) - 1
        z = int(input_data[idx + 2]) - 1
        idx += 3
        triples.append((x, y, z))

    num_cols = 3 * k
    col_to_triples = [[] for _ in range(num_cols)]
    triple_masks = []
    for i, (x, y, z) in enumerate(triples):
        m = (1 << x) | (1 << (k + y)) | (1 << (2 * k + z))
        triple_masks.append(m)
        col_to_triples[x].append(i)
        col_to_triples[k + y].append(i)
        col_to_triples[2 * k + z].append(i)

    for c in range(num_cols):
        if not col_to_triples[c]:
            print("NO")
            return

    target_mask = (1 << num_cols) - 1
    solution = []

    def search(used_mask, depth):
        if depth == k:
            return True

        best_count = 1000000
        best_triples = None

        rem = target_mask ^ used_mask
        while rem > 0:
            lsb = rem & -rem
            c = lsb.bit_length() - 1
            rem ^= lsb

            candidates = [
                i for i in col_to_triples[c] if not (triple_masks[i] & used_mask)
            ]
            cnt = len(candidates)
            if cnt == 0:
                return False
            if cnt < best_count:
                best_count = cnt
                best_triples = candidates
                if cnt == 1:
                    break

        for t_idx in best_triples:
            solution.append(t_idx)
            if search(used_mask | triple_masks[t_idx], depth + 1):
                return True
            solution.pop()

        return False

    if search(0, 0):
        print("YES")
        for t_idx in solution:
            x, y, z = triples[t_idx]
            print(f"{x + 1} {y + 1} {z + 1}")
    else:
        print("NO")


if __name__ == "__main__":
    solve()