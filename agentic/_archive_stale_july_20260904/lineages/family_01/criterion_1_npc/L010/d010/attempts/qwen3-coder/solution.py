from itertools import product

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Try all possible assignments in lexicographical order
    for assignment in product([1, 2, 3], repeat=n):
        valid = True
        for u, v in edges:
            fu = assignment[u]
            fv = assignment[v]
            # The worst case for resonance separation is when x_u and x_v are as close as possible
            # x_u can be in [fu - 1/3, fu + 1/3]
            # x_v can be in [fv - 1/3, fv + 1/3]
            # The minimum |x_u - x_v| is max(0, |fu - fv| - 2/3)
            # For stability, this must be > 1/4
            # So we need |fu - fv| - 2/3 > 1/4
            # Which means |fu - fv| > 2/3 + 1/4 = 11/12
            # Since fu, fv are integers, |fu - fv| is an integer.
            # So |fu - fv| >= 1 is required.
            # But we need |fu - fv| > 11/12, and since |fu - fv| is integer, we need |fu - fv| >= 1.
            # Actually, let's compute it precisely:
            # Minimum |x_u - x_v| = |fu - fv| - 2/3 (when they are on opposite sides)
            # We need |fu - fv| - 2/3 > 1/4
            # So |fu - fv| > 2/3 + 1/4 = 11/12
            # Since |fu - fv| is a non-negative integer, this means |fu - fv| >= 1.
            # But wait, if fu=fv, then |fu - fv| = 0, and 0 > 11/12 is false.
            # So we need |fu - fv| >= 1.
            if abs(fu - fv) < 1 + 1e-9:  # effectively |fu - fv| <= 1
                if abs(fu - fv) <= 11/12 + 1e-9:
                    valid = False
                    break
        if valid:
            print("YES")
            print(' '.join(map(str, assignment)))
            return
    
    print("NO")

if __name__ == "__main__":
    main()