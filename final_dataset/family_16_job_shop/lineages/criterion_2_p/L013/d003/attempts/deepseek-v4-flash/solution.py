import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    nodes = []
    total_b = 0
    for _ in range(n):
        a, b = map(int, input().split())
        nodes.append((a, b))
        total_b += b
    
    # Sort by a - b ascending
    nodes.sort(key=lambda x: x[0] - x[1])
    
    prefix_d = 0
    max_val = 0
    for a, b in nodes:
        max_val = max(max_val, a + prefix_d)
        prefix_d += (a - b)
    
    print(total_b + max_val)

if __name__ == "__main__":
    main()