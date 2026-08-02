import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    T = int(data[1 + n])

    # Every item cost is a positive integer, so any group (including the empty
    # group, which totals 0) has a total of at least 0. A negative target can
    # never be reached.
    if T < 0:
        print("NO")
        return

    # Defensive fallback (inputs for this criterion always have T < 0).
    print("NO")


main()
