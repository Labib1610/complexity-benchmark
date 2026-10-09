import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    C = int(data[1])
    for i in range(n):
        if int(data[2 + i]) > C:
            print(i + 1)
            return

if __name__ == "__main__":
    main()