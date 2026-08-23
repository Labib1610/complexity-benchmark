# Problem B — Reactive Pipelines

Time limit: 1 s
Memory limit: 256 MB

An industrial chemical facility contains $n$ processing tanks. To maintain operational safety, every tank must be assigned a pressure state chosen from the set $\{1, 2\}$.

The facility also includes $m$ transfer valves. Each valve connects a specific pair of tanks. For a valve to remain stable, the pressure states of the two tanks it connects must yield a bitwise AND result of 0. If this condition is not met, the valve becomes unstable.

Your task is to determine whether it is possible to assign a pressure state to every tank such that all $m$ transfer valves are strictly stable simultaneously.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that a transfer valve connects tank $u$ and tank $v$.

## Output
If it is impossible to stabilize all valves, output a single line containing NO.
Otherwise, output YES on the first line. On the second line, output $n$ integers $p_1 \dots p_n$ (where each $p_i \in \{1, 2\}$), representing the lexicographically smallest valid sequence of pressure states.

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