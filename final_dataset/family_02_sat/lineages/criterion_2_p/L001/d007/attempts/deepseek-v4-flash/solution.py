import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    must1 = [False] * (n + 1)
    must0 = [False] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        if a == 1 and b == 1:
            must1[1] = True
        elif a == -1 and b == -1:
            must0[1] = True
    for i in range(1, n + 1):
        if must1[i] and must0[i]:
            print("NO")
            return
    print("YES")
    res = []
    for i in range(1, n + 1):
        if must1[i]:
            res.append("1")
        elif must0[i]:
            res.append("0")
        else:
            res.append("0")
    print(" ".join(res))

if __name__ == "__main__":
    main()