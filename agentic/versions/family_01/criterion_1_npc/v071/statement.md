# Frequency Band Allocation

Time limit: 2 s   Memory limit: 256 MB

A network administrator is deploying a local wireless infrastructure consisting of $n$ access points. To avoid signal interference, the access points must be assigned to one of three distinct frequency bands, labeled 1, 2, and 3.

Certain pairs of access points have overlapping coverage areas and therefore cannot operate on the same frequency band. The conflict topology is provided as a list of overlapping pairs. 

Because interference is often localized, networks typically have a sparse conflict structure. In such well-behaved topologies, administrators can often finalize the band plan by simply processing the access points one by one, greedily assigning the lowest available band (1, 2, or 3) that does not conflict with its already-configured neighbors. 

However, your program must be completely robust. You must determine if *any* interference-free assignment is possible for the given network using exactly three bands. If multiple valid assignments exist, you must output the lexicographically first sequence of bands (comparing the band of access point 1 first, then access point 2, and so on). If no such configuration is possible under any assignment, report that it cannot be done.

## Input
The first line contains two integers $n$ and $m$ — the number of access points and the number of overlapping pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of access points with overlapping coverage.

## Output
If no valid assignment of the three bands exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $b_1, b_2, \ldots, b_n$ (each in $\{1,2,3\}$), where $b_i$ is the frequency band of access point $i$. This sequence must be the lexicographically smallest valid assignment.

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
