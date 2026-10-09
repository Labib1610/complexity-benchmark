# Energy Grid Distribution

Time limit: 2 s   Memory limit: 256 MB

## Description
A power grid contains $n$ transformer substations connected by $m$ unidirectional transmission cables. Each cable has a strict maximum rating, representing the highest integer number of megawatts it can safely carry per hour. A constant energy load of $d$ megawatts must be transferred from a generating substation $s$ to a consuming substation $t$ over the course of one hour.

You must assign a non-negative integer megawatt value to each cable. This assigned value must not exceed the cable's maximum rating. Additionally, no single cable's assigned value is permitted to exceed the aggregate sum of the maximum ratings of all $m$ cables in the grid.

At every substation excluding $s$ and $t$, the total megawatts entering through incoming cables must perfectly match the total megawatts exiting through outgoing cables, ensuring no energy is created or dissipated. At the generating substation $s$, the total exiting megawatts minus the total entering megawatts must equal exactly $d$. At the consuming substation $t$, the total entering megawatts minus the total exiting megawatts must equal exactly $d$.

Determine a valid megawatt assignment for all cables that successfully transfers the load $d$ while respecting all cable ratings and substation balancing rules. If no such configuration can be formed, you must indicate that the transfer is unachievable.

## Input
Line 1: Three integers $n$, $m$, and $1$.
Line 2: Three integers $s$, $t$, and $d$.
Next $m$ lines: Three integers $u$, $v$, and $cap$, detailing a unidirectional cable from substation $u$ to substation $v$ with a maximum rating of $cap$ megawatts.

## Output
If the load can be transferred, print `YES` on the first line. On the second line, print $m$ space-separated integers representing the assigned megawatts for each cable, in the identical order they appeared in the input. If the transfer cannot be achieved, print `NO`.

## Example

### Input
```text
4 5 1
1 4 10
1 2 5
1 3 6
2 4 5
3 4 8
2 3 2
```

### Output
```text
YES
5 5 5 5 0
```
