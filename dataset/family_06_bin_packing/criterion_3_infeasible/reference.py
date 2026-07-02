import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1

    # An item heavier than a single container fits nowhere; report the first one.
    for i in range(n):
        if int(data[idx + i]) > C:
            print(i + 1)
            return

    # Fallback (inputs for this criterion always contain an oversized item).
    print(-1)


main()
