import sys

sys.setrecursionlimit(10000)

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
    answer = []

    # depth‑first search with pruning
    def dfs(chosen_mask: int, candidates_mask: int, chosen_list: list) -> bool:
        nonlocal answer
        if len(chosen_list) == k:
            answer = chosen_list[:]
            return True
        # not enough vertices left
        if len(chosen_list) + candidates_mask.bit_count() < k:
            return False
        # pick a vertex (least significant bit)
        v = (candidates_mask & -candidates_mask).bit_length() - 1

        # branch 1: take v
        new_chosen = chosen_mask | (1 << v)
        new_cand = candidates_mask & ~adj[v] & ~(1 << v)
        if dfs(new_chosen, new_cand, chosen_list + [v]):
            return True

        # branch 2: skip v
        candidates_mask &= ~(1 << v)
        if dfs(chosen_mask, candidates_mask, chosen_list):
            return True

        return False

    if dfs(0, ALL, []):
        print("YES")
        # convert to 1‑based indices
        print(' '.join(str(x + 1) for x in answer))
    else:
        print("NO")

if __name__ == "__main__":
    solve()