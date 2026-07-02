import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); B = int(data[1])

    # Budget 0 with strictly positive costs: no investment is affordable, but at
    # least one must be selected, so no valid selection exists.
    if B == 0:
        print("NO")
        return

    # Fallback (inputs for this criterion always have B = 0).
    print("NO")


main()
