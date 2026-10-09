import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    p1_total = 0
    p2_total = 0
    flows = []
    
    index = 2
    for i in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        p1_total += p1
        p2_total += p2
        flows.append((p1, p2))
        index += 2
    
    # Check for Ingress saturation
    if p1_total > T:
        print("LOAD 1")
        return
    
    # Check for Egress saturation
    if p2_total > T:
        print("LOAD 2")
        return
    
    # Check for causal violation
    for i in range(j):
        p1, p2 = flows[i]
        # To avoid BLOCKED, all egress must come before any ingress
        # Best case: place all egress first, then ingress
        # This uses (p2 + p1) slots. If this exceeds T, it's a causal violation
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return

if __name__ == "__main__":
    main()