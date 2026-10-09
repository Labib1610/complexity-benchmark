import sys
sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = []                     # (x, y, z) 0‑based
    by_x = [[] for _ in range(k)]   # indices of triples having this x

    for idx in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x, y, z))
        by_x[x].append(idx)

    # if some x has no candidate, impossible immediately
    for lst in by_x:
        if not lst:
            print("NO")
            return

    # order x-values by fewest candidates (heuristic)
    order = list(range(k))
    order.sort(key=lambda xx: len(by_x[xx]))

    used_y = 0          # bitmask of used y values
    used_z = 0          # bitmask of used z values
    answer = [0] * k    # store chosen triple indices
    found = False

    def dfs(pos: int) -> None:
        nonlocal used_y, used_z, found
        if found:
            return
        if pos == k:
            found = True
            return
        x = order[pos]
        for rid in by_x[x]:
            _, y, z = triples[rid]
            mask_y = 1 << y
            mask_z = 1 << z
            if (used_y & mask_y) or (used_z & mask_z):
                continue
            # choose this triple
            used_y ^= mask_y
            used_z ^= mask_z
            answer[pos] = rid
            dfs(pos + 1)
            if found:
                return
            # backtrack
            used_y ^= mask_y
            used_z ^= mask_z

    dfs(0)

    if not found:
        print("NO")
        return

    print("YES")
    out_lines = []
    for i in range(k):
        x, y, z = triples[answer[i]]
        out_lines.append(f"{x+1} {y+1} {z+1}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()