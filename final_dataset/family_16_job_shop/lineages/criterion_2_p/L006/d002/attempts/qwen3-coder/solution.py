import sys
from itertools import accumulate

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    ships = []
    index = 1
    for _ in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        ships.append((p1, p2))
        index += 2
    
    # Sort ships by p1 - p2
    ships.sort(key=lambda x: x[0] - x[1])
    
    # Compute prefix sums of p1
    p1_list = [ship[0] for ship in ships]
    prefix_p1 = [0] + list(accumulate(p1_list))
    
    # Compute suffix sums of p2
    p2_list = [ship[1] for ship in ships]
    suffix_p2 = list(accumulate(p2_list[::-1]))[::-1] + [0]
    
    # Find the minimum of max T(k) over all k
    min_clearance = float('inf')
    for k in range(1, j+1):
        Tk = prefix_p1[k] + suffix_p2[k-1]
        if Tk < min_clearance:
            min_clearance = Tk
            
    print(min_clearance)

if __name__ == "__main__":
    main()