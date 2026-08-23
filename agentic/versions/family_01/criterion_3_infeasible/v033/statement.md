# Problem C — System Instability

Time limit: 2 s
Memory limit: 256 MB

You are analyzing a security system consisting of $n$ sensors. Certain pairs of sensors are linked by a hardware interlock. 

The system is designed to operate by assigning each sensor to one of two alternating active phases. A safety rule dictates that if two sensors are linked by an interlock, they must not be active in the same phase. However, the current configuration is fundamentally flawed. 

To demonstrate this flaw, you do not need to attempt an assignment. Instead, you must find a specific structural failure: a set of three distinct sensors that makes a two-phase assignment impossible. A set of three sensors forms a structural failure if the interlocks mandate that the first sensor cannot share a phase with the second, the second cannot share a phase with the third, and the third cannot share a phase with the first. 

It is guaranteed that the provided configuration contains at least one such set of three sensors. Your task is to find and report one.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of sensors and the number of interlocks, respectively. Sensors are numbered from $1$ to $n$.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that sensor $u$ and sensor $v$ are linked by an interlock. Interlocks are bidirectional. It is guaranteed that no pair is listed more than once, and that at least one structural failure of three sensors exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, representing the identifiers of the three sensors that form the structural failure. 

The identifiers must be printed in ascending order ($a < b < c$). If there are multiple valid sets of three sensors, you must output the one that is lexicographically smallest. This means you should first minimize $a$; if there are ties, minimize $b$ among those ties; and if there are still ties, minimize $c$.

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
