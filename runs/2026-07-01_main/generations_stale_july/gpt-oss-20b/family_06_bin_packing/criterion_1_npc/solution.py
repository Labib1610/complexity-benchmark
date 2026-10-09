import sys
import threading

def solve():
    import sys

    sys.setrecursionlimit(1000000)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    C = int(next(it))
    weights = [int(next(it)) for _ in range(n)]

    total = sum(weights)
    if total > k * C:
        print("NO")
        return

    # sort items by weight descending, keep original indices
    items = sorted([(weights[i], i) for i in range(n)], key=lambda x: -x[0])
    # if k > n, we can treat k = n for assignment, but we keep k for output
    bin_loads = [0] * k
    assignment = [0] * n
    found = False

    def dfs(idx):
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        w, orig = items[idx]
        prev_load = -1
        for j in range(k):
            if bin_loads[j] + w <= C:
                if bin_loads[j] == prev_load:
                    continue
                prev_load = bin_loads[j]
                bin_loads[j] += w
                assignment[orig] = j + 1
                dfs(idx + 1)
                if found:
                    return
                bin_loads[j] -= w
                assignment[orig] = 0
            if bin_loads[j] == 0:
                # if we placed in an empty bin and failed, no need to try other empty bins
                break

    dfs(0)
    if not found:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(assignment[i]) for i in range(n)))

def main():
    solve()

threading.Thread(target=main).start()