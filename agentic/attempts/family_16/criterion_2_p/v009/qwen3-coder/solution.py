import sys
import threading

def main():
    import sys
    j = int(sys.stdin.readline())
    jobs = []
    for _ in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        jobs.append((p1, p2))
    
    # Sort jobs using Johnson's rule for two-machine flow shop
    # Jobs with p1 <= p2 should be scheduled early (sorted by p1 ascending)
    # Jobs with p1 > p2 should be scheduled late (sorted by p2 descending)
    front = []  # jobs where p1 <= p2
    back = []   # jobs where p1 > p2
    
    for i, (p1, p2) in enumerate(jobs):
        if p1 <= p2:
            front.append((p1, p2))
        else:
            back.append((p1, p2))
    
    # Sort front by p1 ascending, back by p2 descending
    front.sort(key=lambda x: x[0])
    back.sort(key=lambda x: x[1], reverse=True)
    
    # Combine schedules
    schedule = front + back
    
    # Calculate the minimum completion time
    time_m1 = 0  # current time on machine 1
    time_m2 = 0  # current time on machine 2
    
    for p1, p2 in schedule:
        time_m1 += p1
        # Machine 2 can start this job only after:
        # 1. This job finishes on machine 1 (time_m1)
        # 2. Machine 2 finishes the previous job (time_m2)
        time_m2 = max(time_m1, time_m2) + p2
    
    print(time_m2)

# Threading is needed because of deep recursion in some sorting implementations
threading.Thread(target=main).start()