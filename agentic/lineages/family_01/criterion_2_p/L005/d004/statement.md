# Problem B — Power Grid Synchronization

Time limit: 1 s   Memory limit: 256 MB

A regional power grid has $n$ substations. The grid contains $m$ high-voltage transmission lines, each connecting a specific pair of substations.

To maintain grid stability, the engineers must configure the phase alignment of each substation. Every substation must be permanently configured to one of two phase alignments: Alignment 1 or Alignment 2. 

For a transmission line to safely carry power, there must be a potential difference between its endpoints. Therefore, the two substations connected by any transmission line must be configured to different phase alignments. 

You must determine a phase alignment for all substations that ensures every transmission line operates safely. If the grid cannot be configured under these rules, indicate that it is impossible.

## Input
The first line provides $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), the number of substations and transmission lines, respectively.
The following $m$ lines each contain two integers $u$ and $v$ — a pair of substations connected by a transmission line.

## Output
If the grid cannot be configured safely, output NO on a single line.
If it can, output YES on the first line. On the second line, output $n$ integers $r_1 \dots r_n$ (each in {1,2}), representing the lexicographically smallest valid sequence of phase alignments for substations $1$ through $n$.

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