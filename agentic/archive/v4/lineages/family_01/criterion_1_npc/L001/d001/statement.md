# Multi-State Module Calibration

Time limit: 2 s   Memory limit: 256 MB

An industrial control array consists of $n$ distinct electronic modules, numbered sequentially from $1$ to $n$. To ensure system stability, every module $i$ must be assigned an integer operational state $s_i \in \{1, 2, 3\}$.

Certain module interactions generate harmonic resonance. Specifically, $m$ pairs of mutually disruptive modules are identified. If two modules $u$ and $v$ are designated as disruptive to each other, they cannot operate under the identical state value (that is, $s_u \neq s_v$).

Your task is to determine whether there exists a valid state assignment $s_1, s_2, \dots, s_n$ for all $n$ modules such that no disruptive pair shares the same operational state. If multiple valid assignments exist, choose the state sequence $s_1, s_2, \dots, s_n$ that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of modules and the number of disruptive pairs, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that module $u$ and module $v$ cannot share the same operational state.

## Output
If no valid state assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), representing the operational state assigned to each module, choosing the lexicographically smallest sequence.

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