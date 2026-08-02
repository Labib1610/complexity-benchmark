# Telemetry Frequency Band Assignment

Time limit: 1 s   Memory limit: 256 MB

An environmental survey network uses $n$ deployed telemetry modules, numbered sequentially from $1$ to $n$. Each module must be configured to operate on one of two available frequency bands, labeled $1$ and $2$.

Due to spatial proximity, certain pairs of modules experience severe signal cross-talk if configured to the same frequency band. You are given a list of $m$ such interfering module pairs. Every pair in this list must be assigned distinct frequency bands.

Determine whether it is possible to assign a band ($1$ or $2$) to every module such that no interfering pair shares a band. If possible, determine the configuration sequence $s_1, s_2, \dots, s_n$ that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$) — the number of telemetry modules and the number of interference constraints.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that module $u$ and module $v$ interfere with each other.

## Output
If no valid band assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment sequence.

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
