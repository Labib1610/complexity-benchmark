import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # Try to find an independent set of size k
    # Use backtracking with pruning
    chosen = []
    used_mask = 0

    def backtrack(start, count):
        if count == k:
            return True
        if start >= n:
            return False
        # Prune: not enough remaining vertices
        if n - start < k - count:
            return False

        # Try to include vertex start
        if not (used_mask & (1 << start)):
            # Check if start is compatible with chosen
            if not (used_mask & adj[start]):
                chosen.append(start)
                used_mask_old = used_mask
                # We need to update used_mask to include start and its neighbors? 
                # Actually for independent set, we only need to ensure no edges among chosen.
                # So we just add start to used_mask as chosen.
                # But used_mask is used to check compatibility with future vertices.
                # We can keep a separate chosen_mask.
                # Let's restructure.
                pass

        # Simpler: use recursion with a chosen_mask
        def dfs(idx, chosen_mask, count):
            if count == k:
                return chosen_mask
            if idx >= n:
                return None
            if n - idx < k - count:
                return None
            # Option 1: skip idx
            res = dfs(idx + 1, chosen_mask, count)
            if res is not None:
                return res
            # Option 2: take idx if possible
            if not (chosen_mask & adj[idx]):
                res = dfs(idx + 1, chosen_mask | (1 << idx), count + 1)
                if res is not None:
                    return res
            return None

        result_mask = dfs(0, 0, 0)
        if result_mask is None:
            print("NO")
        else:
            ans = [str(i + 1) for i in range(n) if (result_mask >> i) & 1]
            print("YES")
            print(" ".join(ans))
        return

    # Actually we need to call the dfs properly
    def find_independent_set():
        def dfs(idx, chosen_mask, count):
            if count == k:
                return chosen_mask
            if idx >= n:
                return None
            if n - idx < k - count:
                return None
            # skip
            res = dfs(idx + 1, chosen_mask, count)
            if res is not None:
                return res
            # take
            if not (chosen_mask & adj[idx]):
                res = dfs(idx + 1, chosen_mask | (1 << idx), count + 1)
                if res is not None:
                    return res
            return None
        return dfs(0, 0, 0)

    result_mask = find_independent_set()
    if result_mask is None:
        print("NO")
    else:
        ans = [str(i + 1) for i in range(n) if (result_mask >> i) & 1]
        print("YES")
        print(" ".join(ans))

if __name__ == "__main__":
    solve()