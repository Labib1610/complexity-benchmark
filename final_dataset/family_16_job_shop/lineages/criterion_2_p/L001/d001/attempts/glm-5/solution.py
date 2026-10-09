import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    # p1 = initial review, p2 = final sign-off
    # We want to sort by p2 descending (Johnson's rule for two-machine flow shop)
    # Actually for two-machine flow shop to minimize makespan:
    # jobs with p1 <= p2 sorted by p1 ascending, then jobs with p1 > p2 sorted by p2 descending
    # But the problem says "stack" - dispatcher arranges into a single stack
    # Initial reviewer takes from top of stack one by one
    # So the order of processing is the reverse of the stack order
    # Let's think: if stack is [bottom, ..., top], reviewer takes top first
    # So processing order is reverse of stack arrangement
    # We want to find the processing order that minimizes makespan
    # For two-machine flow shop, optimal order is given by Johnson's rule
    
    jobs = []
    idx = 1
    for i in range(j):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        idx += 2
        jobs.append((p1, p2))
    
    # Johnson's rule: 
    # Partition into two sets: p1 < p2 and p1 >= p2 (or p1 <= p2 and p1 > p2)
    # Set 1 (p1 <= p2): sort by p1 ascending
    # Set 2 (p1 > p2): sort by p2 descending
    # Concatenate: Set1 + Set2
    
    set1 = []  # p1 <= p2
    set2 = []  # p1 > p2
    for p1, p2 in jobs:
        if p1 <= p2:
            set1.append((p1, p2))
        else:
            set2.append((p1, p2))
    
    set1.sort(key=lambda x: x[0])  # by p1 ascending
    set2.sort(key=lambda x: x[1], reverse=True)  # by p2 descending
    
    order = set1 + set2
    
    # Simulate
    t1 = 0  # time on machine 1
    t2 = 0  # time on machine 2
    for p1, p2 in order:
        t1 += p1
        # machine 2 can start at max(t2, t1)
        t2 = max(t2, t1) + p2
    
    print(t2)

solve()