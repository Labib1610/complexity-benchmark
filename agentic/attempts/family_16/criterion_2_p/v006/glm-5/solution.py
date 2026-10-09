import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    containers = []
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        containers.append((p1, p2))
    
    # Sort by Johnson's rule:
    # Group A: p1 <= p2, sort by p1 ascending
    # Group B: p1 > p2, sort by p2 descending
    # Group A first, then Group B
    group_a = [(p1, p2) for p1, p2 in containers if p1 <= p2]
    group_b = [(p1, p2) for p1, p2 in containers if p1 > p2]
    
    group_a.sort(key=lambda x: x[0])
    group_b.sort(key=lambda x: -x[1])
    
    ordered = group_a + group_b
    
    time_inspection = 0
    time_loading = 0
    
    for p1, p2 in ordered:
        time_inspection += p1
        # Loading starts after inspection finishes and after previous loading finishes
        time_loading = max(time_inspection, time_loading) + p2
    
    print(time_loading)

if __name__ == "__main__":
    solve()