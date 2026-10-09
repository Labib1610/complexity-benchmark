# Problem B — Crew Allocation

Time limit: 1 s   Memory limit: 256 MB

A factory needs to assign each of its $n$ workers to one of two available crews. The crews are designated by the codes 1 and 2. 

Because of interpersonal conflicts, $m$ specific pairs of workers refuse to work together. For each of these pairs, the two workers involved must be assigned to different crews. 

Your objective is to find out if there is any way to assign every worker to a crew such that none of the conflicts are violated. If there is more than one valid way to distribute the workers, you must provide the assignment sequence that is lexicographically smallest. If no such assignment is possible, you must report that it cannot be done.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), the number of workers and the number of conflicts.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that worker $u$ and worker $v$ cannot share the same crew code.

## Output
If there is no way to assign the crews without violating a conflict, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment of crews to workers 1 through $n$.

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
