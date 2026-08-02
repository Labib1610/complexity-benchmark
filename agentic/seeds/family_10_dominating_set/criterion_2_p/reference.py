import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1

    children = [[] for _ in range(n + 1)]
    parent = [0] * (n + 1)
    for _ in range(n - 1):
        c = int(data[idx]); p = int(data[idx + 1]); idx += 2
        parent[c] = p
        children[p].append(c)

    # Iterative post-order from root 1 (process children before parents).
    order = []
    stack = [1]
    seen = [False] * (n + 1)
    seen[1] = True
    while stack:
        v = stack.pop()
        order.append(v)
        for c in children[v]:
            if not seen[c]:
                seen[c] = True
                stack.append(c)
    order.reverse()

    INF = float("inf")
    # dp[v] = (has_sensor, covered_by_child, uncovered_needs_parent)
    dp0 = [0] * (n + 1)   # v has a sensor
    dp1 = [0] * (n + 1)   # v has no sensor, covered by some child that has one
    dp2 = [0] * (n + 1)   # v has no sensor and not yet covered (needs its parent)

    for v in order:
        ch = children[v]
        if not ch:
            dp0[v] = 1
            dp1[v] = INF   # no child can cover it
            dp2[v] = 0
            continue
        # v has a sensor: children may be in any state (v covers them).
        s0 = 1 + sum(min(dp0[c], dp1[c], dp2[c]) for c in ch)
        # v not covered by children: children must be self-covered (state 0 or 1).
        base = sum(min(dp0[c], dp1[c]) for c in ch)
        dp2[v] = base
        # v covered by a child: at least one child must be in state 0.
        best_delta = INF
        has0 = False
        for c in ch:
            if dp0[c] <= dp1[c]:
                has0 = True
            else:
                best_delta = min(best_delta, dp0[c] - dp1[c])
        dp0[v] = s0
        dp1[v] = base if has0 else (base + best_delta)

    print(min(dp0[1], dp1[1]))


main()
