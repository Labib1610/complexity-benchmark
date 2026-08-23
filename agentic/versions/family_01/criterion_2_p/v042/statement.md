# Problem B — Curatorial Dilemma

Time limit: 1 s   Memory limit: 256 MB

A museum is organizing a major retrospective and has two separate exhibition halls, Hall 1 and Hall 2. There are $n$ distinct artifacts to be displayed, numbered 1 through $n$. The curators have identified $m$ pairs of artifacts that are visually discordant. If both artifacts in a discordant pair are placed in the same hall, it ruins the aesthetic flow of the exhibition.

Your task is to assign each artifact to either Hall 1 or Hall 2 such that no two discordant artifacts end up in the same hall. If there is no way to divide the artifacts to satisfy this requirement, you must report it.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ $v$ — a discordant pair of artifacts.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $h_1 \dots h_n$ (each in $\{1,2\}$), the lexicographically smallest valid assignment.

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
