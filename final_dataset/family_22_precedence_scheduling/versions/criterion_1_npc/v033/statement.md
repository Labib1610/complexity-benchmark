# Problem A — Meeting the Deadline Across Parallel Assembly Stations

Time limit: 5 s   Memory limit: 256 MB

## Description
A plant must complete a batch of assembly tasks before a hard delivery deadline. All tasks take the same amount of time — one time slot each — and are carried out on a bank of identical parallel stations. In any single time slot, each station handles at most one task, so the number of tasks that can be in progress during any one slot is capped by the number of stations; there is no benefit to leaving a station idle, but there is also no penalty beyond the deadline.

The tasks are not independent. Some tasks produce sub-assemblies consumed by others, which establishes strict ordering rules: whenever one task provides a part to another, the receiving task has to be placed in a strictly later slot than the providing task — being in the same slot is not enough, since a sub-assembly finished in a slot is only available from the next slot onward. Setup times, task priorities, and which specific station runs a task are irrelevant; a task may run on any station, and only the slot it occupies matters.

The deadline is expressed as a maximum number of slots. Assign every task a slot within the deadline so that all ordering rules hold and no slot is assigned more tasks than there are stations, or report that the batch cannot be finished by the deadline. (With few stations the per-slot cap and the chains of parts production pull against each other, so a schedule that respects the ordering rules may still overflow the slot capacity and vice versa.)

## Input
First line: four integers n, M, T, m. 
Each of the next m lines: two integers a b — task a must finish before task b starts.

## Output
Print `YES` on the first line, then on the next line print n integers slot[1..n] (the time slot of each task, in 1..T); otherwise print `NO`.

## Example

### Input
```
4 2 3 3
1 2
1 3
2 4
```

### Output
```
YES
1 2 2 3
```
