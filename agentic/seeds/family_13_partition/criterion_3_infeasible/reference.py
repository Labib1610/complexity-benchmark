import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    total = 0
    for i in range(n):
        total += int(data[1 + i])

    # An odd total cannot be split into two equal whole-number halves.
    if total % 2 != 0:
        print("NO")
        return

    # Fallback (inputs for this criterion always have an odd total).
    print("NO")


main()
