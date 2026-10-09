import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    index = 2
    total_p1 = 0
    total_p2 = 0
    
    for i in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        index += 2
        
        # Check if individual job exceeds window
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
            
        total_p1 += p1
        total_p2 += p2
    
    # Check if cumulative load exceeds window for either node
    if total_p1 > T:
        print("LOAD 1")
    elif total_p2 > T:
        print("LOAD 2")

if __name__ == "__main__":
    main()