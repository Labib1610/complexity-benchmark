import sys

def solve():
    input = sys.stdin.readline
    j = int(input())
    tiles = []
    total_bottom = 0
    for _ in range(j):
        p1, p2 = map(int, input().split())
        tiles.append((p1 - p2, p1, p2))
        total_bottom += p2
    
    # Sort by difference, then by p1
    tiles.sort(key=lambda x: (x[0], x[1]))
    
    max_val = -10**18
    pref = 0
    for diff, a, b in tiles:
        pref += diff
        val = pref + b
        if val > max_val:
            max_val = val
    
    print(total_bottom + max_val)

if __name__ == "__main__":
    solve()