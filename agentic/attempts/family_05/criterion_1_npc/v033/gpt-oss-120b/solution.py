import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    allowed = [[] for _ in range(k)]          # per specialist (0‑based) list of (machine, time)
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        allowed[x].append((y, z))

    full_mask = (1 << k) - 1

    # dp maps machine_mask -> time_mask reachable after processing some specialists
    dp = {0: 0}
    # predecessor info for reconstruction
    pred = {(0, 0): None}

    for s in range(k):
        newdp = {}
        for m_mask, z_mask in dp.items():
            for y, z in allowed[s]:
                if (m_mask >> y) & 1:   # machine already used
                    continue
                if (z_mask >> z) & 1:   # time already used
                    continue
                nm = m_mask | (1 << y)
                nz = z_mask | (1 << z)
                key = (nm, nz)
                if key not in pred:      # store first found way
                    pred[key] = (m_mask, y, z)
                    newdp[nm] = nz
        dp = newdp
        if not dp:          # no states left, impossible early
            print("NO")
            return

    # look for full masks
    for m_mask, z_mask in dp.items():
        if m_mask == full_mask and z_mask == full_mask:
            # reconstruct
            res = [None] * k
            cur_m, cur_z = m_mask, z_mask
            for s_rev in range(k - 1, -1, -1):
                prev_m, y, z = pred[(cur_m, cur_z)]
                res[s_rev] = (s_rev + 1, y + 1, z + 1)
                cur_m, cur_z = prev_m, cur_z
            print("YES")
            out = sys.stdout.write
            for a, b, c in res:
                out(f"{a} {b} {c}\n")
            return

    print("NO")

if __name__ == "__main__":
    solve()