# Problem A — Surgical Schedule

Time limit: 5 s   Memory limit: 256 MB

## Description

A hospital administrator must construct a daily surgical schedule. The hospital's resources are perfectly balanced: there are exactly $k$ surgeons, exactly $k$ operating rooms, and exactly $k$ time blocks (all numbered 1 to $k$). 

Because the supply of facilities exactly matches the personnel, a schedule will utilize 100% of the hospital's capacity if and only if it consists of exactly $k$ procedures with no overlapping resources. You can view this as mapping each surgeon to a unique room and a unique time block. 

You are given a list of $t$ pre-approved templates $(x, y, z)$, meaning surgeon $x$ is compatible with room $y$ during time block $z$. 

To achieve a complete schedule, you must select exactly $k$ templates from the list such that:
- Every surgeon $x$ (from 1 to $k$) is assigned exactly one template.
- The selected templates cover every operating room $y$ (from 1 to $k$) exactly once.
- The selected templates cover every time block $z$ (from 1 to $k$) exactly once.

Determine if such a perfectly balanced assignment exists, and if so, report one valid set of templates.

## Input

The first line contains two integers $k$ and $t$ (1 ≤ $k$ ≤ 22, 0 ≤ $t$ ≤ $k \cdot k \cdot k$): the uniform size of the resource pools and the number of pre-approved templates.
Each of the next $t$ lines contains three integers $x$, $y$, $z$ (1 ≤ $x, y, z$ ≤ $k$), representing a viable template. No template is listed more than once.

## Output

If a perfectly balanced schedule exists, print `YES` on the first line, then print $k$ lines, each containing the three integers $x$ $y$ $z$ of one scheduled template. Any schedule in which every surgeon, operating room, and time block is used exactly once is accepted; the templates may be printed in any order.

If no perfectly balanced schedule exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 1 2
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

## Note

In Example 2, both viable templates use operating room 1, so operating room 2 can never be covered, making a complete schedule impossible.
