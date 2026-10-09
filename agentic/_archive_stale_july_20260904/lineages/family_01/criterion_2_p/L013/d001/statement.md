# Magnetic Resonance Equilibrium

Time limit: 1 s
Memory limit: 256 MB

A particle accelerator contains $n$ magnetic containment fields. Each field features a phase switch that must be set to position 1 or position 2. 

The accelerator is equipped with $m$ phase comparators. Each comparator links two specific fields and continuously monitors their switch positions. If a comparator reads position 1 from both of its linked fields, it triggers a low-band system halt. If it reads position 2 from both of its linked fields, it triggers a high-band system halt. A comparator remains stable as long as neither halt condition is met.

Your task is to determine whether there is a switch configuration for all $n$ fields that keeps every comparator stable. If multiple such configurations exist, the safety override protocol requires the one that is lexicographically smallest (i.e., the sequence of switch positions $s_1, s_2, \dots, s_n$ must be as small as possible when compared element by element starting from the first field).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that a phase comparator links field $u$ and field $v$.

## Output
If no stable configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, \dots, s_n$ (each being 1 or 2) representing the lexicographically smallest stable switch configuration.

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