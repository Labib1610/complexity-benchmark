# Problem A — Delegate Voting

Time limit: 2 s
Memory limit: 256 MB

A legislative assembly consists of $n$ delegates. Each delegate must be assigned to support exactly one of three distinct policy proposals. The available proposals are designated by the integers 1, 2, and 3.

The assembly is subject to $m$ dispute records. Each record specifies a pair of delegates who hold opposing viewpoints. To prevent committee deadlocks, the two delegates in any dispute pair must be assigned different proposals (i.e., if delegate $u$ and delegate $v$ form a dispute pair, their assigned proposal numbers $c_u$ and $c_v$ must satisfy $c_u \neq c_v$).

Your task is to determine whether it is possible to assign proposals to all $n$ delegates such that all dispute records are respected. If it is possible, provide a valid proposal assignment.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of delegates and the number of dispute records.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing that delegate $u$ and delegate $v$ form a dispute pair. It is guaranteed that each unordered pair $\{u, v\}$ appears at most once in the input.

## Output
If there is no valid proposal assignment, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $c_1, c_2, \dots, c_n$, where each $c_i \in \{1, 2, 3\}$ is the proposal assigned to delegate $i$. If multiple valid assignments exist, you may output any of them.

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