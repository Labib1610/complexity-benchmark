import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    vessels = []
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        vessels.append((p1, p2))
    
    # Sort by Johnson's rule:
    # Type A: p1 <= p2, sorted by p1 ascending
    # Type B: p1 > p2, sorted by p2 descending
    typeA = []
    typeB = []
    for p1, p2 in vessels:
        if p1 <= p2:
            typeA.append((p1, p2))
        else:
            typeB.append((p1, p2))
    
    typeA.sort(key=lambda x: x[0])
    typeB.sort(key=lambda x: -x[1])
    
    order = typeA + typeB
    
    # Simulate the process
    # local_time: time when Local officer finishes current vessel
    # federal_time: time when Federal officer finishes current vessel
    local_time = 0
    federal_time = 0
    
    for p1, p2 in order:
        local_time += p1
        # Federal can start only after Local finishes this vessel
        start_federal = max(local_time, federal_time)
        federal_time = start_federal + p2
    
    print(federal_time)

if __name__ == "__main__":
    solve()