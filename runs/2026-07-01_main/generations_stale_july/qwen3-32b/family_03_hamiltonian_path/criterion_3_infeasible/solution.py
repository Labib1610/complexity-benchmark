import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    m = data[1]
    degrees = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        degrees[u] += 1
        degrees[v] += 1
        idx += 2
    for i in range(1, n + 1):
        if degrees[i] == 0:
            print(i)
            return

if __name__ == "__main__":
    main()