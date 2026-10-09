import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    jobs = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        jobs.append((p1, p2))
    
    group1 = []
    group2 = []
    for p1, p2 in jobs:
        if p1 <= p2:
            group1.append((p1, p2))
        else:
            group2.append((p1, p2))
    
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: x[1], reverse=True)
    
    order = group1 + group2
    
    fab_time = 0
    asm_time = 0
    for p1, p2 in order:
        fab_time += p1
        if asm_time < fab_time:
            asm_time = fab_time
        asm_time += p2
    
    print(asm_time)

if __name__ == "__main__":
    main()