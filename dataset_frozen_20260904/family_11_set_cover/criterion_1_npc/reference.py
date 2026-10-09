import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    u = int(data[idx]); s = int(data[idx + 1]); k = int(data[idx + 2]); idx += 3

    set_masks = []
    for _ in range(s):
        cnt = int(data[idx]); idx += 1
        mk = 0
        for _ in range(cnt):
            sk = int(data[idx]); idx += 1
            mk |= 1 << (sk - 1)
        set_masks.append(mk)

    full = (1 << u) - 1
    INF = float("inf")
    best = [INF] * (1 << u)
    best[0] = 0
    choice = [None] * (1 << u)

    # Bitmask DP over covered-skill sets. From each reachable mask, extend only
    # by consultants covering the lowest still-uncovered skill.
    for mask in range(1 << u):
        b = best[mask]
        if b == INF or mask == full:
            continue
        low = (~mask) & full
        low_bit = low & -low
        for si in range(s):
            sm = set_masks[si]
            if sm & low_bit:
                nm = mask | sm
                if b + 1 < best[nm]:
                    best[nm] = b + 1
                    choice[nm] = (mask, si)

    if best[full] <= k:
        chosen = []
        cur = full
        while cur != 0:
            pm, si = choice[cur]
            chosen.append(si + 1)
            cur = pm
        chosen = sorted(set(chosen))
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, chosen)) + "\n")
    else:
        sys.stdout.write("NO\n")


main()
