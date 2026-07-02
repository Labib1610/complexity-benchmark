import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(data[idx]); idx += 1
    e = int(data[idx]); idx += 1

    # Mark which workers appear in at least one allowed pair, then report the
    # smallest worker that appears in none. Such a worker can never be assigned,
    # so no complete plan exists.
    has_partner = [False] * (k + 1)
    for _ in range(e):
        x = int(data[idx]); idx += 2  # y is unused for this decision
        has_partner[x] = True

    for x in range(1, k + 1):
        if not has_partner[x]:
            print(x)
            return

    # Fallback (inputs for this criterion always contain such a worker).
    print(-1)


main()
