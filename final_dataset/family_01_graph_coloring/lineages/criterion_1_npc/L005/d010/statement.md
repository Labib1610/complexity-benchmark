# Problem A — Distributed Sensor Network

Time limit: 2 s   Memory limit: 256 MB

You are deploying a network of $n$ sensor buoys. Each buoy must be configured with exactly one of 3 available firmware packages, identified by the integers 1, 2, and 3.

The packages operate at specific base frequencies:
- **Package 1** operates at 5409 MHz.
- **Package 2** operates at 5616 MHz.
- **Package 3** operates at 5200 MHz.

You are given a list of $m$ critical adjacent pairs of buoys. Each pair involves two specific buoys $(u, v)$ that monitor a highly volatile sector. 
To ensure stable data transmission without destructive harmonic resonance, every critical adjacent pair must be assigned packages such that the sum of their base frequencies is a perfect square. (For example, if two packages had frequencies that summed to 10000, it would be safe because $100 \times 100 = 10000$, whereas a sum of 10001 would not be safe).

You must assign a firmware package (1, 2, or 3) to each of the $n$ buoys such that all $m$ critical adjacent pairs satisfy this perfect square condition.

## Input
The first line contains two integers $n$ and $m$ — the number of buoys and the number of critical adjacent pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a critical adjacent pair of buoys. Buoys are indexed from 1 to $n$.

## Output
If no such assignment is possible, output NO on a single line.
Otherwise, output YES on the first line. On the second line, output $n$ integers $c_1 \ c_2 \dots c_n$ (each being 1, 2, or 3), where $c_i$ is the firmware package assigned to buoy $i$. If multiple valid assignments exist, you may output any of them.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```