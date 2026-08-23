# Orbital Power Routing

Time limit: 2 s   Memory limit: 256 MB

An orbital satellite contains $n$ electronic modules, numbered 1 through $n$. The power management system provides three independent power buses, designated by the integers 1, 2, and 3. Every module must be powered by exactly one of these buses.

Due to electromagnetic sensitivity, the satellite's diagnostic system has identified $m$ pairs of modules that are susceptible to harmonic resonance. To prevent resonance from accumulating, the routing must guarantee that for any identified pair, the two modules draw power from separate buses.

Your task is to determine whether it is possible to assign every module to a bus such that all resonance constraints are satisfied.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$), representing the number of modules and the number of susceptible pairs, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ denoting a pair of modules susceptible to harmonic resonance.

## Output
If no safe routing exists, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $b_1, b_2, \dots, b_n$, where $b_i \in \{1, 2, 3\}$ is the bus for module $i$. If multiple valid routings exist, output the one that is lexicographically smallest (i.e., compare $b_1$ first, then $b_2$, and so on).

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