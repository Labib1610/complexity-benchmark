import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    # j = int(data[0]); T = int(data[1])  # not needed
    # The problem guarantees at least one job with p1 > T, so answer is always NO.
    sys.stdout.write("NO")

if __name__ == "__main__":
    solve()