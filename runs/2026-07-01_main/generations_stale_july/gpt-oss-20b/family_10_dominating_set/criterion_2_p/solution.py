import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    children = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        c = int(next(it)); p = int(next(it))
        children[p].append(c)

    INF = 10**9
    dp0 = [0] * (n + 1)
    dp1 = [0] * (n + 1)
    dp2 = [0] * (n + 1)

    stack = [(1, 0)]
    while stack:
        node, state = stack.pop()
        if state == 0:
            stack.append((node, 1))
            for child in children[node]:
                stack.append((child, 0))
        else:
            if not children[node]:
                dp0[node] = 1
                dp1[node] = INF
                dp2[node] = 0
            else:
                sum_min = 0
                min_extra = INF
                sum_dp1 = 0
                for child in children[node]:
                    m01 = dp0[child] if dp0[child] < dp1[child] else dp1[child]
                    sum_min += m01
                    extra = dp0[child] - m01
                    if extra < min_extra:
                        min_extra = extra
                    sum_dp1 += dp1[child]
                    if sum_dp1 >= INF:
                        sum_dp1 = INF
                dp0[node] = 1 + sum_min
                dp1[node] = sum_min + min_extra if min_extra < INF else INF
                dp2[node] = sum_dp1

    ans = dp0[1] if dp0[1] < dp1[1] else dp1[1]
    print(ans)

if __name__ == "__main__":
    solve()