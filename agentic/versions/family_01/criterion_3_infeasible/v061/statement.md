# Problem C — Diagnostic Error Report

Time limit: 2 s   Memory limit: 256 MB

You are conducting a diagnostic check on a system consisting of $n$ modules. The error logs contain $m$ records, each indicating that a specific pair of modules will interfere with one another if activated simultaneously.

A cascading fault occurs among a group of modules if a direct interference record exists for every possible pair of modules chosen from that group. While a comprehensive analysis might examine all possible groups, your current objective is to isolate a single cascading fault that is formed by exactly three modules. You are guaranteed that at least one such fault exists within the system.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of modules that interfere with each other.
It is guaranteed that there is at least one cascading fault consisting of exactly 3 modules.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$, representing the three modules involved in the fault. If there are multiple valid groups of three, output the one that is lexicographically smallest (i.e., minimize $a$; in case of a tie, minimize $b$; and if still tied, minimize $c$).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
