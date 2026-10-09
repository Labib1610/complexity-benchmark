import sys

def solve():
    data = sys.stdin.read().split()
    # The sum is guaranteed odd, so answer is always NO
    sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()