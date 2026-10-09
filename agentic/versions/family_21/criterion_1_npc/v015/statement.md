# Decommissioning a Chemical Plant

Time limit: 5 s   Memory limit: 256 MB

## Description
A chemical processing plant is undergoing decommissioning. The plant consists of $n$ processing units connected by $m$ pipes. Each pipe requires a specific financial expenditure to cap, which permanently prevents any fluid transfer through it in either direction.

There are $k$ specific units that previously housed highly reactive catalysts. Safety regulations mandate that no two catalyst units can ever exchange fluid, even indirectly through a sequence of uncapped pipes. To achieve this, a selection of pipes must be capped. The remaining uncapped pipes may still connect ordinary units to each other or to a single catalyst unit, which is permissible as long as no path exists between any two catalyst units.

The decommissioning fund provides a maximum allocation of $B$ for the entire capping operation. Determine if there is a single set of pipes to cap whose total expenditure does not exceed this allocation, and which successfully leaves every catalyst unit isolated from all others. If such a plan exists, you must also provide the list of pipes to cap.

## Input
The first line contains four integers $n$, $m$, $k$, and $B$.
The second line contains $k$ integers representing the identifiers of the catalyst units.
The next $m$ lines each contain three integers $u$, $v$, and $w$, indicating a pipe connecting unit $u$ and unit $v$ that requires an expenditure of $w$ to cap.

## Output
If a valid capping plan exists within the allocation, output `YES` on the first line. On the second line, output the number of capped pipes, $c$. Then, output $c$ lines, each containing two integers $u$ and $v$ representing a capped pipe.
If no such plan is possible within the allocation, output `NO`.

## Example
**Input**
```
5 5 3 10
1 3 5
1 2 4
2 3 5
3 4 4
4 5 5
2 4 2
```

**Output**
```
YES
2
1 2
4 5
```
