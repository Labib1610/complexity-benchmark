import sys

def solve():
    input = sys.stdin.readline
    j = int(input())
    checkpoints = []
    for _ in range(j):
        p1, p2 = map(int, input().split())
        checkpoints.append((p1, p2))
    
    # Sort by p2 descending, then p1 descending
    checkpoints.sort(key=lambda x: (-x[1], -x[0]))
    
    scout_time = 0
    hauler_time = 0
    
    for p1, p2 in checkpoints:
        scout_time += p1
        if hauler_time < scout_time:
            hauler_time = scout_time
        hauler_time += p2
    
    print(hauler_time)

if __name__ == "__main__":
    solve()