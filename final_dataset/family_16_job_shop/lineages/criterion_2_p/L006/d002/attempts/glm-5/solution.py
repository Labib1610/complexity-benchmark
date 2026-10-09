import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    starships = []
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        starships.append((p1, p2))
    
    # Sort by p2 - p1 descending (equivalently, p1 - p2 ascending)
    starships.sort(key=lambda x: x[0] - x[1])
    
    # Compute prefix sums of p1
    prefix_p1 = [0] * (j + 1)
    for i in range(j):
        prefix_p1[i + 1] = prefix_p1[i] + starships[i][0]
    
    # Compute suffix sums of p2
    suffix_p2 = [0] * (j + 1)
    for i in range(j - 1, -1, -1):
        suffix_p2[i] = suffix_p2[i + 1] + starships[i][1]
    
    # Find max T(k) = prefix_p1[k] + suffix_p2[k]
    max_T = 0
    for k in range(1, j + 1):
        T_k = prefix_p1[k] + suffix_p2[k - 1]
        if T_k > max_T:
            max_T = T_k
    
    print(max_T)

if __name__ == "__main__":
    solve()