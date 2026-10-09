import sys, random, time

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx+=1
    m = int(input_data[idx]); idx+=1
    k = int(input_data[idx]); idx+=1
    prods = []
    for _ in range(k):
        s = int(input_data[idx]); t = int(input_data[idx+1]); d = int(input_data[idx+2]); idx+=3
        prods.append((s,t,d))
    edges = []
    for _ in range(m):
        u = int(input_data[idx]); v = int(input_data[idx+1]); c = int(input_data[idx+2]); idx+=3
        edges.append((u,v,c))
    ...