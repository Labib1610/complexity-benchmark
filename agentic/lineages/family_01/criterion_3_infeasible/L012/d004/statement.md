# Problem C — System Instability

Time limit: 2 s
Memory limit: 256 MB

You are analyzing a distributed monitoring network consisting of $n$ sensors. The network is designed to operate by assigning each sensor to one of two available frequency bands. 

The provided configuration lists $m$ hardware interlocks between pairs of sensors. A safety rule dictates that if two sensors share an interlock, they must not be assigned to the same frequency band. 

However, the current configuration is fundamentally flawed. To demonstrate this flaw, you must identify a minimal contradiction: a group of exactly three distinct sensors that cannot be legally assigned. Specifically, you must find three sensors such that, no matter how you allocate them between the two frequency bands, at least one pair among these three sensors will both share an interlock and be placed in the same band.

It is guaranteed that the provided configuration contains at least one such group of three sensors. Your task is to find and report one.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of sensors and the number of interlocks, respectively. Sensors are numbered from $1$ to $n$.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that sensor $u$ and sensor $v$ share an interlock. It is guaranteed that at least one such group of three sensors exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, representing the identifiers of the three sensors that form the flaw. 

The identifiers must be printed in ascending order ($a < b < c$). If there are multiple valid groups of three sensors, you must output the one that is lexicographically smallest. This means you should first minimize $a$; if there are ties, minimize $b$ among those ties; and if there are still ties, minimize $c$.

## Example 1
**Input:**
```
4 5
1 2
1 3
2 3
2 4
3 4
```
**Output:**
```
1 2 3
```

## Example 2
**Input:**
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
**Output:**
```
1 2 4
```