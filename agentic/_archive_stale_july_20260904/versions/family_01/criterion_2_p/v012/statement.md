# Clockwork Configuration

Time limit: 1 s
Memory limit: 256 MB

You are designing the internal mechanism of a large clockwork engine. The engine contains $n$ gears, numbered 1 through $n$. Each gear must be configured to spin in exactly one of two directions: direction 1 (clockwise) or direction 2 (counter-clockwise).

The design includes $m$ mechanical linkages. Each linkage directly engages two specific gears. By the laws of mechanics, any two gears that are directly engaged must spin in opposite directions to avoid jamming the engine. 

You need to determine if it is possible to assign a spin direction to every gear such that no linkages jam. If multiple valid configurations exist, you must provide the one where the sequence of spin directions, ordered from gear 1 to gear $n$, is lexicographically smallest.

## Input
The first line of the input contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of gears and the number of linkages.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — a pair of directly engaged gears.

## Output
If there is no way to assign spin directions without jamming the engine, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $s_1, \dots, s_n$ (where each $s_i \in \{1, 2\}$) representing the lexicographically smallest valid sequence of spin directions.

## Example 1
**Input:**
```
4 4
1 2
2 3
3 4
1 4
```
**Output:**
```
YES
1 2 1 2
```

## Example 2
**Input:**
```
3 3
1 2
1 3
2 3
```
**Output:**
```
NO
```
