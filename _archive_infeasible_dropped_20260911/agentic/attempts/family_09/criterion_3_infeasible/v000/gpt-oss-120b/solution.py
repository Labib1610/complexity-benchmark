import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    if k > n:
        sys.stdout.write("SIZE")
        return

    # If the graph is complete, number of edges equals n*(n-1)//2
    if m == n * (n - 1) // 2:
        sys.stdout.write("COMPLETE")
        return

    # According to the problem statement, one of the above cases always holds.
    # No further processing is needed.

if __name__ == "__main__":
    solve()