import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    g = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        g[u].append(v)
        g[v].append(u)

    colour = [-1] * n
    comps = []          # list of (list_left, list_right)
    from collections import deque
    for start in range(n):
        if colour[start] != -1:
            continue
        q = deque([start])
        colour[start] = 0
        left, right = [], []
        while q:
            v = q.popleft()
            if colour[v] == 0:
                left.append(v)
            else:
                right.append(v)
            for to in g[v]:
                if colour[to] == -1:
                    colour[to] = colour[v] ^ 1
                    q.append(to)
        comps.append((left, right))

    # DP arrays
    reachable = 1  # bit 0 set
    prev_sum = [-1] * (k + 1)   # previous sum
    taken_side = [0] * (k + 1)  # 0 -> left, 1 -> right
    comp_of = [-1] * (k + 1)    # which component created this sum
    prev_sum[0] = -2            # start marker
    cur_sums = [0]

    for idx, (L, R) in enumerate(comps):
        a = len(L)
        b = len(R)
        new_sums = []
        for s in cur_sums:
            ns = s + a
            if ns <= k and prev_sum[ns] == -1:
                prev_sum[ns] = s
                taken_side[ns] = 0
                comp_of[ns] = idx
                new_sums.append(ns)
            ns = s + b
            if ns <= k and prev_sum[ns] == -1:
                prev_sum[ns] = s
                taken_side[ns] = 1
                comp_of[ns] = idx
                new_sums.append(ns)
        cur_sums.extend(new_sums)

    if prev_sum[k] == -1:
        print("NO")
        return

    # reconstruct choices
    choose = [None] * len(comps)   # 0 -> left, 1 -> right
    cur = k
    while cur != 0:
        idx = comp_of[cur]
        side = taken_side[cur]
        choose[idx] = side
        cur = prev_sum[cur]

    # components that were never needed (sum 0) can take any side,
    # we simply take the left side (size may be 0)
    for i in range(len(comps)):
        if choose[i] is None:
            choose[i] = 0

    answer = []
    for (L, R), side in zip(comps, choose):
        answer.extend(L if side == 0 else R)

    # answer size must be k
    answer = answer[:k]

    print("YES")
    print(' '.join(str(v + 1) for v in answer))

if __name__ == "__main__":
    solve()