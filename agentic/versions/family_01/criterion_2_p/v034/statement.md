# Problem B — Floor Operations

Time limit: 1 s
Memory limit: 256 MB

The manufacturing plant is restructuring its floor operations into process 1 and process 2. Every individual on the payroll must be allocated to exactly one of these two processes.

However, certain individuals have overlapping tool requirements. If two such individuals are placed in the same process, they will cause delays. You are given a list of these overlapping requirements. You must allocate every individual to either process 1 or process 2 such that no two individuals with overlapping requirements are placed in the same process. 

If this cannot be done, you must report it. If there are multiple valid ways to allocate the individuals, you must provide the sequence of process numbers that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$. The headcount $n$ is restricted by the facility's minimum staffing of one and its maximum occupancy of two hundred thousand. The number of logged overlapping requirements $m$ ranges from zero up to the system's storage limit of two hundred thousand.

Each of the following $m$ lines contains two integers $u$ and $v$ — the identifiers of two individuals (from $1$ to $n$) who share overlapping requirements.

## Output
If no valid allocation exists, print a single line containing `NO`.
Otherwise, print `YES`, followed by a second line containing $n$ integers $s_1 \dots s_n$ (where each $s_i$ is either $1$ or $2$), representing the lexicographically smallest valid allocation.

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
