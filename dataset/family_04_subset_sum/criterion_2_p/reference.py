import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    costs = [int(data[idx + i]) for i in range(n)]; idx += n
    T = int(data[idx]); idx += 1

    if T < 0:
        print("NO")
        return

    # Boolean DP over reachable sums with 0/1 (downward) update; O(n*T).
    # from_item[j] / prev_sum[j] track how sum j was first reached so we can
    # reconstruct one valid group.
    reach = [False] * (T + 1)
    reach[0] = True
    from_item = [-1] * (T + 1)
    prev_sum = [-1] * (T + 1)

    for i in range(n):
        c = costs[i]
        if c > T:
            continue
        for j in range(T, c - 1, -1):
            if not reach[j] and reach[j - c]:
                reach[j] = True
                from_item[j] = i
                prev_sum[j] = j - c

    if not reach[T]:
        print("NO")
        return

    chosen = []
    j = T
    while j > 0:
        chosen.append(from_item[j] + 1)
        j = prev_sum[j]
    chosen.reverse()

    print("YES")
    print(' '.join(map(str, chosen)))


main()
