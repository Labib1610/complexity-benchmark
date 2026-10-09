# Optical Switch Diagnostics

Time limit: 2 s   Memory limit: 256 MB

## Description
A high-speed optical switch contains an array of input transmitters and an array of output receivers. Fiber optic strands are patched between these two arrays, with each strand linking exactly one transmitter to exactly one receiver. 

Let $D$ be the maximum number of strands attached to any single hardware component (whether a transmitter or a receiver). Your task is to assign each strand to a diagnostic cycle numbered from $1$ to $D$. 

During any single diagnostic cycle, each transmitter and each receiver can actively test at most one strand. Therefore, strands sharing a common transmitter or receiver must be assigned to different diagnostic cycles. The structural separation between the transmitter and receiver arrays ensures that an assignment using exactly $D$ cycles is always achievable.

## Input
The first line contains three integers $n_L$, $n_R$, and $m$ ($1 \le n_L, n_R \le 100000$, $0 \le m \le 400000$), representing the number of input transmitters, the number of output receivers, and the total number of fiber optic strands, respectively.

The next $m$ lines each contain two integers $u$ and $v$ ($1 \le u \le n_L$, $1 \le v \le n_R$), indicating a strand patched between transmitter $u$ and receiver $v$.

## Output
Print `YES` on the first line. On the second line, print $m$ integers separated by spaces, where the $i$-th integer represents the diagnostic cycle assigned to the $i$-th strand in the given input order. Each cycle must be an integer between $1$ and $D$.

## Example

### Input
```text
3 3 4
1 1
1 2
2 2
3 3
```

### Output
```text
YES
1 2 1 1
```
