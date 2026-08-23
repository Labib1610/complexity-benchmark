# Reactive Compound Storage

Time limit: 1 s   Memory limit: 256 MB

A logistics coordinator is assigning $n$ industrial chemical compounds, numbered 1 through $n$, to two available storage facilities: Facility 1 and Facility 2.

Due to off-gassing and shared ventilation systems within each facility, certain pairs of compounds will create hazardous atmospheric conditions if stored in the same building. You are provided with a manifest of $m$ such reactive pairs. To maintain safety, any two compounds listed in a pair must be placed in different facilities.

Your task is to determine whether it is possible to securely store all $n$ compounds without violating any safety restrictions.

If a safe distribution exists, you must provide the exact facility assignment for each compound. Company policy strongly prefers utilizing Facility 1 whenever possible, especially for compounds with lower identification numbers. Formally, you must output the lexicographically smallest valid sequence of facility assignments. A sequence of assignments $s_1, \dots, s_n$ is lexicographically smaller than another valid sequence $t_1, \dots, t_n$ if, at the first compound index $i$ where they differ, $s_i < t_i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of compounds and the number of hazardous pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of compounds that cannot be stored in the same facility.

## Output
If it is impossible to securely store all compounds, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid facility assignment.

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