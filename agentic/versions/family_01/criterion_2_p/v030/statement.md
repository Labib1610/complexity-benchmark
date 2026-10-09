# Problem B — Factory Reorganization

Time limit: 1 s   Memory limit: 256 MB

The factory is restructuring its workforce. There are $n$ employees and two distinct operational branches, designated as Branch 1 and Branch 2. Every employee must be allocated to exactly one of these two branches.

During the reorganization, management has identified $m$ cases where two specific employees perform overlapping duties. If both employees in such a case are allocated to the same branch, their overlapping duties will cause delays. Therefore, for each identified case, the two employees must be placed in different branches.

Your task is to determine if it is possible to allocate all $n$ employees to the branches without any delays. If it is impossible to satisfy all separation requirements simultaneously, you must report this.

If a valid allocation exists, you must find the one that places employee 1 in the lowest possible branch number. If there are still multiple valid ways to allocate the employees, you must break ties by minimizing the branch number for employee 2, then employee 3, and so on, continuing sequentially through all employees.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of employees and the number of overlapping duty cases, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that employee $u$ and employee $v$ must be allocated to different branches.

## Output
If there is no way to place the employees to avoid all delays, output a single line with the word NO.
If it is possible, output YES on the first line. On the second line, output $n$ integers separated by spaces, where the $i$-th integer (either 1 or 2) represents the branch allocated to employee $i$, following the sequential minimization rule described above.

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
