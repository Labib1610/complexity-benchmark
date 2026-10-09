import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    if m == 0:
        if k <= n:
            sys.stdout.write("YES\n")
            sys.stdout.write(" ".join(str(i) for i in range(1, k + 1)) + "\n")
        else:
            sys.stdout.write("NO\n")
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)
    comp = []
    comp_size = 0
    comp_a = 0
    comp_b = 0
    stack = []

    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            stack.append(i)
            a = 0
            b = 0
            while stack:
                u = stack.pop()
                if color[u] == 1:
                    a += 1
                else:
                    b += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
            comp.append((a, b))
            comp_size += 1
            comp_a += a
            comp_b += b

    total = comp_a + comp_b
    target = k
    if target < 0 or target > total:
        sys.stdout.write("NO\n")
        return

    dp = [0] * (target + 1)
    dp[0] = 1
    for a, b in comp:
        if a > b:
            a, b = b, a
        for j in range(target, a - 1, -1):
            if dp[j - a] == 1 and dp[j] == 0:
                dp[j] = 1

    if dp[target] == 0:
        sys.stdout.write("NO\n")
        return

    chosen = [0] * comp_size
    cur = target
    for i in range(comp_size - 1, -1, -1):
        a, b = comp[i]
        if a > b:
            a, b = b, a
        if cur >= a and dp[cur - a] == 1:
            chosen[i] = a
            cur -= a
        else:
            chosen[i] = b
            cur -= b

    color = [0] * (n + 1)
    comp_idx = 0
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            stack.append(i)
            a = 0
            b = 0
            while stack:
                u = stack.pop()
                if color[u] == 1:
                    a += 1
                else:
                    b += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
            need = chosen[comp_idx]
            if a == need:
                pick_color = 1
            else:
                pick_color = 2
            stack.append(i)
            color[i] = -pick_color
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] > 0:
                        color[v] = -pick_color if color[v] == pick_color else -3 + pick_color
                        stack.append(v)
            comp_idx += 1

    ans = [str(i) for i in range(1, n + 1) if color[i] == -1]
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(ans) + "\n")

solve()