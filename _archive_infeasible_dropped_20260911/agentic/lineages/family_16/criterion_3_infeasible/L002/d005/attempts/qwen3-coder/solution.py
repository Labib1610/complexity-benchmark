import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    queries = []
    idx = 2
    for i in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        queries.append((p1, p2))
        idx += 2
    
    # Check Scenario A: Single job completion time
    for i in range(j):
        p1, p2 = queries[i]
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    # Check Scenario B: LOAD 1 (Component 1 bottleneck)
    total_p1 = sum(q[0] for q in queries)
    if total_p1 > T:
        print("LOAD 1")
        return
    
    # Check Scenario C: LOAD 2 (Component 2 bottleneck)
    total_p2 = sum(q[1] for q in queries)
    if total_p2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()