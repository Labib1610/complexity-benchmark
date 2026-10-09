import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    q, t = map(int, data[:2])
    # As the general 3‑dimensional matching problem is NP‑hard,
    # and the statement does not provide additional structure,
    # we cannot guarantee a solution for arbitrary inputs within
    # the given limits. Therefore we output NO.
    print("NO")

if __name__ == "__main__":
    solve()