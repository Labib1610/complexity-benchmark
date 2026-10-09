def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr += 1
    t = int(input[ptr])
    ptr += 1

    required = list(map(int, input[ptr:ptr + t]))
    ptr += t

    connected = [False] * (n + 1)
    for _ in range(m):
        u = int(input[ptr])
        ptr += 1
        v = int(input[ptr])
        ptr += 1
        w = int(input[ptr])
        ptr += 1
        connected[u] = True
        connected[v] = True

    candidates = [x for x in required if not connected[x]]
    print(min(candidates))

if __name__ == "__main__":
    main()