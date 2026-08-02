import sys

def find_smallest_interfering_set():
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    interference = [set() for _ in range(n)]
    
    index = 2
    for _ in range(m):
        u, v = int(data[index]), int(data[index + 1])
        index += 2
        # Store in a zero-based index format
        interference[u - 1].add(v - 1)
        interference[v - 1].add(u - 1)

    for i in range(n):
        for j in sorted(interference[i]):
            if j > i:
                for k in sorted(interference[j]):
                    if k > j and i in interference[k]:
                        print(i + 1, j + 1, k + 1)
                        return

if __name__ == "__main__":
    find_smallest_interfering_set()