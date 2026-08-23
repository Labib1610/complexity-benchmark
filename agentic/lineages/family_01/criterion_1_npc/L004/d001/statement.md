# Orbital Power Routing

Time limit: 2 s   Memory limit: 256 MB

An orbital satellite contains $n$ electronic modules, numbered 1 through $n$. The power management system requires each module to be configured with a specific operating state. To ensure stability, this state must be chosen from the integer values 1, 2, or 3.

Due to electromagnetic sensitivity, the satellite's diagnostic system has identified $m$ critical pairs of modules. If the two modules in a critical pair are configured with the exact same operating state, their interference exceeds safe thresholds. Consequently, for every critical pair, the assigned operating states of the two modules must differ.

Your task is to determine whether it is possible to choose an operating state for every module such that all safety protocols are satisfied.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$), representing the number of modules and the number of critical pairs, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ denoting a critical pair of modules.

## Output
If no safe configuration exists, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $b_1, b_2, \dots, b_n$, where $b_i \in \{1, 2, 3\}$ is the operating state for module $i$. If multiple valid configurations exist, output the one that is lexicographically smallest (i.e., compare $b_1$ first, then $b_2$, and so on).

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