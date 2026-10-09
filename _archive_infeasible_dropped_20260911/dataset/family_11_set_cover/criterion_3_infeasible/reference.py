import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    u = int(data[idx]); s = int(data[idx + 1]); idx += 2

    covered = [False] * (u + 1)
    for _ in range(s):
        cnt = int(data[idx]); idx += 1
        for _ in range(cnt):
            sk = int(data[idx]); idx += 1
            covered[sk] = True

    # A skill brought by no consultant can never be covered.
    for sk in range(1, u + 1):
        if not covered[sk]:
            print(sk)
            return

    # Fallback (inputs for this criterion always have an uncoverable skill).
    print(-1)


main()
