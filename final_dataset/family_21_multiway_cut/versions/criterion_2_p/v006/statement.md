# Problem B — Isolating Reactive Units

Time limit: 2 s   Memory limit: 256 MB

## Description
A specialized chemical plant consists of processing units connected by pipelines, where each pipeline requires a specific number of work-hours to safely decommission. Two specific processing units handle reactive compounds that must not be able to mix in the event of a leak: after the safety retrofit, there must be no sequence of active pipelines connecting these two units, in either direction. A decommissioned pipeline allows no fluid transfer.

The status of all other processing units is governed solely by the need to separate the two reactive units — they can be left connected to either reactive unit, provided the two reactive units are isolated from each other. The facility manager must track the total work-hours required to decommission the chosen pipelines. The plant has a strict allocation of maintenance work-hours that this total must not exceed.

Determine a set of pipelines to decommission such that their total work-hours do not exceed the allocation and their removal leaves the two reactive units disconnected, or report that the safety retrofit cannot be completed within the allocation.

## Input
Line 1: five integers $n$, $m$, $s$, $t$, $B$, representing the number of processing units, the number of pipelines, the two reactive units, and the work-hour allocation.  
Next $m$ lines: three integers $u$ $v$ $w$ — a pipeline between units $u$ and $v$ requiring $w$ work-hours to decommission.

## Output
`YES`, then a line with the number $c$ of decommissioned pipelines, then $c$ lines "$u$ $v$"; or `NO`.

## Example

### Input
```text
4 5 1 4 10
1 2 5
1 3 5
2 4 6
3 4 6
2 3 2
```

### Output
```text
YES
2
1 2
1 3
```
