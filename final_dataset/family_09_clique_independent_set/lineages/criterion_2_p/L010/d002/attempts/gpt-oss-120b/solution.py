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
    comps = []          # list of (list0, list1)
    from collections import deque
    for start in range(n):
        if colour[start] != -1:
            continue
        q = deque([start])
        colour[start] = 0
        list0 = [start]
        list1 = []
        while q:
            v = q.popleft()
            for to in g[v]:
                if colour[to] == -1:
                    colour[to] = colour[v] ^ 1
                    if colour[to] == 0:
                        list0.append(to)
                    else:
                        list1.append(to)
                    q.append(to)
        comps.append((list0, list1))

    # DP bitset
    dp = 1  # bit 0 set
    max_sum = n
    prev = [-1] * (max_sum + 1)
    choice = [0] * (max_sum + 1)

    for idx, (lst0, lst1) in enumerate(comps):
        a = len(lst0)
        b = len(lst1)
        new = (dp << a) | (dp << b)
        added = new ^ dp
        while added:
            lsb = added & -added
            s = lsb.bit_length() - 1
            # which side gave this sum?
            if s >= a and ((dp >> (s - a)) & 1):
                prev[s] = s - a
                choice[s] = 0
            else:
                prev[s] = s - b
                choice[s] = 1
            added ^= lsb
        dp = new

    if (dp >> k) & 1 == 0:
        print("NO")
        return

    # reconstruction
    take_side = []          # for each component, which side to take (0/1)
    cur = k
    while cur > 0:
        ch = choice[cur]
        take_side.append(ch)
        cur = prev[cur]
    # the order of components processed is the same as comps list,
    # but we collected choices only for those components that contributed
    # (all of them, because each component adds either a or b >0, except
    # isolated vertices where one side may be empty; still a+b =1)
    # however some components may have size0==size1==0? impossible.
    # The length of take_side equals number of components.
    take_side = take_side[::-1]   # now in component order

    answer = []
    for (lst0, lst1), side in zip(comps, take_side):
        if side == 0:
            answer.extend(lst0)
        else:
            answer.extend(lst1)

    # answer length is exactly k
    print("YES")
    print(' '.join(str(v + 1) for v in answer[:k]))

if __name__ == "__main__":
    solve()