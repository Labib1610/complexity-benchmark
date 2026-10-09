import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n_A = int(data[0])
    n_B = int(data[1])
    m = int(data[2])
    
    transfers = []
    alpha_deg = [0] * (n_A + 1)
    beta_deg = [0] * (n_B + 1)
    
    idx = 3
    for i in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        transfers.append((u, v))
        alpha_deg[u] += 1
        beta_deg[v] += 1
        idx += 2
    
    T = max(max(alpha_deg), max(beta_deg))
    
    # For each processor, we need to assign timeslots to its transfers
    # We'll use a greedy approach: for each transfer, assign the earliest available timeslot
    # that's not yet used by either its alpha or beta processor
    
    # Keep track of which timeslots are used by each processor
    alpha_slots = [set() for _ in range(n_A + 1)]
    beta_slots = [set() for _ in range(n_B + 1)]
    
    result = []
    
    for u, v in transfers:
        # Find the first available slot that's free for both processors
        slot = 1
        while slot in alpha_slots[u] or slot in beta_slots[v]:
            slot += 1
        alpha_slots[u].add(slot)
        beta_slots[v].add(slot)
        result.append(str(slot))
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()