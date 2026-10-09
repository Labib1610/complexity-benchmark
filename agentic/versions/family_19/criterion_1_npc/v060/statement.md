# Problem A — Asset Settlement Clearing

Time limit: 5 s
Memory limit: 256 MB

## Description
At the end of the fiscal quarter, a financial clearing house must execute a series of asset transfers between corporate accounts. Your module is responsible for compiling the daily settlement plan.

The clearing system consists of a set of corporate accounts connected by approved one-way transaction channels. Each channel has a strict regulatory limit on the total number of indivisible asset bundles it can process during the day. This limit applies to the combined sum of all asset bundles using the channel, regardless of which settlement contract they belong to. The number of bundles assigned to any channel must be a non-negative integer.

Today, there are $k$ settlement contracts that must be executed. Each contract specifies an origin account, a destination account, and an exact number of asset bundles that must be transferred. Because all contracts are settled simultaneously, they share the same transaction channels and compete for the available regulatory limits.

Your settlement plan must ensure strict zero-balance compliance for each contract individually. At any account that is neither the origin nor the destination for a specific contract, the number of asset bundles for that contract received via incoming channels must exactly equal the number forwarded via outgoing channels. For a contract's origin account, the total number of its asset bundles sent through outgoing channels minus the number received through incoming channels must exactly equal the required delivery amount. Conversely, at a contract's destination account, the total received minus the total sent must equal the required amount.

Determine if there is a valid assignment of asset bundles to transaction channels that fulfills all contracts without exceeding any channel's regulatory limit. If such an assignment exists, output it so the clearing house can execute the transfers. Otherwise, report that the settlement cannot be executed.

## Input
The first line contains three integers $n$, $m$, and $k$: the number of corporate accounts, the number of transaction channels, and the number of settlement contracts.
The next $k$ lines specify the contracts. The $i$-th of these lines contains three integers $s_i$, $t_i$, and $d_i$, representing the origin account, the destination account, and the required number of asset bundles for contract $i$.
The next $m$ lines describe the clearing system. The $j$-th of these lines contains three integers $u$, $v$, and $cap$, indicating a one-way transaction channel from account $u$ to account $v$ with a regulatory limit of $cap$ asset bundles.

## Output
If the settlement contracts can be fulfilled simultaneously, print `YES` on the first line. Then, print $k$ lines, each containing $m$ integers. The $j$-th integer on the $i$-th line must be the number of asset bundles from contract $i$ assigned to the $j$-th channel (in the exact order the channels were provided in the input).
If no such assignment is possible, print `NO`.

## Example

### Input
```text
4 5 2
1 4 2
2 3 1
1 2 2
1 3 2
2 4 2
3 4 2
2 3 1
```

### Output
```text
YES
1 1 1 1 0
0 0 0 0 1
```
