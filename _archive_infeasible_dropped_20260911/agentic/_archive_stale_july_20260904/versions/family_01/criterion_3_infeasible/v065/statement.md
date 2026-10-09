# Problem C — Artifact Exhibition

Time limit: 2 s
Memory limit: 256 MB

You are curating a display of $n$ delicate historical artifacts, numbered 1 through $n$. Due to their varied material compositions, certain pairs of artifacts require mutually exclusive atmospheric conditions and cannot be housed in the same display case.

You want to design a special "contrast exhibit" featuring exactly three distinct artifacts. To highlight the extreme differences in their preservation needs, every artifact chosen for this specific exhibit must be atmospherically incompatible with both of the other two artifacts in the exhibit.

Your task is to select three artifacts that meet this strict requirement.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of artifacts and the number of incompatible pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ — indicating that artifacts $u$ and $v$ are incompatible.
It is guaranteed that at least one valid group of three mutually incompatible artifacts exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are incompatible. Output the lexicographically smallest such group (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
