# Problem A — Three-Stage Allocation

Time limit: 2 s   Memory limit: 256 MB

A manufacturing process is divided into three parallel stages: Stage 1, Stage 2, and Stage 3. You must assign each of the $n$ tasks to exactly one of these stages.

Certain pairs of tasks are incompatible and cannot be processed in the same stage. However, the system provides considerable flexibility: because there are three stages in total, an incompatibility between two tasks only restricts them from sharing a stage. If one task is already assigned to a stage, the other task still has two completely valid alternatives available. 

Given this flexibility, determine whether it is possible to assign all $n$ tasks without placing any incompatible pair in the same stage.

## Input
The first line contains two integers $n$ and $m$ — the number of tasks and the number of incompatibilities ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a pair of tasks that cannot share a stage.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{1, 2, 3\}$), where $s_i$ is the stage assigned to task $i$. Any valid assignment is accepted.

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
