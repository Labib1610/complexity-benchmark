import sys
import threading

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    q1_list = []
    q2_list = []
    
    index = 2
    for i in range(j):
        q1 = int(data[index])
        q2 = int(data[index+1])
        q1_list.append(q1)
        q2_list.append(q2)
        index += 2
    
    # Check JOB certificates
    for i in range(j):
        q1 = q1_list[i]
        q2 = q2_list[i]
        # For JOB i to be invalid:
        # w1 >= q1
        # w2 - w1 >= q1 + q2 => w2 >= w1 + q1 + q2
        # w2 <= 2T - q2
        # So: w1 + q1 + q2 <= w2 <= 2T - q2
        # => w1 + q1 + q2 <= 2T - q2
        # => w1 <= 2T - q1 - 2*q2
        # But also w1 >= q1
        # So we need q1 <= 2T - q1 - 2*q2
        # => 2*q1 + 2*q2 <= 2T
        # => q1 + q2 <= T
        # If q1 + q2 > T, then JOB i is unsatisfiable
        if q1 + q2 > T:
            print(f"JOB {i+1}")
            return
    
    # Check LOAD certificates
    # For stage 1: S(w1_i, q1_i) >= 0 means min(w1_i - q1_i, 2T - q1_i - w1_i) >= 0
    # So: q1_i <= w1_i <= 2T - q1_i
    # Dispersion: |w1_i - w1_k| >= q1_i + q1_k
    # This is like placing intervals of length 2*q1_i centered at w1_i, requiring 
    # pairwise distance at least q1_i + q1_k between centers.
    # But more precisely, it's placing points in [q1_i, 2T - q1_i] with pairwise separation >= q1_i + q1_k
    
    # Similarly for stage 2.
    
    # Let's sort q1 and q2 to check if they can fit.
    # For stage 1:
    sorted_q1 = sorted(q1_list)
    # The minimum span needed is sum of all 2*q1_i (for the intervals themselves) 
    # plus sum of (j-1) separations of at least (sorted_q1[i] + sorted_q1[i+1])
    # Actually, let's think differently.
    # We have j points to place in their respective intervals [q1_i, 2T - q1_i].
    # The available space for w1_i is [q1_i, 2T - q1_i], so width 2T - 2*q1_i.
    # But actually, we want to place them respecting dispersion.
    # The total "width" available is 2T (since all w1_i must be in [min q1_i, max (2T-q1_i)] subset of [0,2T])
    # But better approach: 
    # Sort the items. Place them optimally to minimize required span.
    # Minimum required span when placing items with separations:
    # If we sort q1_i, the minimum span is sum of (2*q1_i) + (j-1)*min_separation
    # But the actual constraint is |w1_i - w1_k| >= q1_i + q1_k
    # Optimal placement: sort q1_i ascending, then place w1_i such that consecutive differences are exactly q1_i + q1_{i+1}
    # So total span = sum(2*q1_i) + sum_{i=1}^{j-1} (q1_i + q1_{i+1}) = sum(2*q1_i) + sum_{i=1}^{j-1} (q1_i + q1_{i+1})
    # = sum(2*q1_i) + sum_{i=1}^{j-1} q1_i + sum_{i=2}^{j} q1_i = sum(2*q1_i) + (sum(q1_i) - q1_j) + (sum(q1_i) - q1_1)
    # = 2*sum(q1_i) + 2*sum(q1_i) - q1_1 - q1_j = 4*sum(q1_i) - q1_1 - q1_j
    # Wait, that doesn't seem right. Let me re-think.
    # If we place points with |w_i - w_k| >= q_i + q_k, and we sort q_i ascending,
    # optimal is to place them with w_{i+1} - w_i = q_i + q_{i+1}.
    # Then w_j - w_1 = sum_{i=1}^{j-1} (q_i + q_{i+1}) = sum(q_1..q_{j-1}) + sum(q_2..q_j) = 2*sum(q_i) - q_1 - q_j
    # And each w_i needs a "buffer" of q_i around it? No, the constraint is on positions, not buffers.
    # The total span from w_min to w_max must be at least 2*sum(q_i) - q_min - q_max if we sort q.
    # But actually, the positions w_i must satisfy w_i in [q_i, 2T - q_i].
    # So w_max <= 2T - q_max and w_min >= q_min.
    # Available span is (2T - q_max) - q_min = 2T - q_min - q_max.
    # Required span is 2*sum(q_i) - q_min - q_max (if sorted with min and max at ends).
    # So if 2*sum(q_i) - q_min - q_max > 2T - q_min - q_max, i.e., 2*sum(q_i) > 2T, i.e., sum(q_i) > T, then impossible.
    
    # But wait, that's not quite right either. Let's think of it as placing intervals.
    # Each item i has a "core" point w_i that must be placed such that:
    # 1. w_i is in [q_i, 2T - q_i] (from S(w_i, q_i) >= 0)
    # 2. |w_i - w_k| >= q_i + q_k for all k != i (dispersion)
    # This is equivalent to placing intervals I_i = [w_i - q_i, w_i + q_i] such that:
    # 1. The center w_i of I_i is in [q_i, 2T - q_i]
    # 2. Intervals I_i and I_k are disjoint (since |w_i - w_k| >= q_i + q_k)
    
    # But even simpler: just check if sum(q1_i) > T for stage 1, and sum(q2_i) > T for stage 2.
    # Because if sum(q_c_i) > T, then the total "size" of all elements exceeds the capacity T,
    # making LOAD c unsatisfiable.
    
    sum_q1 = sum(q1_list)
    sum_q2 = sum(q2_list)
    
    if sum_q1 > T:
        print("LOAD 1")
        return
        
    if sum_q2 > T:
        print("LOAD 2")
        return

if __name__ == '__main__':
    threading.Thread(target=main).start()