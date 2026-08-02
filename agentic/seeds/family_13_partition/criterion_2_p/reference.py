import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    d = [int(data[1 + i]) for i in range(n)]

    total = sum(d)
    if total % 2 != 0:
        sys.stdout.write("NO\n")
        return
    target = total // 2

    # Boolean subset-sum DP to target with predecessor tracking for one group.
    reach = [False] * (target + 1)
    reach[0] = True
    from_item = [-1] * (target + 1)
    prev_sum = [-1] * (target + 1)

    for i in range(n):
        c = d[i]
        if c > target:
            continue
        for j in range(target, c - 1, -1):
            if not reach[j] and reach[j - c]:
                reach[j] = True
                from_item[j] = i
                prev_sum[j] = j - c

    if not reach[target]:
        sys.stdout.write("NO\n")
        return

    chosen = []
    j = target
    while j > 0:
        chosen.append(from_item[j] + 1)
        j = prev_sum[j]
    chosen.sort()

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, chosen)) + "\n")


main()
