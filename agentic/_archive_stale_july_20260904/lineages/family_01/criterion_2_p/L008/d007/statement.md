# Problem B — Harmonic Resonance

Time limit: 1 s   Memory limit: 256 MB

A factory employs $n$ workers, with $m$ synchronization links established among them. You must assign a shift $s_i \in \{1, 2\}$ to each worker $i$. 

To maintain proper timing, connected workers cannot operate on the same shift. For every synchronization link between two workers $u$ and $v$, they must be assigned different shifts.

Determine if there is a valid assignment of shifts for all workers such that every synchronization link is respected. 

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of workers connected by a synchronization link.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ (each in $\{1,2\}$) representing the valid assignment. If there are multiple valid assignments, output the lexicographically smallest sequence $s_1, s_2, \ldots, s_n$. (Lexicographic order compares $s_1$, then $s_2$, etc.)

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```