# Interdiction of the Contagion

Time limit: 2 s   Memory limit: 256 MB

## Description
A series of $n$ quarantine habitats are interconnected by $m$ bidirectional transit tubes. A highly infectious contagion has breached habitat $s$. To prevent the contagion from spreading to the central population at habitat $t$, a protocol must be enacted to permanently collapse a subset of the transit tubes. Collapsing a tube requires a specific yield of explosives, denoted as $w$. Once a tube is collapsed, no biological material can pass through it in either direction.

Your task is to select a subset of transit tubes to collapse such that no sequence of intact tubes allows transit between $s$ and $t$ in either direction. The total explosive yield required for the collapsed tubes must not exceed the available stockpile $B$. Habitats other than $s$ and $t$ may end up connected to either, neither, or each other; the only requirement is the absolute separation of $s$ and $t$.

To ensure the safety of the protocol, the habitat network has been constructed such that it guarantees the following structural properties:
1. **Endpoint Parity**: The sum of the number of tube endpoints attached to all habitats is exactly $2m$.
2. **Connectivity Bound**: No single habitat has more than $2m$ attached tube endpoints.

Determine if a valid collapse protocol exists within the stockpile limit $B$, and if so, identify the tubes to be collapsed.

## Input
The first line contains five integers: $n$, $m$, $s$, $t$, and $B$.
Each of the subsequent $m$ lines contains three integers $u$, $v$, and $w$, detailing a transit tube between habitat $u$ and habitat $v$ requiring an explosive yield of $w$.

## Output
If a valid protocol exists, output `YES` on the first line. On the second line, output the number of collapsed tubes $c$. On each of the next $c$ lines, output two integers $u$ and $v$ specifying a collapsed tube.
If no such protocol can be executed within the stockpile limit, output `NO`.

## Example

**Input:**
```
4 4 1 4 10
1 2 5
1 3 5
2 4 4
3 4 7
```

**Output:**
```
YES
2
2 4
1 3
```
