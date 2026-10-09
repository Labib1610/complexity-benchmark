# Problem A — Security Tier Allocation

Time limit: 2 s   Memory limit: 256 MB

A distributed architecture consists of $n$ modules, which are subject to $m$ separation protocols. Each separation protocol acts as a strict restriction between a given pair of modules. 

The system utilizes exactly three security tiers, denoted by the integers 1, 2, and 3. A valid configuration of the architecture requires that every module is assigned exactly one security tier, with the condition that no two modules connected by a separation protocol share the same tier.

Your task is to determine whether the entire architecture can be configured under these conditions. If a valid configuration exists, you must output the sequence of security tiers that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ (1 ≤ $n$ ≤ 40, 0 ≤ $m$ ≤ $n(n−1)/2$) — the number of modules and the number of separation protocols.
Each of the following $m$ lines contains two integers $u$ and $v$ (1 ≤ $u, v$ ≤ $n$, $u \neq v$) representing a separation protocol between module $u$ and module $v$.

## Output
If no valid configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \dots, c_n$ (where each $c_i \in \{1, 2, 3\}$) representing the security tier of each module. This sequence must be the lexicographically smallest among all valid configurations (comparing $c_1$ first, then $c_2$, and so on).

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
