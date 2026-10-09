import sys

def solve():
    input = sys.stdin.readline
    j = int(input())
    apps = []
    total_p1 = 0
    gain = []
    loss = []
    
    for _ in range(j):
        p1, p2 = map(int, input().split())
        total_p1 += p1
        if p1 < p2:
            gain.append((p1, p2))
        else:
            loss.append((p1, p2))
    
    # Sort gain by p1 ascending
    gain.sort(key=lambda x: x[0])
    # Sort loss by p2 descending
    loss.sort(key=lambda x: -x[1])
    
    battery = 0
    for p1, p2 in gain + loss:
        if battery < p1:
            battery = 0
        else:
            battery -= p1
        battery += p2
    
    print(total_p1 + battery)

if __name__ == "__main__":
    solve()