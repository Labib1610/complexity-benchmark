# Problem A — Artifact Exhibition

Time limit: 2 s   Memory limit: 256 MB

A museum director is planning a new exhibition featuring $n$ historical relics. The facility features exactly three separate gallery wings, labeled 1, 2, and 3.

Because of clashing historical narratives, specific pairs of relics cannot be displayed in the same gallery wing. The director needs to assign each of the $n$ relics to one of the three wings such that no two clashing relics end up in the same location. It is acceptable if one or more wings remain completely empty, provided all relics are placed without any clashes. If there is no way to assign the relics without a clash, you must determine that it cannot be done.

## Input
The first line provides two integers $n$ and $m$ — the total number of relics and the number of clashing pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$ representing a clashing pair of relics.

## Output
If a clash-free assignment is impossible, output a single line with NO.
Otherwise, output YES on the first line. On the second line, output $n$ integers $z_1, z_2, \dots, z_n$ (each being 1, 2, or 3), where $z_i$ indicates the gallery wing for relic $i$.

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