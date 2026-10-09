import sys

def solve():
    input = sys.stdin.readline
    j = int(input())
    comps = []
    for _ in range(j):
        p1, p2 = map(int, input().split())
        comps.append((p1, p2))
    
    # Sort using the Johnson's rule variant
    comps.sort(key=lambda x: (x[0] < x[1], x[0] if x[0] < x[1] else -x[1]))
    
    X = 0
    Y = 0
    for p1, p2 in comps:
        X += p1
        Y = max(X, Y) + p2
    print(Y)

if __name__ == "__main__":
    solve()