import sys

def solve():
    data = sys.stdin.buffer.read().split()
    j = int(data[0])
    performances = []
    idx = 1
    for _ in range(j):
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2
        performances.append((a, b))
    
    # Sort by review time descending
    performances.sort(key=lambda x: x[1], reverse=True)
    
    total_a = 0
    current_time = 0
    for a, b in performances:
        total_a += a
        current_time = max(current_time, total_a) + b
    
    print(current_time)

if __name__ == "__main__":
    solve()