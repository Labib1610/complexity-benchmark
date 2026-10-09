# Mechanism Design

Time limit: 1 s   Memory limit: 256 MB

You are assembling a mechanical system consisting of $n$ gears, numbered 1 through $n$. Each gear will spin continuously in one of two directions: 1 (clockwise) or 2 (counter-clockwise).

The system includes $m$ direct engagements between pairs of gears. Whenever two gears are engaged with each other, they must spin in opposite directions to prevent the mechanism from jamming.

Determine if it is possible to assign a spin direction to every gear such that no two engaged gears spin in the same direction. If it is impossible, report it. If it is possible, and there are multiple valid configurations, you must provide the configuration that is lexicographically smallest when written as a sequence of $n$ integers.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that gear $u$ and gear $v$ are engaged with each other.

## Output
If the mechanism will inevitably jam, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each in $\{1, 2\}$), representing the spin directions of gears 1 through $n$ in the lexicographically smallest valid configuration.

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
