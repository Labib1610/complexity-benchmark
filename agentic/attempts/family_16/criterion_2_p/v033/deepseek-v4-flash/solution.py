import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    tasks = []
    idx = 1
    for _ in range(n):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
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
    group2.sort(key=lambda x: -x[1])
    
    order = group1 + group2
    
    solver_time = 0
    tracer_time = 0
    for p1, p2 in order:
        solver_time += p1
        if tracer_time < solver_time:
            tracer_time = solver_time
        tracer_time += p2
    
    print(tracer_time)

if __name__ == "__main__":
    main()