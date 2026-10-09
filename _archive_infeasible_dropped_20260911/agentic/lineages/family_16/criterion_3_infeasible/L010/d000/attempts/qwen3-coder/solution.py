import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    idx = 2
    build_times = []
    verify_times = []
    
    for i in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        build_times.append(p1)
        verify_times.append(p2)
        
        # Check sequential bottleneck
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    # Check server overload
    total_build = sum(build_times)
    total_verify = sum(verify_times)
    
    if total_build > T:
        print("LOAD 1")
        return
    if total_verify > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()