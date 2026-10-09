import sys

def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    j = int(input_data[0])
    jobs = []
    idx = 1
    for _ in range(j):
        p1 = int(input_data[idx])
        p2 = int(input_data[idx + 1])
        idx += 2
        jobs.append((p1, p2))
    
    group1 = []  # p1 < p2
    group2 = []  # p1 >= p2
    
    for p1, p2 in jobs:
        if p1 < p2:
            group1.append((p1, p2))
        else:
            group2.append((p1, p2))
    
    group1.sort(key=lambda x: x[0])          # ascending p1
    group2.sort(key=lambda x: -x[1])         # descending p2
    
    order = group1 + group2
    
    scan_time = 0
    load_time = 0
    for p1, p2 in order:
        scan_time += p1
        if load_time < scan_time:
            load_time = scan_time
        load_time += p2
    
    print(load_time)

if __name__ == "__main__":
    main()