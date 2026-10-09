import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # degree list, choose a vertex with maximal degree as start
    start = max(range(n), key=lambda x: adj[x].bit_count())

    col = [-1] * n               # -1 = uncoloured, else 0,1,2
    col_mask = [0, 0, 0]         # bitmask for each colour

    # fix colour of start vertex to 0 (break symmetry)
    col[start] = 0
    col_mask[0] = 1 << start

    # ---------- recursive search ----------
    def dfs(coloured_cnt: int, used: int) -> bool:
        if coloured_cnt == n:
            return True

        # choose vertex with minimum remaining colours
        v = -1
        best_options = 4
        options_mask = 0
        for i in range(n):
            if col[i] != -1:
                continue
            mask = 0
            # existing colours
            for c in range(used):
                if (adj[i] & col_mask[c]) == 0:
                    mask |= 1 << c
            # possible new colour
            if used < 3:
                mask |= 1 << used
            cnt = mask.bit_count()
            if cnt == 0:               # dead end
                return False
            if cnt < best_options:
                best_options = cnt
                v = i
                options_mask = mask
                if cnt == 1:
                    break

        # try existing colours first
        for c in range(used):
            if (options_mask >> c) & 1:
                col[v] = c
                col_mask[c] |= 1 << v
                if dfs(coloured_cnt + 1, used):
                    return True
                col_mask[c] ^= 1 << v
                col[v] = -1

        # try a new colour
        if used < 3 and ((options_mask >> used) & 1):
            c = used
            col[v] = c
            col_mask[c] |= 1 << v
            if dfs(coloured_cnt + 1, used + 1):
                return True
            col_mask[c] ^= 1 << v
            col[v] = -1

        return False

    possible = dfs(1, 1)

    if not possible:
        print("NO")
    else:
        print("YES")
        # convert 0,1,2 to 1,2,3
        ans = [str(col[i] + 1) for i in range(n)]
        print(" ".join(ans))

if __name__ == "__main__":
    solve()