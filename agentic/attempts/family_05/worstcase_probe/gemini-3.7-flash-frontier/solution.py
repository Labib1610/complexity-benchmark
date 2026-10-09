import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    t = int(input_data[1])

    triplets = []
    triplet_mask = []
    item_triplets = [[] for _ in range(3 * k)]

    idx = 2
    for i in range(t):
        x = int(input_data[idx]) - 1
        y = int(input_data[idx + 1]) - 1
        z = int(input_data[idx + 2]) - 1
        idx += 3

        triplets.append((x + 1, y + 1, z + 1))
        mask = (1 << x) | (1 << (k + y)) | (1 << (2 * k + z))
        triplet_mask.append(mask)

        item_triplets[x].append(i)
        item_triplets[k + y].append(i)
        item_triplets[2 * k + z].append(i)

    # If any item has 0 triplets to begin with, impossible
    for item in range(3 * k):
        if not item_triplets[item]:
            print("NO")
            return

    solution = []

    def search(used_mask, depth):
        if depth == k:
            return True

        min_count = 999999
        best_candidates = None

        for item in range(3 * k):
            if not ((used_mask >> item) & 1):
                cands = [
                    t_idx
                    for t_idx in item_triplets[item]
                    if (triplet_mask[t_idx] & used_mask) == 0
                ]
                cnt = len(cands)
                if cnt < min_count:
                    min_count = cnt
                    best_candidates = cands
                    if min_count <= 1:
                        break

        if min_count == 0 or best_candidates is None:
            return False

        for t_idx in best_candidates:
            solution.append(t_idx)
            if search(used_mask | triplet_mask[t_idx], depth + 1):
                return True
            solution.pop()

        return False

    if search(0, 0):
        print("YES")
        out = []
        for t_idx in solution:
            x, y, z = triplets[t_idx]
            out.append(f"{x} {y} {z}")
        print("\n".join(out))
    else:
        print("NO")

if __name__ == "__main__":
    solve()