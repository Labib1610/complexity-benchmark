import sys
import threading

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    p1_list = []
    p2_list = []
    
    index = 2
    for i in range(j):
        p1 = int(data[index])
        p1_list.append(p1)
        index += 1
        p2 = int(data[index])
        p2_list.append(p2)
        index += 1
    
    # Check JOB i
    for i in range(j):
        total = p1_list[i] + p2_list[i]
        if total > T:
            print(f"JOB {i+1}")
            return
    
    # Check LOAD 1
    sum_p1 = sum(p1_list)
    if sum_p1 > T:
        print("LOAD 1")
        return
    
    # Check LOAD 2
    sum_p2 = sum(p2_list)
    if sum_p2 > T:
        print("LOAD 2")
        return

if __name__ == '__main__':
    threading.Thread(target=main).start()