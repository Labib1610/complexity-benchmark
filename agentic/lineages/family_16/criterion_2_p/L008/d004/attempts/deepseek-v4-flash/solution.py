import sys

def solve():
    input = sys.stdin.readline
    j = int(input())
    pos = []  # p1 <= p2
    neg = []  # p1 > p2
    
    total_p2 = 0
    for _ in range(j):
        p1, p2 = map(int, input().split())
        total_p2 += p2
        if p1 <= p2:
            pos.append((p1, p2))
        else:
            neg.append((p1, p2))
    
    # Sort: pos by p1 ascending, neg by p2 descending
    pos.sort(key=lambda x: x[0])
    neg.sort(key=lambda x: -x[1])
    
    order = pos + neg
    
    buffer = 0
    idle_delay = 0
    for p1, p2 in order:
        buffer -= p1
        if buffer < 0:
            idle_delay += -buffer
            buffer = 0
        buffer += p2
    
    print(idle_delay + total_p2)

if __name__ == "__main__":
    solve()