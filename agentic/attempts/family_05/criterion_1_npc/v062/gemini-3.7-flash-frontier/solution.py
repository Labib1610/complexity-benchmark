import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    t = int(input_data[1])

    if t < k:
        print("NO")
        return

    pathways = []
    idx = 2
    for i in range(t):
        x = int(input_data[idx]) - 1
        y = int(input_data[idx + 1]) - 1 + k
        z = int(input_data[idx + 2]) - 1 + 2 * k
        pathways.append((x, y, z))
        idx += 3

    num_items = 3 * k
    item_opts = [[] for _ in range(num_items)]

    for opt_id, (x, y, z) in enumerate(pathways):
        item_opts[x].append(((1 << y) | (1 << z), opt_id))
        item_opts[y].append(((1 << x) | (1 << z), opt_id))
        item_opts[z].append(((1 << x) | (1 << y), opt_id))

    for i in range(num_items):
        if not item_opts[i]:
            print("NO")
            return

    selected = []
    covered = 0
    all_items = list(range(num_items))

    def search():
        nonlocal covered
        if len(selected) == k:
            return True

        best_item = -1
        min_count = 1000000
        best_valid_opts = None

        for item in all_items:
            if not (covered & (1 << item)):
                count = 0
                valid_opts = []
                for other_mask, opt_id in item_opts[item]:
                    if not (covered & other_mask):
                        count += 1
                        valid_opts.append((other_mask, opt_id))
                if count == 0:
                    return False
                if count < min_count:
                    min_count = count
                    best_item = item
                    best_valid_opts = valid_opts
                    if count == 1:
                        # Continue checking other items to ensure no item has count 0
                        pass

        for other_mask, opt_id in best_valid_opts:
            if not (covered & other_mask):
                mask = (1 << best_item) | other_mask
                covered |= mask
                selected.append(opt_id)
                if search():
                    return True
                selected.pop()
                covered ^= mask

        return False

    if search():
        print("YES")
        for opt_id in selected:
            x, y, z = pathways[opt_id]
            print(f"{x + 1} {y - k + 1} {z - 2 * k + 1}")
    else:
        print("NO")


if __name__ == "__main__":
    solve()