import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    tasks = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        idx += 2
        tasks.append((p1, p2))
    
    # Sort by Johnson's rule:
    # tasks with p1 <= p2 sorted by p1 ascending, then tasks with p1 > p2 sorted by p2 descending
    group1 = [(p1, p2) for (p1, p2) in tasks if p1 <= p2]
    group2 = [(p1, p2) for (p1, p2) in tasks if p1 > p2]
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: x[1], reverse=True)
    order = group1 + group2
    
    surveyor_time = 0
    harvester_time = 0
    for p1, p2 in order:
        surveyor_time += p1
        # Harvester can start at max(surveyor_time, harvester_time)
        start = surveyor_time if surveyor_time > harvester_time else harvester_time
        harvester_time = start + p2
    
    print(harvester_time)

solve()