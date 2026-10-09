import sys
from functools import cmp_to_key

def compare(trains):
    # Sort by (s_i - c_i) descending, break ties by s_i descending
    def cmp(train1, train2):
        diff1 = train1[0] - train1[1]
        diff2 = train2[0] - train2[1]
        if diff1 != diff2:
            return diff2 - diff1  # Descending order of (s - c)
        else:
            return train2[0] - train1[0]  # Descending order of s
    
    return cmp_to_key(cmp)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    trains = []
    index = 1
    for _ in range(j):
        s = int(data[index])
        c = int(data[index+1])
        trains.append((s, c))
        index += 2
    
    # Sort trains according to the optimal order
    trains.sort(key=compare(trains))
    
    A = 0  # Structural completion time
    B = 0  # Cargo completion time
    
    for s, c in trains:
        A += s
        B = max(A, B) + c
        
    print(B)

if __name__ == "__main__":
    main()