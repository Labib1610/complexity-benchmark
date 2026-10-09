# Problem B — Clockwork Assembly

Time limit: 1 s
Memory limit: 256 MB

You are designing the blueprint for a complex clockwork mechanism consisting of $n$ gears, numbered 1 through $n$. Each gear must be configured to rotate in one of two directions: 
- Direction 1 (clockwise)
- Direction 2 (counter-clockwise)

The blueprint includes $m$ pairs of gears that are directly meshed together. By the laws of mechanics, any two gears that are meshed together must rotate in strictly opposite directions. 

Your task is to determine if it is possible to assign a rotation direction to every gear such that all meshing constraints are satisfied. If it is possible, you must provide a valid configuration. Because the manufacturing tool requires a deterministic input, if there are multiple valid ways to configure the gears, you must provide the configuration that is lexicographically smallest when written as a sequence of $n$ integers (each being 1 or 2).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that gear $u$ and gear $v$ are meshed together. 

## Output
If the mechanism will jam and no valid rotation assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment of rotation directions.

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
