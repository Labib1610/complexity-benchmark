import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    crit = [int(next(it)) - 1 for _ in range(t)]
    crit_index = {c: i for i, c in enumerate(crit)}
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        mask = 0
        if u in crit_index:
            mask ^= 1 << crit_index[u]
        if v in crit_index:
            mask ^= 1 << crit_index[v]
        if mask:  # only edges that affect critical nodes
            edges.append((w, mask))
    if t <= 1:
        print(0)
        return
    edges.sort(key=lambda x: x[0])
    basis = [0] * t          # basis[i] has leading bit i
    rank = 0
    total = 0
    for w, mask in edges:
        cur = mask
        # try to insert into basis
        for bit in range(t - 1, -1, -1):
            if (cur >> bit) & 1:
                if basis[bit]:
                    cur ^= basis[bit]
                else:
                    basis[bit] = cur
                    rank += 1
                    total += w
                    break
        if rank == t - 1:
            break
    print(total)

if __name__ == "__main__":
    solve()