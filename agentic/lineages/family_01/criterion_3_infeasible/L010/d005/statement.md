# Ternary Alloy Synthesis

Time limit: 2 s   Memory limit: 256 MB

A materials science laboratory is researching a new class of materials. There are $n$ pure elements available, numbered $1$ through $n$.

Through extensive prior experimentation, the lab has catalogued $m$ stable binary alloys. Each stable binary alloy is composed of exactly two distinct pure elements.

The lab now wishes to synthesize a "ternary alloy" consisting of exactly three distinct pure elements. According to the empirical rules governing this material class, a ternary alloy is structurally sound if and only if the extraction of any single pure element from the ternary mixture leaves a binary alloy that is already catalogued as stable. Thus, no matter which one of the three elements is removed, the remaining two must correspond to one of the $m$ known stable binary alloys.

Your task is to identify three pure elements that can form a structurally sound ternary alloy. The lab's catalogue guarantees that at least one such ternary alloy is possible.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of pure elements and the number of catalogued stable binary alloys, respectively.
The next $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that the pure elements $u$ and $v$ form a catalogued stable binary alloy. Each binary alloy is listed at most once.

## Output
Output three integers $a$, $b$, and $c$ on a single line, separated by spaces, satisfying $a < b < c$, which identify the pure elements comprising the ternary alloy. Should multiple valid ternary alloys exist, provide the lexicographically smallest combination (minimize $a$, then minimize $b$, then minimize $c$).

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