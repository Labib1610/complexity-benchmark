# Problem B — Digital Asset Routing Schedule

Time limit: 2 s
Memory limit: 256 MB

## Description
A regulatory mandate requires a financial institution to execute a bulk transfer of a specific digital asset. The transfer must move a fixed target volume of the asset from a designated origin ledger to a final destination ledger during a single overnight processing window. The asset moves across a network of registered institutional ledgers connected by unidirectional cryptographic bridges.

To prevent systemic risk, each bridge is assigned a strict upper limit on the volume of the asset it can process in a single night. The asset is indivisible and transfers cannot be reversed, so the volume routed across any bridge must be a non-negative integer. Because the intermediate ledgers belong to third parties acting solely as routing agents, they cannot absorb or provide any liquidity. Consequently, the total volume of the asset entering any intermediate ledger must perfectly match the total volume leaving it. The origin ledger must have a net outflow equal to the target volume, and the destination ledger must have a net inflow equal to the target volume.

You must design a routing schedule that successfully moves the exact target volume without exceeding the risk limit of any bridge. If no such schedule is possible under the risk limits, you must flag the transfer as infeasible.

## Input
The first line contains three integers: `n m 1`, where `n` is the number of ledgers, `m` is the number of bridges, and `1` indicates the single asset type. 
The second line contains three integers: `s t d`, where `s` is the origin ledger, `t` is the destination ledger, and `d` is the target volume. 
The next `m` lines each contain three integers: `u v cap`, representing a unidirectional bridge from ledger `u` to ledger `v` with a risk limit of `cap`.

## Output
If a valid routing schedule exists, print `YES` on the first line. On the second line, print `m` space-separated integers representing the volume of the asset routed across each bridge, in the exact order the bridges were provided in the input. 
If no valid schedule is possible, print `NO`.

## Example

### Input
```text
4 5 1
1 4 10
1 2 10
1 3 5
2 3 5
2 4 5
3 4 10
```

### Output
```text
YES
5 5 0 5 5
```
