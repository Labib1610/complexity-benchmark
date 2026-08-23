# Critical Interference

Time limit: 2 s
Memory limit: 256 MB

A network administrator is attempting to partition $n$ communication terminals (numbered 1 through $n$) into two separate operational frequencies. The system log provides $m$ records of terminal pairs that will trigger a severe interference event if they are forced to broadcast on the exact same frequency.

Due to the distribution of these interference records, it is known to be impossible to achieve a safe two-frequency partition. To formally document the failure, you must output a minimal proof of impossibility. You need to find a terminal $x$ that experiences interference with two other distinct terminals $y$ and $z$, under the condition that $y$ and $z$ also experience interference with each other. This exact configuration ensures that the three terminals cannot be safely divided across only two frequencies.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of terminals that experience interference if on the same frequency. 
It is guaranteed that at least one such configuration of three terminals exists.

## Output
Print the three integer identifiers of these terminals on one line, sorted in ascending order. 
If there are multiple valid configurations, output the one that is lexicographically smallest (smallest first integer; resolving ties by the second integer, then the third).

## Example 1
### Input
```
4 5
1 2
1 3
2 3
2 4
3 4
```
### Output
```
1 2 3
```

## Example 2
### Input
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
### Output
```
1 2 4
```