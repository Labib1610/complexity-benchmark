import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    jobs = []
    total_gimbal = 0
    total_sensor = 0
    
    for i in range(n):
        p1 = int(data[idx]); idx += 1
        p2 = int(data[idx]); idx += 1
        jobs.append((p1, p2))
        total_gimbal += p1
        total_sensor += p2
    
    # Check per-job feasibility
    for i, (p1, p2) in enumerate(jobs, start=1):
        if p1 > T or p2 > T or p2 > T - p1:
            print(f"JOB {i}")
            return
    
    # Check global constraints
    if total_gimbal > T or total_sensor > T:
        print("LOAD 1")
        return
    
    # If all pass, no contradiction
    # The problem statement implies there is always a contradiction, but if none, we output nothing?
    # However, based on examples, they always output something. We'll output nothing if all pass.
    # But to be safe, we can output nothing or handle as needed.
    # Since the problem guarantees a contradiction, we can just return.
    
if __name__ == "__main__":
    main()