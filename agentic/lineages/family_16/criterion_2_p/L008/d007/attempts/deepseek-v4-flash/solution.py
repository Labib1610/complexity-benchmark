import sys

def solve():
    input = sys.stdin.readline
    j = int(input())
    sectors = []
    total_p1 = 0
    for _ in range(j):
        p1, p2 = map(int, input().split())
        sectors.append((p1, p2))
        total_p1 += p1
    
    # Sort by (p1+p2, p1) ascending
    sectors.sort(key=lambda x: (x[0] + x[1], x[0]))
    
    D = 0
    for p1, p2 in sectors:
        if D < 2 * p1:
            D = 2 * p2
        else:
            D = D + 2 * (p2 - p1)
    
    ans = total_p1 + D // 2
    print(ans)

if __name__ == "__main__":
    solve()