# Facility Configuration State Space

Time limit: 2 s   Memory limit: 256 MB

## Description
A research facility consists of $n$ rooms and $m$ bidirectional corridors. Each corridor has a specific cost to seal. You must assign each of the $m$ corridors an independent boolean state: `true` (sealed) or `false` (open). This yields a state space of $2^m$ possible facility configurations.

Your objective is to search this state space for a configuration that satisfies two strict conditions:
1. The sum of the costs of all corridors assigned `true` must not exceed a given budget $B$.
2. There must be no sequence of `false` corridors that allows transit between designated room $s$ and designated room $t$. The connectivity among the other $n - 2$ rooms is not restricted.

Evaluate the $2^m$ possible configurations to determine if at least one configuration satisfies both the budget and the structural separation condition.

## Input
Line 1: five integers $n$, $m$, $s$, $t$, $B$.
Next $m$ lines: three integers $u$, $v$, $w$ — representing a corridor between room $u$ and room $v$ with a sealing cost of $w$.

## Output
If a valid configuration exists within the budget, output `YES` on the first line. On the second line, output the number $c$ of `true` (sealed) corridors in your configuration. Then, output $c$ lines, each containing the two rooms $u$ and $v$ connected by a sealed corridor. 
If no such configuration exists, output `NO`.

## Example

### Input
```text
4 5 1 4 12
1 2 5
1 3 5
2 4 10
3 4 10
2 3 2
```

### Output
```text
YES
2
1 2
1 3
```
