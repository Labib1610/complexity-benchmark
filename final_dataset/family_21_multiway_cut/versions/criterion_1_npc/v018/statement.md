# Problem A — Sealing a Facility into Isolated Containment Zones

Time limit: 5 s   Memory limit: 256 MB

## Description
A research facility is composed of multiple chambers, with certain pairs of chambers connected by passageways. Moving between chambers is possible in both directions through any open passageway. Some specific chambers are designated as high-risk zones, storing materials that are highly reactive.

The remediation team has the option to permanently weld shut any number of passageways. Welding a passageway requires a specific amount of labour and materials, represented as a numerical expense. Once a passageway is welded, it is completely impassable. Any chambers that are not high-risk zones will simply end up in whatever accessible area they fall into; their final placement does not affect safety compliance.

The mandatory safety protocol dictates that after the welding operations are complete, no two high-risk zones may remain accessible to each other. That is, there must not exist any sequence of open passageways that allows transit from one high-risk zone to another. Every high-risk zone must be completely partitioned from all the others.

The remediation team is allocated a strict maximum expenditure $B$ for these operations. Your task is to determine whether it is possible to satisfy the mandatory safety protocol such that the sum of the welding expenses for the chosen passageways does not exceed $B$, and if so, to provide a valid list of passageways to weld shut.

## Input
Line 1: four integers $n$ (total chambers), $m$ (total passageways), $k$ (number of high-risk zones), and $B$ (maximum expenditure).
Line 2: $k$ integers representing the identifiers of the high-risk zones.
Next $m$ lines: three integers $u$, $v$, and $w$ per line, representing a passageway between chamber $u$ and chamber $v$ with a welding expense of $w$. 

## Output
If a valid set of passageways can be welded without exceeding $B$, output `YES` on the first line. On the second line, output the number of passageways to weld, $c$. On the following $c$ lines, output two integers $u$ and $v$ for each passageway welded. If the protocol cannot be achieved within budget, output `NO`.

## Example

**Input**
```text
4 3 3 10
1 2 3
1 4 4
2 4 5
3 4 6
```

**Output**
```text
YES
2
1 4
2 4
```
