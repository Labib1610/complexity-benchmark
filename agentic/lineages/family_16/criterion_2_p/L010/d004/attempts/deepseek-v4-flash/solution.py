import sys

def solve():
    input = sys.stdin.readline
    j = int(input())
    brackets = []
    for _ in range(j):
        d1, d2 = map(int, input().split())
        brackets.append((d1, d2))
    
    # Sort by d2 descending, then d1 descending
    brackets.sort(key=lambda x: (-x[1], -x[0]))
    
    total_d1 = sum(d1 for d1, _ in brackets)
    max_val = 0
    suffix_sum = total_d1
    for d1, d2 in brackets:
        suffix_sum -= d1
        max_val = max(max_val, d2 + suffix_sum)
    
    print(total_d1 + max_val)

if __name__ == "__main__":
    solve()