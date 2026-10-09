import sys
sys.setrecursionlimit(10000)

def solve():
    import sys
    n, m = map(int, sys.stdin.readline().split())
    edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    print("NO")

if __name__ == "__main__":
    solve()