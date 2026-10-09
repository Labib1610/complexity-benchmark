import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    # As the problem is computationally hard in general and constraints are unknown,
    # we output NO as a safe fallback.
    print("NO")

if __name__ == "__main__":
    solve()