import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    
    total_node1 = 0
    total_node2 = 0
    job_index = 0
    
    for i in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 + p2 > T:
            job_index = i
            # We must continue reading all input, but we can break early
            # since we found the answer. However, for simplicity and to avoid
            # leaving unread data in the iterator (though not strictly necessary
            # when reading all at once), we can just break.
            # Actually, we need to output the first such job (1-based).
            # The problem guarantees exactly one breach type, so if we find a job,
            # that's the answer.
            # We can break to save time.
            break
        total_node1 += p1
        total_node2 += p2
    
    if job_index > 0:
        print(f"JOB {job_index}")
        return
    
    # If we didn't break early, we need to process the rest of the jobs
    # But since we broke, we need to handle the case where we didn't.
    # Let's restructure to process all jobs if no individual job breach.
    # Actually, the break above is fine, but we need to ensure we read all input
    # if we were reading lazily. Since we read all at once, it's fine.
    # However, if we break early, we haven't summed the rest.
    # But the problem guarantees exactly one breach type.
    # So if we found a job breach, we output it.
    # If we didn't find any job breach, we must have a load breach.
    # So we need to sum all jobs.
    
    # Let's re-process without breaking early for correctness.
    # Reset totals
    total_node1 = 0
    total_node2 = 0
    job_index = 0
    
    # Re-iterate from the start
    it = iter(data)
    next(it)  # j
    next(it)  # T
    
    for i in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 + p2 > T:
            job_index = i
            # Since exactly one breach type, we can break
            break
        total_node1 += p1
        total_node2 += p2
    
    if job_index > 0:
        print(f"JOB {job_index}")
    elif total_node1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

if __name__ == "__main__":
    main()