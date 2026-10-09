# Problem A — Fluid Separation Protocols

Time limit: 5 s   Memory limit: 256 MB

## Description
A chemical plant consists of a number of vats, with certain pairs of vats connected by bidirectional pipelines. Each pipeline has a deactivation expense, which is the cost to permanently block all flow through it.

Several specific vats are designated as reactive sources. Each reactive source generates a distinct chemical fluid. These fluids flow freely in both directions through any active pipelines, spreading from vat to vat across the plant.

If fluids from two or more different reactive sources ever reach the same vat (including the source vats themselves), a dangerous reaction will occur. To prevent this, you must deactivate a set of pipelines. When a pipeline is deactivated, no fluid can pass through it in either direction. Unlabeled vats are inert and can safely hold fluid from a single reactive source, or no fluid at all.

You are given a fixed budget. Determine a set of pipelines to deactivate such that the total deactivation expense does not exceed the budget, and no vat in the plant can be reached by fluids from more than one reactive source. If this is possible, you must also output the specific pipelines to deactivate. If it is impossible to achieve this within the budget, report so.

## Input
Line 1: four integers $n$, $m$, $k$, $B$. 
Line 2: $k$ integers, the IDs of the reactive sources. 
Next $m$ lines: three integers $u$, $v$, $w$ — representing a pipeline between vat $u$ and vat $v$ with deactivation expense $w$.

## Output
`YES`, then a line with the number $c$ of deactivated pipelines, then $c$ lines each containing two integers $u$ and $v$ representing a deactivated pipeline; or `NO`.

## Example 1

**Input**
```text
5 4 3 10
1 2 3
1 4 2
2 4 3
3 5 4
4 5 5
```

**Output**
```text
YES
2
1 4
2 4
```

## Example 2

**Input**
```text
5 4 3 4
1 2 3
1 4 2
2 4 3
3 5 4
4 5 5
```

**Output**
```text
NO
```
