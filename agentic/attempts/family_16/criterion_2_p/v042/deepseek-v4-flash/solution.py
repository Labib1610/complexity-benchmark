import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx]); idx += 1
    
    jobs = []
    for _ in range(n):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        jobs.append((a, b))
    
    # Sort jobs by wash time ascending (Johnson's rule for two-machine flow shop)
    # For minimizing makespan in a two-machine flow shop:
    # - If min(a, b) is from a, put job early
    # - If min(a, b) is from b, put job late
    left = []
    right = []
    for a, b in jobs:
        if a <= b:
            left.append((a, b))
        else:
            right.append((a, b))
    
    left.sort(key=lambda x: x[0])
    right.sort(key=lambda x: x[1], reverse=True)
    
    order = left + right
    
    # Simulate the two-stage process
    time_wash = 0
    time_bake = 0
    for a, b in order:
        time_wash += a
        if time_bake < time_wash:
            time_bake = time_wash
        time_bake += b
    
    print(time_bake)

if __name__ == "__main__":
    main()