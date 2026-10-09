# Problem B — Synchronized Asset Deployment

Time limit: 2 s
Memory limit: 256 MB

## Description
The directorate is preparing a synchronized deployment of its remote segment. The inventory consists of an even number of assets, sequentially tagged from $1$ up to $2q$. A deployment involves linking these assets into operational pairs.

Due to hardware constraints, a link is only valid if it bridges the two halves of the inventory: it must connect one asset with a tag of $q$ or lower to another asset with a tag strictly greater than $q$. Furthermore, not all such cross-half links are functional; you are provided with a registry of the specific links that have passed safety checks.

The drill mandates full participation. You must select a subset of the registered links to form a complete deployment roster. A roster is strictly acceptable if and only if every single asset (all $2q$ of them) is included in exactly one selected link. No asset may be left unassigned, and no asset may be assigned to more than one active link.

Determine whether the safety registry allows for a roster that fully commits all $2q$ assets. If so, output the links to activate; if not, report that a full commitment is impossible.

## Input
First line: two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
Next $t$ lines: two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a registered link between asset $a$ and asset $b$.

## Output
If a complete deployment roster is possible, print `YES` then $q$ lines, each containing the two tags of one activated link. If there are multiple valid rosters, any one is acceptable. Otherwise, print `NO`.

## Example
### Input
```
3 5
1 4
1 5
2 4
2 6
3 5
```

### Output
```
YES
1 4
2 6
3 5
```
