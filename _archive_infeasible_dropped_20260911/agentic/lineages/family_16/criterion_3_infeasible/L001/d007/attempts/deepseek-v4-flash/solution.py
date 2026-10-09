import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    p1 = []
    p2 = []
    idx = 2
    for i in range(j):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        p1.append(a)
        p2.append(b)
    
    # Check local contradiction
    for i in range(j):
        if p1[i] + p2[i] > T:
            print(f"JOB {i+1}")
            return
    
    # Check global contradiction
    sum1 = sum(p1)
    sum2 = sum(p2)
    if sum1 > T:
        print("LOAD 1")
    elif sum2 > T:
        print("LOAD 2")
    else:
        # Should not happen per problem statement, but just in case
        # We can output any valid certificate, but let's pick LOAD 1
        print("LOAD 1")

if __name__ == "__main__":
    main()