import sys

def solve():
    input = sys.stdin.readline
    j = int(input())
    vessels = []
    for _ in range(j):
        p1, p2 = map(int, input().split())
        vessels.append((p1, p2))
    
    # Sort: vessels with p1 <= p2 first (ascending p1), then p1 > p2 (descending p2)
    first = []
    second = []
    for p1, p2 in vessels:
        if p1 <= p2:
            first.append((p1, p2))
        else:
            second.append((p1, p2))
    
    first.sort(key=lambda x: x[0])  # ascending p1
    second.sort(key=lambda x: -x[1])  # descending p2
    
    order = first + second
    
    local_time = 0
    federal_time = 0
    for p1, p2 in order:
        local_time += p1
        if federal_time < local_time:
            federal_time = local_time
        federal_time += p2
    
    print(federal_time)

if __name__ == "__main__":
    solve()