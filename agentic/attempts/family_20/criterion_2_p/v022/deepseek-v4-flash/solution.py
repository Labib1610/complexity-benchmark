import sys

def main():
    input = sys.stdin.readline
    Nα, Nω, m = map(int, input().split())
    jobs = []
    deg_alpha = [0] * (Nα + 1)
    deg_omega = [0] * (Nω + 1)
    
    for _ in range(m):
        u, v = map(int, input().split())
        jobs.append((u, v))
        deg_alpha[u] += 1
        deg_omega[v] += 1
    
    K = max(max(deg_alpha), max(deg_omega))
    
    # For each resource, track used colors
    used_alpha = [set() for _ in range(Nα + 1)]
    used_omega = [set() for _ in range(Nω + 1)]
    
    # We'll also maintain pointers to next free color for speed
    next_color_alpha = [1] * (Nα + 1)
    next_color_omega = [1] * (Nω + 1)
    
    result = []
    
    for u, v in jobs:
        # find smallest color not in used_alpha[u] and not in used_omega[v]
        c = max(next_color_alpha[u], next_color_omega[v])
        while c in used_alpha[u] or c in used_omega[v]:
            c += 1
        result.append(c)
        used_alpha[u].add(c)
        used_omega[v].add(c)
        next_color_alpha[u] = c + 1
        next_color_omega[v] = c + 1
    
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, result)) + "\n")

if __name__ == "__main__":
    main()