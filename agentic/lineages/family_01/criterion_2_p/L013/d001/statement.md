# Magnetic Resonance Equilibrium

Time limit: 1 s
Memory limit: 256 MB

A particle accelerator must maintain equilibrium across $n$ magnetic containment fields. To achieve this, each field's calibration dial must be locked to a value of either 1 or 2.

The system's integrity is monitored by $m$ load balancers. Rather than tracking individual fields, each balancer is wired to a specific pair of fields. For a balancer to remain stable, the combined total of the calibration values on its two assigned fields must equal exactly 3. Any other sum (2 or 4) causes an immediate system halt.

You must find a valid assignment of calibration values to all $n$ fields such that no balancer destabilizes. In the event that several valid assignments are possible, the system defaults to the lexicographically smallest sequence of values (meaning the sequence $s_1, s_2, \dots, s_n$ is minimized element by element, starting with the first field).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that a load balancer is wired to field $u$ and field $v$.

## Output
If no stable assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, \dots, s_n$ (each being 1 or 2) representing the lexicographically smallest stable configuration.

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