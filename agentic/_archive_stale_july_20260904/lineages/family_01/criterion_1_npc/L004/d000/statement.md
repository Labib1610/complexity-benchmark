# Orbital Power Routing

Time limit: 2 s   Memory limit: 256 MB

An orbital satellite contains $n$ electronic modules, numbered 1 through $n$. To distribute the electrical load, the satellite is equipped with exactly three independent power buses, designated as Bus 1, Bus 2, and Bus 3. Every module must be directly wired to exactly one of these three buses.

Due to electromagnetic sensitivity, certain pairs of modules will experience severe crosstalk if they draw power from the same bus. You are provided with a list of all such incompatible module pairs. Your task is to determine whether it is possible to assign every module to a power bus such that no two incompatible modules share a bus.

## Input
The first line contains two integers $n$ and $m$ — the number of modules and the number of incompatible pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of modules that cannot share the same bus.

## Output
If no safe routing configuration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $b_1, b_2, \dots, b_n$ (each in $\{1,2,3\}$), where $b_i$ is the bus assignment for module $i$. Among all valid assignments, output the lexicographically smallest sequence (compare $b_1$ first, then $b_2$, and so on).

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
