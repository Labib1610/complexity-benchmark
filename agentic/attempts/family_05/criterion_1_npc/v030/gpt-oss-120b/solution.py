import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    triples = []
    by_x = [[] for _ in range(k)]
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x, y, z))
        by_x[x].append((y, z, len(triples) - 1))   # store index for output

    used_x = 0
    used_y = 0
    used_z = 0
    selected = []

    # precompute order of x to try: those with fewest candidates first
    order_x = sorted(range(k), key=lambda i: len(by_x[i]))

    # map from x to its position in order_x for quick skip
    pos_in_order = {x: i for i, x in enumerate(order_x)}

    def dfs(depth: int) -> bool:
        nonlocal used_x, used_y, used_z
        if depth == k:
            return True

        # choose next unused x with minimal branching
        best_x = -1
        best_options = None
        for x in order_x:
            if not (used_x >> x) & 1:
                opts = []
                for y, z, idx in by_x[x]:
                    if ((used_y >> y) & 1) or ((used_z >> z) & 1):
                        continue
                    opts.append((y, z, idx))
                if not opts:
                    return False
                if best_options is None or len(opts) < len(best_options):
                    best_x = x
                    best_options = opts
                    if len(best_options) == 1:
                        break
        # try each option
        for y, z, idx in best_options:
            # place
            used_x ^= 1 << best_x
            used_y ^= 1 << y
            used_z ^= 1 << z
            selected.append(idx)
            if dfs(depth + 1):
                return True
            # backtrack
            selected.pop()
            used_x ^= 1 << best_x
            used_y ^= 1 << y
            used_z ^= 1 << z
        return False

    if dfs(0):
        out = ["YES"]
        for idx in selected:
            x, y, z = triples[idx]
            out.append(f"{x+1} {y+1} {z+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()