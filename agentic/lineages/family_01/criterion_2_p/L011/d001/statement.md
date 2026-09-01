# Facility Staffing

Time limit: 1 s   Memory limit: 256 MB

You are managing the staffing levels for a network of facilities. The network consists of $n$ stations.
Each station $i$ must be assigned a staffing level $x_i$. By union regulations, a station requires a minimum headcount of 1 and a maximum headcount of 2. Fractional staffing is not permitted, meaning each $x_i$ must be either 1 or 2.

The stations are connected by a set of $m$ communication links. Due to bandwidth interference, every link imposes a strict requirement on its endpoints: if a link connects station $u$ and station $v$, the combined staffing level of these two stations must be exactly 3.

Your task is to determine a valid staffing assignment for all $n$ stations.
If there are multiple valid ways to staff the network, you must output the assignment that is lexicographically smallest when written as the sequence $x_1, x_2, \dots, x_n$. If it is impossible to satisfy all interference conditions simultaneously, you must report that no such assignment exists.

## Input
The first line contains two integers $n$ and $m$. The number of stations $n$ is at least 1 and bounded by a regional maximum of $2\cdot 10^5$. The number of links $m$ is at least 0 and at most $2\cdot 10^5$.
Each of the following $m$ lines contains two integers $u$ and $v$ (valid station IDs ranging from 1 to $n$), indicating that a link exists between station $u$ and station $v$.

## Output
If there is no valid staffing assignment, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $x_1, x_2, \dots, x_n$ (each being 1 or 2), representing the lexicographically smallest valid assignment.

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