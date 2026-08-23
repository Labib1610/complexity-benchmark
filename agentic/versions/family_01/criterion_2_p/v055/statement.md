# Plasma Containment Grid

Time limit: 1 s
Memory limit: 256 MB

You are commissioning a fusion reactor's plasma containment grid. The grid is driven by $n$ electromagnetic coils, labeled 1 to $n$. To maintain magnetic confinement, each coil requires a fixed polarity assignment: either positive (1) or negative (2).

The reactor's blueprints detail $m$ thermal proximity links between specific pairs of coils. When two coils share a proximity link, their magnetic fluxes will constructively interfere and melt the shielding unless they operate with opposite polarities.

You must determine if a polarity assignment exists for all $n$ coils that prevents shielding failure. The control software records the configuration as a sequence of $n$ numbers (1s and 2s) ordered by coil label. To pass automated safety checks, if multiple safe configurations exist, you must provide the one whose sequence is lexicographically smallest.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of coils and the number of proximity links.
Each of the following $m$ lines provides two integers $u$ and $v$, indicating a proximity link between coil $u$ and coil $v$.

## Output
If it is impossible to assign polarities safely, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers (each 1 or 2) representing the lexicographically smallest safe polarity sequence.

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
