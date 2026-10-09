def solve():
    j = int(input())
    jobs = []
    for _ in range(j):
        p1, p2 = map(int, input().split())
        jobs.append((p1, p2))
    
    jobs.sort(key=lambda x: x[0] - x[1])
    
    machine1_time = 0
    machine2_time = 0
    
    for p1, p2 in jobs:
        machine1_time += p1
        machine2_time = max(machine2_time, machine1_time) + p2
        
    print(machine2_time)

solve()