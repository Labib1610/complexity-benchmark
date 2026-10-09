# Problem B — Quarantine Protocol

Time limit: 2 s   Memory limit: 256 MB

## Description
A subterranean laboratory comprises various chambers linked by transit tunnels. Each tunnel requires a specific expenditure of resources to permanently collapse. Two specific chambers, designated as the primary and secondary hazard zones, house incompatible biological samples. 

To ensure safety, we must execute a sequence of tunnel collapses. The operation is deemed successful if it becomes impossible to navigate from the primary hazard zone to the secondary hazard zone by traversing any sequence of intact tunnels. Tunnels can be navigated in either direction. 

Other chambers are not subject to quarantine rules; they may remain accessible from either hazard zone or neither. The sole metric evaluated is the sum of the expenditures for the collapsed tunnels. We have a strict financial limit for this operation, and the total expenditure of the collapsed tunnels must not exceed this limit.

Determine a valid set of tunnels to collapse that satisfies the safety requirement without exceeding the financial limit. If no such set exists within the limit, indicate failure.

## Input
The first line contains five integers $n$, $m$, $s$, $t$, and $B$: the number of chambers, the number of tunnels, the index of the primary hazard zone, the index of the secondary hazard zone, and the financial limit. Chambers are indexed from $1$ to $n$.
The next $m$ lines each contain three integers $u$, $v$, and $w$, indicating a tunnel connecting chamber $u$ and chamber $v$ that requires an expenditure of $w$ to collapse.

## Output
If the safety requirement can be met without exceeding the budget, output `YES`. On the next line, output the number $c$ of tunnels to collapse. On the following $c$ lines, output the two chambers connected by each collapsed tunnel (as `u v`). 
If no such set of tunnels exists, output `NO`.

## Example

### Input
```
4 5 1 4 25
1 2 10
1 3 10
2 4 10
3 4 10
2 3 5
```

### Output
```
YES
2
1 2
1 3
```
