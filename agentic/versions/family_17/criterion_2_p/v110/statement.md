# Full-Capacity Modular Assembly

Time limit: 2 s
Memory limit: 256 MB

## Description
A manufacturing plant needs to assemble $2q$ distinct modules into composite units. The modules are numbered from $1$ to $2q$. The manufacturing process dictates that modules $1$ through $q$ are forged with outward-facing pins, while modules $q+1$ through $2q$ are forged with inward-facing slots.

A valid composite unit is formed by joining exactly one module with pins and one module with slots. However, due to microscopic variations during production, not all pin-slot combinations fit together. You are provided with a list of $t$ tested configurations that are known to fit perfectly. Unlisted combinations will fail to join and are strictly forbidden. The list may contain densely overlapping options, with many more tested configurations than will ultimately be used.

Each module can only be incorporated into a single composite unit, as the joining process permanently locks them together. To meet the production quota, no module can be discarded or left unused. You must determine if a subset of the tested configurations can be chosen such that all $2q$ modules are successfully locked into composite units. If such a full assembly is possible, you must output the chosen configurations.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing half the total number of modules and the number of tested configurations, respectively.
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that the outward-facing module $a$ and the inward-facing module $b$ can be joined.

## Output
If a full assembly is possible, print `YES` on the first line, followed by $q$ lines each containing the two module identifiers for an active combination in your selection. If no such assembly is possible, print `NO`.

## Example
### Input
```text
3 4
1 4
2 5
3 5
2 6
```

### Output
```text
YES
1 4
3 5
2 6
```
