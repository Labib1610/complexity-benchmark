import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    conflicts = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        conflicts[u] |= (1 << v)
        conflicts[v] |= (1 << u)
    
    # Precompute for each person the set of people they conflict with
    # We'll do backtracking with pruning
    assignment = [0] * n
    # shift_masks[0], shift_masks[1], shift_masks[2] for shifts 1,2,3
    shift_masks = [0, 0, 0]
    
    def backtrack(i):
        if i == n:
            return True
        # Try shifts 1,2,3 in order
        for shift in range(3):
            # Check if any conflict with already assigned in this shift
            if (shift_masks[shift] & conflicts[i]) == 0:
                assignment[i] = shift + 1
                shift_masks[shift] |= (1 << i)
                if backtrack(i + 1):
                    return True
                shift_masks[shift] ^= (1 << i)
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()