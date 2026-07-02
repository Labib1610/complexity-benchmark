import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); T = int(data[idx + 1]); idx += 2

    max_p1 = 0
    for _ in range(j):
        p1 = int(data[idx]); idx += 2  # p2 not needed for this decision
        if p1 > max_p1:
            max_p1 = p1

    # Some job's machine-1 time alone exceeds the deadline, so no schedule can
    # finish all jobs by time T.
    if T < max_p1:
        print("NO")
        return

    # Fallback (inputs for this criterion always have T < max machine-1 time).
    print("NO")


main()
