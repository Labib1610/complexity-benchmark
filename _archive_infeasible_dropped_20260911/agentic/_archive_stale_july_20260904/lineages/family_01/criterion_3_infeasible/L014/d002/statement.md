# Problem C — Flight Manifest Rejection

Time limit: 2 s   Memory limit: 256 MB

A cargo company relies on two transport planes to ship various industrial chemicals. Many of these chemicals are volatile when mixed, meaning certain pairs will react dangerously and must be transported on different planes.

The current shipping manifest is fundamentally flawed. Your task is to generate an automated safety rejection report by finding a specific configuration of three chemicals that demonstrates this flaw.

To provide this proof, you must identify a set of exactly three chemicals that forms a 'locked' group. A group of three chemicals is considered locked if, no matter which one of the three chemicals you exclude, the other two chemicals in the group form a reactive pair explicitly listed in the input. Finding such a group formally proves the manifest is invalid.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of chemicals and the number of reactive pairs. Chemicals are numbered from $1$ to $n$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$) — a pair of chemicals that react dangerously with each other. 
It is guaranteed that at least one locked group of three chemicals exists in the given data.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the IDs of the three chemicals in the locked group.
If there are multiple such groups, output the one that is lexicographically smallest (i.e., smallest $a$; ties broken by smallest $b$; then smallest $c$).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```