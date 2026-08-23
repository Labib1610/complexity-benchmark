# Phase II: Deployment Partitioning

Time limit: 1 s   Memory limit: 256 MB

A manufacturing facility is overhauling its workforce scheduling pipeline. In Phase I of this pipeline, an automated profiling tool evaluates all $n$ employees and flags $m$ pairs of individuals whose concurrent presence on the factory floor causes severe operational disruptions.

Your task is to implement Phase II. You must allocate the $n$ employees into exactly two distinct operational rotations, designated by the rotation codes `1` and `2`. To prevent disruptions, if two employees were flagged as a pair in Phase I, they must receive different rotation codes.

Once Phase II successfully generates a valid rotation sequence, it is passed to Phase III, where the payroll subsystem applies rotation-specific multipliers. To ensure deterministic behavior in Phase III, if multiple valid rotation assignments exist, you must produce the one that has the smaller rotation code at the earliest employee index where two valid assignments differ. If no valid allocation can be formed, the pipeline must halt.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of employees and the number of flagged pairs from Phase I.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — a pair of employees who must not receive the same rotation code.

## Output
If the Phase II allocation cannot be completed without placing a flagged pair in the same rotation, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers separated by spaces, where the $i$-th integer (each being `1` or `2`) is the rotation code assigned to employee $i$. This sequence must be the valid assignment that has the smaller rotation code at the earliest index where it differs from any other valid assignment.

## Example 1
### Input
```
4 4
1 2
2 3
3 4
1 4
```
### Output
```
YES
1 2 1 2
```

## Example 2
### Input
```
3 3
1 2
1 3
2 3
```
### Output
```
NO
```
