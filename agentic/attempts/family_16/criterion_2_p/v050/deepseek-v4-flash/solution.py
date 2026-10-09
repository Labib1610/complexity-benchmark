import sys

def solve():
    data = sys.stdin.buffer.read().split()
    j = int(data[0])
    tasks = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        tasks.append((p1, p2))
    
    group1 = []
    group2 = []
    for p1, p2 in tasks:
        if p1 <= p2:
            group1.append((p1, p2))
        else:
            group2.append((p1, p2))
    
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: x[1], reverse=True)
    
    order = group1 + group2
    
    surveyor_time = 0
    harvester_time = 0
    for p1, p2 in order:
        surveyor_time += p1
        if harvester_time < surveyor_time:
            harvester_time = surveyor_time
        harvester_time += p2
    
    print(harvester_time)

if __name__ == "__main__":
    solve()