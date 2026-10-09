# Problem A — Instrument Calibration Conduit

Time limit: 5 s   Memory limit: 256 MB

## Description
A new control vault requires $n$ instruments to be installed along a single straight conduit. The conduit features exactly $n$ consecutive calibration slots. Each slot must house exactly one instrument, and every instrument must be assigned to exactly one slot. The slots are numbered sequentially from 1 to $n$ from one end of the conduit to the other.

Certain pairs of instruments must share a dedicated data link. These links run directly through the conduit. The physical length of a single data link is entirely determined by the separation of the slots holding its two endpoints. Specifically, if one instrument is placed in slot $x$ and another in slot $y$, the length of the link between them is $|x - y|$ units.

Procurement has allocated a strict total resource budget of $B$ units of link material for the entire installation. There is no restriction on the length of any individual link, nor on how many links overlap in the conduit. The only requirement is that the sum of the lengths of all necessary data links does not exceed $B$.

Determine if there exists a valid slot assignment for the $n$ instruments such that the sum of all data link lengths is at most $B$. If it is possible, output a valid assignment. Otherwise, report that no such assignment exists.

## Input
The first line contains three integers $n$, $m$, and $B$. 
Each of the following $m$ lines contains two integers $u$ and $v$, representing a required data link between instrument $u$ and instrument $v$ (where instruments are identified by integers from $1$ to $n$).

## Output
If a valid placement exists, print `YES` on the first line. On the second line, print $n$ space-separated integers representing the assigned slot numbers (from $1$ to $n$) for instruments $1, 2, \dots, n$ respectively. If there are multiple valid assignments, any one is acceptable. 
If no such placement is possible, print `NO`.

## Examples

**Input 1:**
```
4 4 6
1 2
2 3
3 4
4 1
```

**Output 1:**
```
YES
1 2 4 3
```

**Input 2:**
```
4 4 5
1 2
2 3
3 4
4 1
```

**Output 2:**
```
NO
```
