# Problem B — Critical Zone Isolation

Time limit: 2 s   Memory limit: 256 MB

## Description
A facility comprises $n$ zones and $m$ bidirectional conduits. Each conduit requires a specific expense to be permanently dismantled. 

Two specific zones, designated as $s$ and $t$, hold volatile materials and must be completely isolated from each other. Your task is to select a subset of conduits to dismantle such that, upon their removal, it is impossible to traverse between zone $s$ and zone $t$ using any sequence of the remaining intact conduits. Dismantling a conduit completely halts all transit through it in both directions.

Zones other than $s$ and $t$ may remain accessible to either $s$, to $t$, or to neither; their final accessibility status does not affect the validity of the isolation plan. The sole objective is to ensure that no sequence of intact conduits forms a route between $s$ and $t$.

You are provided with an expense threshold $B$. The sum of the expenses of the dismantled conduits must be less than or equal to $B$. Furthermore, it is guaranteed that no single zone is incident to more than $m$ conduits, and any valid dismantling plan will require removing at most $m$ conduits.

If it is possible to achieve the required isolation without exceeding the threshold $B$, you must determine a valid set of conduits to dismantle. Otherwise, you must report that no such plan exists.

## Input
The first line contains five integers: $n$, $m$, $s$, $t$, and $B$.
The following $m$ lines each contain three integers $u$, $v$, and $w$, representing a conduit between zone $u$ and zone $v$ with a dismantling expense of $w$.

## Output
If the isolation can be achieved within the threshold, print `YES` on the first line. On the second line, print the integer $c$, the number of conduits to dismantle. Then, output $c$ lines, each containing two integers $u$ and $v$ representing a dismantled conduit.
If it is not possible to isolate the critical zones within the threshold, print `NO`.

## Example
**Input:**
```
4 5 1 4 10
1 2 4
1 3 5
2 3 2
2 4 4
3 4 5
```

**Output:**
```
YES
2
1 2
1 3
```
