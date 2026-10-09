import sys

def main():
    k = int(sys.stdin.readline())
    fragments = [sys.stdin.readline().strip() for _ in range(k)]
    forbidden = sys.stdin.readline().strip()
    len_f = len(forbidden)
    
    for i in range(k):
        s = fragments[i]
        if len(s) < len_f:
            continue
        if forbidden in s:
            print(i + 1)
            return

if __name__ == "__main__":
    main()