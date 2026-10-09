import sys
import threading

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    p1 = []
    p2 = []
    
    index = 1
    for i in range(j):
        p1.append(int(data[index]))
        p2.append(int(data[index+1]))
        index += 2
    
    # Create list of (p1[i], p2[i], index)
    trains = [(p1[i], p2[i], i) for i in range(j)]
    
    # Sort using Johnson's rule for optimal sequence
    # For two machine flow shop scheduling to minimize makespan
    # We sort based on the following criteria:
    # If min(p1[i], p2[i]) <= min(p1[j], p2[j]), then i comes before j
    
    # Actually, for F2||Cmax (two-machine flow shop to minimize makespan), 
    # the optimal algorithm is to use Johnson's rule:
    # - Partition jobs into two sets:
    #   S1 = {jobs where p1 <= p2}
    #   S2 = {jobs where p1 > p2}
    # - Sort S1 by p1 ascending
    # - Sort S2 by p2 descending
    # - Sequence is S1 followed by S2
    
    S1 = []  # jobs with p1 <= p2
    S2 = []  # jobs with p1 > p2
    
    for i in range(j):
        if p1[i] <= p2[i]:
            S1.append((p1[i], p2[i], i))
        else:
            S2.append((p1[i], p2[i], i))
    
    # Sort S1 by p1 ascending
    S1.sort(key=lambda x: x[0])
    # Sort S2 by p2 descending
    S2.sort(key=lambda x: x[1], reverse=True)
    
    # Final sequence is S1 + S2
    sequence = S1 + S2
    
    # Now simulate the processing according to this sequence
    A_prev = 0  # Time when previous train finishes lower segment
    B_prev = 0  # Time when previous train finishes upper segment
    
    for p1_i, p2_i, idx in sequence:
        A_curr = A_prev + p1_i
        B_curr = max(A_curr, B_prev) + p2_i
        A_prev = A_curr
        B_prev = B_curr
    
    print(B_prev)

# Use threading to avoid recursion limit issues
threading.Thread(target=main).start()