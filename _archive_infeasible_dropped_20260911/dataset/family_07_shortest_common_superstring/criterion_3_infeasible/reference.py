import sys


def main():
    data = sys.stdin.buffer.read().split()
    k = int(data[0])
    frags = [data[1 + i].decode() for i in range(k)]
    F = data[1 + k].decode()

    # Any output must contain each fragment, so a fragment holding F forces F to
    # appear. Report the first such fragment.
    for i in range(k):
        if F in frags[i]:
            print(i + 1)
            return

    # Fallback (inputs for this criterion always contain such a fragment).
    print(-1)


main()
