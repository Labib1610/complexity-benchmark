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
    for _ in range(t):
        m = int(next(it)) - 1
        p = int(next(it)) - 1
        s = int(next(it)) - 1
        triples.append((m, p, s))

    # index triples by each component
    by_mem = [[] for _ in range(k)]
    by_path = [[] for _ in range(k)]
    by_seq = [[] for _ in range(k)]
    for idx, (m, p, s) in enumerate(triples):
        by_mem[m].append(idx)
        by_path[p].append(idx)
        by_seq[s].append(idx)

    used_mem = 0
    used_path = 0
    used_seq = 0
    solution = [None] * k  # store indices of chosen triples

    # precompute popcount for heuristic ordering
    full_mask = (1 << k) - 1

    def count_bits(x):
        return x.bit_count()

    # recursive search
    def dfs(depth, used_mem, used_path, used_seq):
        if depth == k:
            return True
        # choose the most constrained unused element among three sides
        # compute candidates for each unused element
        best_elem = None
        best_type = None
        best_list = None
        best_count = None

        # membranes
        um = (~used_mem) & full_mask
        while um:
            v = (um & -um).bit_length() - 1
            um &= um - 1
            cand = []
            for idx in by_mem[v]:
                m, p, s = triples[idx]
                if (used_path >> p) & 1: continue
                if (used_seq >> s) & 1: continue
                cand.append(idx)
            c = len(cand)
            if c == 0:
                return False
            if best_count is None or c < best_count:
                best_count = c
                best_elem = v
                best_type = 0
                best_list = cand
                if c == 1:
                    break

        if best_count != 1:  # maybe we can find better on other sides
            # pathways
            up = (~used_path) & full_mask
            while up:
                v = (up & -up).bit_length() - 1
                up &= up - 1
                cand = []
                for idx in by_path[v]:
                    m, p, s = triples[idx]
                    if (used_mem >> m) & 1: continue
                    if (used_seq >> s) & 1: continue
                    cand.append(idx)
                c = len(cand)
                if c == 0:
                    return False
                if best_count is None or c < best_count:
                    best_count = c
                    best_elem = v
                    best_type = 1
                    best_list = cand
                    if c == 1:
                        break

            # sequences
            us = (~used_seq) & full_mask
            while us:
                v = (us & -us).bit_length() - 1
                us &= us - 1
                cand = []
                for idx in by_seq[v]:
                    m, p, s = triples[idx]
                    if (used_mem >> m) & 1: continue
                    if (used_path >> p) & 1: continue
                    cand.append(idx)
                c = len(cand)
                if c == 0:
                    return False
                if best_count is None or c < best_count:
                    best_count = c
                    best_elem = v
                    best_type = 2
                    best_list = cand
                    if c == 1:
                        break

        # try candidates
        for idx in best_list:
            m, p, s = triples[idx]
            if (used_mem >> m) & 1: continue
            if (used_path >> p) & 1: continue
            if (used_seq >> s) & 1: continue
            solution[depth] = idx
            if dfs(depth + 1,
                   used_mem | (1 << m),
                   used_path | (1 << p),
                   used_seq | (1 << s)):
                return True
        return False

    if dfs(0, 0, 0, 0):
        out = ["YES"]
        for idx in solution:
            m, p, s = triples[idx]
            out.append(f"{m+1} {p+1} {s+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()