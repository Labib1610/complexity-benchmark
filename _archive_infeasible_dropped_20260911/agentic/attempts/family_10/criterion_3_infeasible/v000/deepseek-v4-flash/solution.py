import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    degree = [0] * (n + 1)
    
    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        degree[u] += 1
        degree[v] += 1
    
    for i in range(1, n + 1):
        if degree[i] == 0:
            print(i)
            return

if __name__ == "__main__":
    main()