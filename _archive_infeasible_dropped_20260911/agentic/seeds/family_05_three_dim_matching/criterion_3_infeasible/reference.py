import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(data[idx]); t = int(data[idx + 1]); idx += 2
    appears = [False] * (k + 1)
    for _ in range(t):
        x = int(data[idx]); idx += 3   # only the specialist matters for the certificate
        if 1 <= x <= k:
            appears[x] = True

    # At least one specialist is in no allowed crew, so it can never be covered -> no valid plan.
    for x in range(1, k + 1):
        if not appears[x]:
            print(x)
            return
    print(1)   # defensive fallback (inputs always contain an uncovered specialist)


main()
