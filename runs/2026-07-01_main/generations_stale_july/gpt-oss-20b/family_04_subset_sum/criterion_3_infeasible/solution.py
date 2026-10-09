import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    # n = int(data[0])  # not needed
    # costs = list(map(int, data[1:1+int(data[0])]))  # not needed
    # T = int(data[1+int(data[0])])  # not needed
    # Since all costs are positive and T is negative, no subset can sum to T.
    sys.stdout.write("NO")

if __name__ == "__main__":
    solve()