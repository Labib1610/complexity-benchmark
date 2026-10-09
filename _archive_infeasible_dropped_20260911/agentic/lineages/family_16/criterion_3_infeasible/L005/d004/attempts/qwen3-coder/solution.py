import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    p1_list = []
    p2_list = []
    
    index = 2
    for _ in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        p1_list.append(p1)
        p2_list.append(p2)
        index += 2
    
    # Check Routing Delay: Is there an item i such that p1[i] + p2[i] > T?
    for i in range(j):
        if p1_list[i] + p2_list[i] > T:
            print(f"JOB {i+1}")
            return
    
    # Check Throughput Saturation
    total_p1 = sum(p1_list)
    total_p2 = sum(p2_list)
    
    if total_p1 > T:
        print("LOAD 1")
        return
    elif total_p2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()