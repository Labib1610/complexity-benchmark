import sys
from functools import cmp_to_key

def compare_sectors(a, b):
    # a = (p1_a, p2_a), b = (p1_b, p2_b)
    # Compare a then b vs b then a
    p1_a, p2_a = a
    p1_b, p2_b = b
    
    # Time if we do a then b:
    # Scan_a (p1_a) + max(Scan_b starts, Extraction_a ends) + p2_b
    # Scan_b starts at p1_a, Extraction_a ends at p1_a + p2_a
    # So max(p1_a, p1_a + p2_a) = p1_a + p2_a
    # Total: p1_a + (p1_a + p2_a) + p2_b = 2*p1_a + p2_a + p2_b
    
    # Actually, let's think more carefully:
    # Schedule for a then b:
    # t=0: scan_a starts
    # t=p1_a: scan_a ends, extraction_a starts
    # t=p1_a+p2_a: extraction_a ends, scan_b starts
    # t=p1_a+p2_a+p1_b: scan_b ends, extraction_b starts (if extraction_a is done, which it is)
    # t=p1_a+p2_a+p1_b+p2_b: extraction_b ends
    # Total time: p1_a + p2_a + p1_b + p2_b
    
    # Wait, that's not right either. The extraction of b can start as soon as both:
    # 1. scan of b finishes (at time p1_a + p2_a + p1_b)
    # 2. extraction of a finishes (at time p1_a + p2_a)
    # So extraction_b starts at time p1_a + p2_a + p1_b
    # And ends at p1_a + p2_a + p1_b + p2_b
    
    # Let's reorganize:
    # For sequence [a, b]:
    # T1 = p1_a (scan a)
    # T2 = T1 + p2_a (extraction a)
    # T3 = T2 + p1_b (scan b)
    # T4 = max(T2, T3) + p2_b (extraction b)
    # T4 = max(p1_a + p2_a, p1_a + p2_a + p1_b) + p2_b
    # Since p1_b >= 1, max term is p1_a + p2_a + p1_b
    # So T4 = p1_a + p2_a + p1_b + p2_b
    
    # Hmm wait -- what if p1_b = 0? But constraints say p1_b >= 1.
    # Actually, let me re-read... p1, p2 >= 1. So p1_b >= 1.
    
    # But wait, I think I'm overcomplicating this.
    # Let's simulate properly for comparison.
    
    # Sequence a then b:
    time_scan_a = p1_a
    time_extract_a = time_scan_a + p2_a
    time_scan_b = time_extract_a + p1_b
    time_extract_b = max(time_extract_a, time_scan_b) + p2_b
    
    # Sequence b then a:
    time_scan_b_first = p1_b
    time_extract_b_first = time_scan_b_first + p2_b
    time_scan_a_first = time_extract_b_first + p1_a
    time_extract_a_first = max(time_extract_b_first, time_scan_a_first) + p2_a
    
    return (time_extract_b - time_extract_a_first)

def compare(a, b):
    p1_a, p2_a = a
    p1_b, p2_b = b
    
    # We want to sort such that doing a then b gives better or equal result than b then a
    # Compute end times for both sequences
    
    # a then b
    scan_a_end = p1_a
    extract_a_end = scan_a_end + p2_a
    scan_b_start = extract_a_end
    scan_b_end = scan_b_start + p1_b
    extract_b_start = max(extract_a_end, scan_b_end)
    extract_b_end = extract_b_start + p2_b
    
    # b then a
    scan_b_end_2 = p1_b
    extract_b_end_2 = scan_b_end_2 + p2_b
    scan_a_start_2 = extract_b_end_2
    scan_a_end_2 = scan_a_start_2 + p1_a
    extract_a_start_2 = max(extract_b_end_2, scan_a_end_2)
    extract_a_end_2 = extract_a_start_2 + p2_a
    
    diff = extract_b_end - extract_a_end_2
    
    if diff < 0:
        return -1
    elif diff > 0:
        return 1
    else:
        return 0

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    sectors = []
    index = 1
    for _ in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        sectors.append((p1, p2))
        index += 2
    
    # Sort using Johnson's rule heuristic
    # For two jobs, we should do job i before job j if:
    # min(p1_i, p2_j) <= min(p1_j, p2_i)
    
    def johnson_compare(a, b):
        p1_a, p2_a = a
        p1_b, p2_b = b
        val_a_b = min(p1_a, p2_b)
        val_b_a = min(p1_b, p2_a)
        if val_a_b < val_b_a:
            return -1
        elif val_a_b > val_b_a:
            return 1
        else:
            return 0
    
    sectors.sort(key=cmp_to_key(johnson_compare))
    
    # Simulate the schedule
    current_time = 0  # Time when next scan can start
    extraction_complete_time = 0  # Time when previous extraction completes
    
    for p1, p2 in sectors:
        # Start scan as soon as possible
        scan_start = current_time
        scan_end = scan_start + p1
        
        # Extraction can start when both:
        # 1. This sector's scan is done (scan_end)
        # 2. Previous sector's extraction is done (extraction_complete_time)
        extraction_start = max(scan_end, extraction_complete_time)
        extraction_end = extraction_start + p2
        
        current_time = scan_end
        extraction_complete_time = extraction_end
    
    print(extraction_complete_time)

if __name__ == "__main__":
    main()