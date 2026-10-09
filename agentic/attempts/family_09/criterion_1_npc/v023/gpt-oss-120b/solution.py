import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    ALL = (1 << n) - 1
    sys.setrecursionlimit(10000)
    answer = []

    # simple recursive search for independent set of size k
    def dfs(cur_mask: int, cand_mask: int):
        nonlocal answer
        if answer:  # already found
            return True
        cur_size = cur_mask.bit_count()
        if cur_size == k:
            # extract vertices
            ans = []
            for i in range(n):
                if cur_mask >> i & 1:
                    ans.append(i + 1)
            answer = ans
            return True
        # prune if even taking all candidates not enough
        if cur_size + cand_mask.bit_count() < k:
            return False
        # choose a vertex (heuristic: highest degree maybe)
        # pick first set bit
        v = (cand_mask & -cand_mask).bit_length() - 1
        # branch 1: include v
        new_cur = cur_mask | (1 << v)
        new_cand = cand_mask & ~adj[v] & ~(1 << v)
        if dfs(new_cur, new_cand):
            return True
        # branch 2: exclude v
        cand_mask &= ~(1 << v)
        if dfs(cur_mask, cand_mask):
            return True
        return False

    dfs(0, ALL)

    if answer:
        print("YES")
        print(" ".join(map(str, answer)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()