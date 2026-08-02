# Problem B — Research Facility Scheduling

Time limit: 1 s   Memory limit: 256 MB

A research facility operates two isolated laboratories, designated as Laboratory 1 and Laboratory 2. The facility employs $n$ researchers, numbered $1$ through $n$, and maintains a list of $m$ restriction pairs representing researchers who interfere with each other's equipment and thus cannot work in the same laboratory.

Determine whether it is possible to assign every researcher to either Laboratory 1 or Laboratory 2 such that no pair of restricted researchers is assigned to the same laboratory. If a valid assignment exists, find the lexicographically smallest assignment sequence.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — indicating that researcher $u$ and researcher $v$ cannot share a laboratory.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES`, and on a second line print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment of researchers to laboratories.

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
