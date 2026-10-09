import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    uplink = []
    downlink = []
    
    index = 2
    for i in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        uplink.append(p1)
        downlink.append(p2)
        index += 2
        
        # Check for fundamental delay in a single transmission
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    # Check for fundamental capacity shortfall on a single frequency
    if sum(uplink) > T:
        print("LOAD 1")
        return
        
    if sum(downlink) > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()