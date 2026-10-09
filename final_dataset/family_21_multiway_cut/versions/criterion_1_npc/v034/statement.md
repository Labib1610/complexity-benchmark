# Problem A — Securing a Subterranean Vault Complex

Time limit: 5 s   Memory limit: 256 MB

## Description
A subterranean vault complex consists of various chambers linked by passageways. Each passageway requires a specific quantity of explosive charges to collapse, rendering it permanently impassable in both directions.

Certain chambers house highly reactive anomalies. To prevent a catastrophic resonance cascade, no two anomalies can be allowed to communicate. Communication occurs if there is any sequence of intact passageways that allows transit from one anomaly's chamber to another's, regardless of how many intermediate empty chambers are traversed.

The demolition crew must select a set of passageways to collapse. The objective is to ensure that for every possible pair of anomalies, there is no intact route between their respective chambers. Chambers that do not contain anomalies do not have any specific requirements and can end up accessible from anywhere, as long as the anomalies themselves cannot reach one another. The total expenditure of the operation is the sum of the explosive charges required for the collapsed passageways.

The crew is given a strict explosive supply limit. They must determine if it is possible to collapse a valid set of passageways using a total number of charges that does not exceed this limit. If such a set exists, they must detail which passageways to collapse. Otherwise, they must report that the operation cannot be completed within the supply limit.

## Input
Line 1: four integers $n$, $m$, $k$, $B$.
Line 2: $k$ chamber IDs where anomalies are housed.
Next $m$ lines: three integers $u$ $v$ $w$ — a passageway between $u$ and $v$ requiring $w$ charges to collapse.

## Output
`YES`, then a line with the number $c$ of collapsed passageways, then $c$ lines "$u$ $v$"; or `NO`.

## Example

### Input
```text
5 5 3 10
1 3 5
1 2 4
2 3 5
2 4 2
4 5 3
1 4 8
```

### Output
```text
YES
2
2 3
4 5
```
