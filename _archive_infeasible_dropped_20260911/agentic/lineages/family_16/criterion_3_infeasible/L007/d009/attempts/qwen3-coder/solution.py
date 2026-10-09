import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    graphs = []
    total_p1 = 0
    total_p2 = 0
    
    idx = 2
    for i in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        graphs.append((p1, p2))
        total_p1 += p1
        total_p2 += p2
        # Check if individual job is impossible
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    # Check if phase 1 is overloaded
    if total_p1 > T:
        print("LOAD 1")
        return
        
    # Check if phase 2 is overloaded
    if total_p2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()