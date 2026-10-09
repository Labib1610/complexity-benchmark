import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    # (edges are not needed to emit the certificate)

    # Certificate 1: asking for more vertices than exist.
    if k > n:
        print("SIZE")
        return

    # Certificate 2: the graph is complete (every pair adjacent), so the max independent set is 1;
    # with k >= 2 no independent set of size k exists.
    if m == n * (n - 1) // 2 and k >= 2:
        print("COMPLETE")
        return

    # Inputs for this criterion always satisfy one of the two certificates; defensive fallback.
    print("SIZE")


main()
