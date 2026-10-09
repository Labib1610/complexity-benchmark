# Problem A — Securing a Facility into Independent Sectors

Time limit: 5 s   Memory limit: 256 MB

## Description
A research facility is a system of chambers joined by passageways, each passageway carrying a closure expense that reflects the labour and materials to block it permanently. Several chambers are designated critical locations, each holding materials that must never share an accessible zone with the materials at another critical location. The remediation team will block a chosen set of passageways; a passageway, once blocked, no longer permits transit in either direction.

After the works, the critical locations must be **mutually unreachable**: for every pair of critical locations, there must be no remaining sequence of unblocked passageways linking them, so each critical location ends up in its own independent sector of the facility. Chambers that are not critical locations may fall into whichever sector the blocking produces — their placement is unconstrained and irrelevant to acceptance. What is measured is solely the total closure expense, the sum of the expenses of the passageways actually blocked.

There is a fixed remediation budget. Choose a set of passageways to block whose total expense does not exceed the budget and whose removal leaves every pair of critical locations unreachable from one another, or report that no blocking within budget can secure all locations simultaneously. (Securing any one pair may be cheap; the budget must cover securing all locations from one another at once.)

## Input
Line 1: four integers n, m, k, B. Line 2: k critical location ids. Next m lines: three integers u v w — a passageway linking u and v with expense w.

## Output
`YES`, then a line with the number c of blocked passageways, then c lines "u v"; or `NO`.

## Example

**Input**
```text
4 3 3 10
1 2 3
1 4 4
2 4 4
3 4 4
```

**Output**
```text
YES
2
1 4
2 4
```
