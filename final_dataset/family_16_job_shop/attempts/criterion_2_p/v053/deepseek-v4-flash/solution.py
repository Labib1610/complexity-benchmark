import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    jobs = []
    idx = 1
    for _ in range(n):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        jobs.append((a, b))
    
    # Johnson's rule
    group1 = []
    group2 = []
    for a, b in jobs:
        if a <= b:
            group1.append((a, b))
        else:
            group2.append((a, b))
    
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: x[1], reverse=True)
    
    order = group1 + group2
    
    # Simulate
    time_solver = 0
    time_tracer = 0
    for a, b in order:
        time_solver += a
        if time_tracer < time_solver:
            time_tracer = time_solver
        time_tracer += b
    
    print(time_tracer)

if __name__ == "__main__":
    solve()