import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    brackets = []
    idx = 1
    for _ in range(j):
        d1 = int(data[idx])
        d2 = int(data[idx+1])
        brackets.append((d1, d2))
        idx += 2
    
    # Sort by d1 descending
    brackets.sort(key=lambda x: -x[0])
    
    alpha_pos = 0
    beta_pos = 0
    for d1, d2 in brackets:
        alpha_pos += d1
        beta_pos = max(beta_pos, alpha_pos) + d2
    
    print(beta_pos)

if __name__ == "__main__":
    main()