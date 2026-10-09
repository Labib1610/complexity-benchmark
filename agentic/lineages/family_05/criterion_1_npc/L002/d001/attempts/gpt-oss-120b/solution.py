import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    triples_by_input = [[] for _ in range(k)]
    for _ in range(t):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it)) - 1
        triples_by_input[u].append((v, w, u))
    # if any input has no triples, impossible
    for lst in triples_by_input:
        if not lst:
            print("NO")
            return

    # order inputs by fewest options to improve pruning
    order = sorted(range(k), key=lambda x: len(triples_by_input[x]))
    # map from position in recursion to actual input index
    pos2inp = order

    used_out = 0
    used_freq = 0
    solution = [None] * k
    found = False

    # precompute bit for each index
    out_bit = [1 << i for i in range(k)]
    freq_bit = [1 << i for i in range(k)]

    # recursion
    def dfs(depth, used_out, used_freq):
        nonlocal found
        if found:
            return
        if depth == k:
            # all inputs assigned
            print("YES")
            for triple in solution:
                # triple stored as (v,w,u)
                v, w, u = triple
                print(u + 1, v + 1, w + 1)
            found = True
            return
        inp = pos2inp[depth]
        # try each triple for this input that fits
        for v, w, u in triples_by_input[inp]:
            ob = out_bit[v]
            fb = freq_bit[w]
            if (used_out & ob) or (used_freq & fb):
                continue
            solution[depth] = (v, w, u)
            dfs(depth + 1, used_out | ob, used_freq | fb)
            if found:
                return

    dfs(0, 0, 0)
    if not found:
        print("NO")

if __name__ == "__main__":
    solve()