import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    if k == 0:
        print("YES")
        print()
        return

    if m == 0:
        if k <= n:
            print("YES")
            print(" ".join(str(i) for i in range(1, k + 1)))
        else:
            print("NO")
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)
    comp = []

    for i in range(1, n + 1):
        if color[i] == 0:
            stack = [i]
            color[i] = 1
            cnt = [0, 0, 0]
            cnt[1] = 1
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        cnt[color[v]] += 1
                        stack.append(v)
            comp.append((cnt[1], cnt[2]))

    total = 0
    for a, b in comp:
        total += max(a, b)

    if k > total:
        print("NO")
        return

    print("YES")

    if k == 1:
        print(1)
        return

    dp = 1
    for a, b in comp:
        dp |= (dp << a)
        dp |= (dp << b)

    if (dp >> k) & 1:
        target = k
    else:
        target = total - k

    chosen = [0] * (n + 1)
    for a, b in reversed(comp):
        if target >= a and (dp >> (target - a)) & 1:
            chosen_color = 1
            target -= a
        else:
            chosen_color = 2
            target -= b
        for i in range(1, n + 1):
            if color[i] == chosen_color and chosen[i] == 0:
                chosen[i] = 1

    if (dp >> k) & 1:
        result = [str(i) for i in range(1, n + 1) if chosen[i] == 1]
    else:
        result = [str(i) for i in range(1, n + 1) if chosen[i] == 0]

    print(" ".join(result))

solve()