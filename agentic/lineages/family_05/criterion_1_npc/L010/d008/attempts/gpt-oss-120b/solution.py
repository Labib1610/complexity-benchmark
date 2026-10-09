import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    ncols = 3 * k
    FULL = (1 << ncols) - 1

    rows_mask = []          # mask of each candidate
    rows_trip = []          # original (a,b,c) for output
    col_rows = [[] for _ in range(ncols)]   # for each column: list of row indices

    for idx in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        mask = (1 << (a - 1)) | (1 << (k + b - 1)) | (1 << (2 * k + c - 1))
        rows_mask.append(mask)
        rows_trip.append((a, b, c))
        for col in (a - 1, k + b - 1, 2 * k + c - 1):
            col_rows[col].append(idx)

    answer = []                     # indices of chosen rows
    used = 0                        # bitmask of already covered columns
    found = False

    # pre‑compute popcount function (Python 3.8+ has int.bit_count())
    popcnt = int.bit_count

    def search(used_mask: int, depth: int) -> bool:
        nonlocal found
        # success?
        if used_mask == FULL:
            return True
        # too many rows already
        if depth == k:
            return False
        # remaining columns must be exactly 3 per missing row
        remaining = popcnt(FULL ^ used_mask)
        if remaining != 3 * (k - depth):
            return False

        # choose column with fewest compatible rows
        best_col = -1
        best_cnt = 10 ** 9
        # iterate over uncovered columns
        mask = (~used_mask) & FULL
        while mask:
            col = (mask & -mask).bit_length() - 1
            mask &= mask - 1
            cnt = 0
            for r in col_rows[col]:
                if rows_mask[r] & used_mask == 0:
                    cnt += 1
            if cnt == 0:
                return False
            if cnt < best_cnt:
                best_cnt = cnt
                best_col = col
                if cnt == 1:
                    break

        # try each compatible row
        for r in col_rows[best_col]:
            rm = rows_mask[r]
            if rm & used_mask:
                continue
            answer.append(r)
            if search(used_mask | rm, depth + 1):
                return True
            answer.pop()
        return False

    possible = search(0, 0)

    out = []
    if possible:
        out.append("YES")
        for idx in answer:
            a, b, c = rows_trip[idx]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()