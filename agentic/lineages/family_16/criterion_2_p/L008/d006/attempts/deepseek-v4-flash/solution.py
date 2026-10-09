import sys

def solve():
    input = sys.stdin.readline
    j = int(input())
    sectors = []
    for _ in range(j):
        p1, p2 = map(int, input().split())
        sectors.append((p1, p2))
    
    gain = []
    loss = []
    for p1, p2 in sectors:
        if p1 < p2:
            gain.append((p1, p2))
        else:
            loss.append((p1, p2))
    
    gain.sort(key=lambda x: x[0])
    loss.sort(key=lambda x: -x[1])
    
    order = gain + loss
    
    charge = 0
    cost = 0
    for p1, p2 in order:
        allocated = min(p1, charge)
        charge -= allocated
        charge += p2
        cost += p1 + p2 - allocated
    
    print(cost)

if __name__ == "__main__":
    solve()