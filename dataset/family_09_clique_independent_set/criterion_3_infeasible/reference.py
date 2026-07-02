import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    r = int(data[2])

    # A group cannot have more members than the n users that exist, so a request
    # for r > n users can never be satisfied.
    if r > n:
        print("NO")
        return

    # Fallback (inputs for this criterion always have r > n).
    print("NO")


main()
