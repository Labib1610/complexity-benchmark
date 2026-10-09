# Problem C — Switch Restrictions

Time limit: 2 s   Memory limit: 256 MB

You are configuring a system of $n$ two-state switches, numbered 1 through $n$. Each switch can be set to one of two operating modes. You are provided with a list of $m$ restrictions. Each restriction is a pair of switches that are required to be set to different modes.

Your task is to identify a specific triad of switches that structurally conflict. You must find exactly three distinct switches, denoted as $a$, $b$, and $c$ (with $a < b < c$), that satisfy all of the following conditions simultaneously:
- The provided list of restrictions explicitly includes the pair of switches $a$ and $b$.
- The provided list of restrictions explicitly includes the pair of switches $b$ and $c$.
- The provided list of restrictions explicitly includes the pair of switches $a$ and $c$.

Find such a triad. If there are multiple triads that meet all three conditions, you must output the one that is lexicographically smallest. A triad $(a_1, b_1, c_1)$ is lexicographically smaller than $(a_2, b_2, c_2)$ if $a_1 < a_2$; or if $a_1 = a_2$ and $b_1 < b_2$; or if $a_1 = a_2$, $b_1 = b_2$, and $c_1 < c_2$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$, representing a restriction that switch $u$ and switch $v$ must be set to different modes.
The given restrictions will always contain at least one such triad.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ representing the identifiers of the switches in the triad.

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
