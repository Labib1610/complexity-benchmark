# Problem A — Bio-containment Protocols

Time limit: 2 s   Memory limit: 256 MB

A research facility needs to safely store $n$ biological samples. The facility is equipped with three isolated containment units, designated by the numbers 1, 2, and 3. Each sample must be placed into exactly one of these three units.

Due to chemical volatility, certain pairs of samples are cross-reactive. If any two cross-reactive samples are placed into the same containment unit, their airborne byproducts will mix and ruin both samples. You are provided with a list of all cross-reactive pairs.

Determine if it is possible to distribute all the samples among the three units without placing any cross-reactive pair together. If a safe distribution is possible, you must find a valid arrangement. To comply with the facility's standardized logging system, if there are multiple safe arrangements, you must output the sequence of unit assignments that is lexicographically smallest. (A sequence $A$ is lexicographically smaller than $B$ if, at the first sample index $i$ where they differ, $A$ assigns sample $i$ to a lower-numbered unit than $B$ does).

## Input
The first line contains two integers $n$ and $m$ — the total number of biological samples and the number of cross-reactive pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$). The samples are numbered from 1 to $n$.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), representing a pair of samples that are cross-reactive and cannot share a containment unit.

## Output
If there is no way to safely store all samples, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $c_1, c_2, \dots, c_n$ separated by spaces, where $c_i \in \{1, 2, 3\}$ is the containment unit assigned to sample $i$. This sequence must be the lexicographically smallest valid assignment.

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
