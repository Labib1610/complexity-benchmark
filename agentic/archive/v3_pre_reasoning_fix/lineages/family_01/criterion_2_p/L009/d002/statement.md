# Signal Amplifiers

Time limit: 1 s   Memory limit: 256 MB

You are configuring a network of $n$ signal amplifiers, numbered 1 through $n$. Each amplifier must be assigned a gain multiplier of either 1 or 2.

The network contains $m$ critical connections. Each connection links two amplifiers, $u$ and $v$. The combined amplification across a connection is calculated as the product of the gain multipliers of the two linked amplifiers. 

To ensure system stability, the combined amplification for every critical connection must be exactly 2. If the product is 1, the signal drops out; if the product is 4, the hardware overloads.

Your task is to determine whether it is possible to assign a gain multiplier to every amplifier such that all $m$ connections are stable.

If a valid configuration exists, you must provide it. Because there may be multiple valid configurations, you must output the lexicographically smallest sequence of gain multipliers. A sequence $s_1, \dots, s_n$ is lexicographically smaller than another valid sequence $t_1, \dots, t_n$ if, at the first index $i$ where they differ, $s_i < t_i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of amplifiers and the number of critical connections.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — the indices of the amplifiers linked by a critical connection.

## Output
If there is no way to assign the multipliers 1 and 2 to all amplifiers such that all $m$ connections have a combined amplification of exactly 2, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $g_1 \dots g_n$ (each being 1 or 2), representing the lexicographically smallest valid sequence of gain multipliers.

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