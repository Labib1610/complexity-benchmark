import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    p1 = []
    p2 = []
    
    index = 2
    for _ in range(j):
        p1_val = int(data[index])
        p2_val = int(data[index+1])
        p1.append(p1_val)
        p2.append(p2_val)
        index += 2
    
    # Check Sequential Bottleneck: T - p1[i] < p2[i] => T < p1[i] + p2[i]
    # But more accurately, a job i cannot finish within T if T < p1[i] + p2[i]
    # Because even if it starts at time 0 on M1, it finishes M1 at p1[i], 
    # then starts M2 at p1[i], finishes at p1[i]+p2[i]. Need p1[i]+p2[i] <= T.
    for i in range(j):
        if p1[i] + p2[i] > T:
            print(f"JOB {i+1}")
            return
    
    # Check Machine Capacity Limit
    sum_p1 = sum(p1)
    sum_p2 = sum(p2)
    
    if sum_p1 > T:
        print("LOAD 1")
        return
    elif sum_p2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()