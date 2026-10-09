import sys
from bisect import bisect_right

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    containers = []
    index = 1
    for i in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        containers.append((p1, p2))
        index += 2
    
    # Sort containers by p1 + p2 in descending order (Johnson's rule)
    containers.sort(key=lambda x: x[0] + x[1], reverse=True)
    
    # For containers with same p1+p2, sort by p1 ascending to minimize initial wait
    # However, Johnson's rule for two machines says:
    # For jobs with processing times (a_i, b_i), 
    # if a_i < b_i, schedule them as early as possible
    # if a_i > b_i, schedule them as late as possible
    # if a_i == b_i, order doesn't matter
    
    # But we want to minimize makespan. The optimal strategy is not just sorting.
    # This is actually the F2||C_max problem (flow shop scheduling with 2 machines to minimize makespan)
    # The optimal algorithm is Johnson's rule:
    # - Divide jobs into two sets:
    #   Set1: jobs where p1 <= p2
    #   Set2: jobs where p1 > p2
    # - Sort Set1 by p1 ascending
    # - Sort Set2 by p2 descending
    # - Schedule Set1 first, then Set2
    
    set1 = []  # jobs where p1 <= p2
    set2 = []  # jobs where p1 > p2
    
    for p1, p2 in containers:
        if p1 <= p2:
            set1.append((p1, p2))
        else:
            set2.append((p1, p2))
    
    # Sort set1 by p1 ascending
    set1.sort(key=lambda x: x[0])
    # Sort set2 by p2 descending
    set2.sort(key=lambda x: x[1], reverse=True)
    
    # Final sequence: set1 + set2
    sequence = set1 + set2
    
    # Now simulate the process
    time_scan = 0
    time_load = 0
    
    for p1, p2 in sequence:
        time_scan += p1
        time_load = max(time_load, time_scan) + p2
    
    print(time_load)

if __name__ == "__main__":
    main()