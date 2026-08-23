# Problem B — Reactive Pipelines

Time limit: 1 s
Memory limit: 256 MB

An industrial plant contains $n$ chemical processing tanks. Each tank must be configured to operate at a pressure state of either 1 or 2.

The plant features $m$ transfer valves, each regulating the flow between a specific pair of tanks. A transfer valve is stable if and only if the pressure state of one of its connected tanks is exactly twice the pressure state of the other.

You must determine if there is a valid configuration for all $n$ tanks such that all $m$ transfer valves are stable simultaneously.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that a transfer valve connects tank $u$ and tank $v$.

## Output
If no such configuration exists, print a single line NO.
Otherwise, print YES. On the second line, print $n$ integers $p_1 \dots p_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid sequence of pressure states.

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