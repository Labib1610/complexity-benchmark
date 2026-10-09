import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    # read commodities
    for _ in range(k):
        next(it); next(it); next(it)
    # read edges
    for _ in range(m):
        next(it); next(it); next(it)
    print("NO")

if __name__ == "__main__":
    solve()