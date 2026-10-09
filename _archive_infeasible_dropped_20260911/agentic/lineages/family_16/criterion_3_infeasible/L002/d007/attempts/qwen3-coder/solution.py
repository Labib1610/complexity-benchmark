import sys
import threading

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
    
    # Check for JOB certificate
    for i in range(j):
        p1 = p1_list[i]
        p2 = p2_list[i]
        # For JOB i: x_i >= 0, x_i + p1 <= y_i, y_i + p2 <= T
        # => x_i + p1 + p2 <= T => x_i <= T - p1 - p2
        # Also x_i >= 0
        # If T - p1 - p2 < 0, then no such x_i exists
        if T - p1 - p2 < 0:
            print(f"JOB {i+1}")
            return
    
    # Check for LOAD certificates
    # LOAD 1: x_i >= 0, integral of phi_i^2 = sum p1_i, x_i + p1_i <= T
    # This is equivalent to placing intervals [x_i, x_i + p1_i) in [0, T]
    # The integral of (sum phi_i)^2 = sum p1_i implies no overlap
    # So total length = sum p1_i <= T
    sum_p1 = sum(p1_list)
    if sum_p1 > T:
        print("LOAD 1")
        return
    
    # LOAD 2: y_i >= 0, integral of psi_i^2 = sum p2_i, y_i + p2_i <= T
    # Same logic: total length = sum p2_i <= T
    sum_p2 = sum(p2_list)
    if sum_p2 > T:
        print("LOAD 2")
        return

threading.Thread(target=main).start()