import sys
import threading

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
    
    # Check for order-specific contradiction
    for i in range(j):
        if p1[i] + p2[i] > T:
            print(f"JOB {i+1}")
            return
    
    # Check for workstation-specific contradiction
    total_p1 = sum(p1)
    total_p2 = sum(p2)
    
    if total_p1 > T:
        print("LOAD 1")
        return
    if total_p2 > T:
        print("LOAD 2")
        return

    # If no contradiction found (should not happen per problem statement)
    # But as per problem guarantee, one must exist, so we should have found it
    # However, let's just return the first one as fallback
    print("LOAD 1")

# Threading is used to increase recursion limit if needed, but not necessary here
threading.Thread(target=main).start()