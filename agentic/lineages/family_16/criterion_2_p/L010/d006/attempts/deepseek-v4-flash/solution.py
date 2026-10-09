import sys

def solve():
    input = sys.stdin.readline
    j = int(input())
    brackets = [tuple(map(int, input().split())) for _ in range(j)]
    
    # Sort: decreasing d2, then decreasing d1
    brackets.sort(key=lambda x: (-x[1], -x[0]))
    
    # Sort by decreasing d2 only actually works. But tie break by decreasing d1 is fine.
    
    prefix_d1 = 0
    total_d2 = sum(d2 for _, d2 in brackets)
    ans = 0
    for d1, d2 in brackets:
        prefix_d1 += d1
        ans = max(ans, prefix_d1 + total_d2)
        total_d2 -= d2
    
    print(ans)

if __name__ == "__main__":
    solve()