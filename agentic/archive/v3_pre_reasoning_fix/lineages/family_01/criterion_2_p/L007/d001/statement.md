# Problem B — Differential Comparators

Time limit: 1 s
Memory limit: 256 MB

A weather station has $n$ sensors. Each sensor must be configured with a sensitivity level of either 1 or 2.

The system relies on $m$ differential comparators to filter out noise. Each comparator is wired to two sensors. A comparator functions correctly if and only if the absolute difference between the sensitivity levels of its two connected sensors is exactly 1.

You must determine if there is a valid configuration for all $n$ sensors such that all $m$ comparators function correctly simultaneously.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that a comparator is wired to sensor $u$ and sensor $v$.

## Output
If no such configuration exists, print a single line NO.
Otherwise, print YES. On the second line, print $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid sequence of sensitivity levels.

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