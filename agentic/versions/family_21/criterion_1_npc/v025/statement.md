# Problem A — Shattering the Oligarchs' Trust

Time limit: 5 s   Memory limit: 256 MB

## Description
In the cyber-underworld, an information broker has mapped the communication infrastructure of a powerful cartel. The infrastructure comprises $n$ secure drop-points, linked by $m$ bidirectional encrypted tunnels. Disrupting a tunnel permanently severs that connection and incurs a specific operational cost reflecting the resources required to execute the hack.

Within this network, $k$ drop-points are designated as the personal vaults of the cartel's oligarchs. The broker's objective is to sow complete distrust among the oligarchs by partitioning the network. After the disruptions, it must be impossible for any oligarch's vault to reach the vault of any other oligarch through any sequence of intact tunnels. Drop-points that do not belong to oligarchs are collateral; they may end up connected to any single oligarch's vault, or none at all, without affecting the success of the operation. What is measured is solely the total operational cost, the sum of the costs of the tunnels actually disrupted.

The broker has a fixed operational budget $B$. You must select a subset of tunnels to disrupt such that their combined operational cost does not exceed $B$, and the removal of these tunnels guarantees that every oligarch's vault is strictly isolated from all others. If no such subset of tunnels can be found within the budget, you must report this failure. (Isolating any one pair of vaults may be cheap; the budget must cover separating all oligarchs from one another simultaneously.)

To assist in your tactical planning, the broker's intel guarantees two structural properties of the tunnel network:
1. Any sequence of tunnels that visits no drop-point more than once will involve at most $n$ distinct drop-points.
2. Every individual encrypted tunnel connects exactly two drop-point endpoints (which may or may not be distinct).

## Input
The first line contains four integers: $n$, $m$, $k$, and $B$.
The second line provides $k$ integers: the identifiers of the oligarch vaults.
The following $m$ lines each contain three integers $u$, $v$, and $w$, indicating an encrypted tunnel between drop-point $u$ and drop-point $v$ with an operational disruption cost of $w$.

## Output
If the broker can isolate all oligarch vaults within budget, print `YES` on the first line. On the second line, print an integer $c$, the number of tunnels to disrupt. On each of the next $c$ lines, print two integers $u$ and $v$ representing the endpoints of a disrupted tunnel. 
If it is impossible to isolate all oligarch vaults without exceeding the budget $B$, print `NO`.

## Example 1

### Input
```text
5 4 3 7
1 2 3
1 4 4
2 4 4
3 5 10
4 5 2
```

### Output
```text
YES
2
1 4
4 5
```

## Example 2

### Input
```text
5 4 3 5
1 2 3
1 4 4
2 4 4
3 5 10
4 5 2
```

### Output
```text
NO
```
