import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    effects = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        idx += 2
        effects.append((p1, p2))
    
    # Johnson's rule for two-machine flow shop (minimize makespan)
    # Group A: p1 <= p2, sorted by p1 ascending
    # Group B: p1 > p2, sorted by p2 descending
    groupA = []
    groupB = []
    for p1, p2 in effects:
        if p1 <= p2:
            groupA.append((p1, p2))
        else:
            groupB.append((p1, p2))
    
    groupA.sort(key=lambda x: x[0])
    groupB.sort(key=lambda x: x[1], reverse=True)
    
    order = groupA + groupB
    
    # Simulate to compute makespan
    time_solver = 0
    time_tracer = 0
    for p1, p2 in order:
        start_solver = time_solver
        end_solver = start_solver + p1
        start_tracer = max(end_solver, time_tracer)
        end_tracer = start_tracer + p2
        time_solver = end_solver
        time_tracer = end_tracer
    
    print(time_tracer)

solve()