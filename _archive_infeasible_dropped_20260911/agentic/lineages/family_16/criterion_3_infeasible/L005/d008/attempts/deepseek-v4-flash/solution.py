import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    items = []
    idx = 2
    for i in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        items.append((p1, p2))
    
    # JOB check
    for i, (p1, p2) in enumerate(items, start=1):
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
    
    # LOAD check
    sum1 = sum(p1 for p1, _ in items)
    sum2 = sum(p2 for _, p2 in items)
    if sum1 > T:
        print("LOAD 1")
    elif sum2 > T:
        print("LOAD 2")

if __name__ == "__main__":
    main()