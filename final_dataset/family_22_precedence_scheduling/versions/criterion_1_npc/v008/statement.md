# Problem A — Meeting the Deadline Across Parallel Assembly Stations

Time limit: 5 s
Memory limit: 256 MB

## Description
The production workflow at our plant consists of three stages. First, design blueprints are compiled into a batch of assembly tasks and their dependencies. Second, the plant must complete this batch of assembly tasks before a hard delivery deadline. Third, the completed units undergo final packaging for shipment. Your system is responsible only for the second stage.

All tasks take the same amount of time — one time slot each — and are carried out on a bank of identical parallel stations. In any single time slot, each station handles at most one task, so the number of tasks that can be in progress during any one slot is capped by the number of stations; there is no benefit to leaving a station idle, but there is also no penalty beyond the deadline.

The tasks are not independent. Some tasks produce sub-assemblies consumed by others, giving rise to precedence requirements: whenever one task must finish before another can begin, the dependent task has to be placed in a strictly later slot than the task it depends on — being in the same slot is not enough, since a sub-assembly finished in a slot is only available from the next slot onward. Setup times, task priorities, and which specific station runs a task are irrelevant; a task may run on any station, and only the slot it occupies matters.

The deadline is expressed as a maximum number of slots. Assign every task a slot within the deadline so that all precedence requirements hold and no slot is assigned more tasks than there are stations, or report that the batch cannot be finished by the deadline. Once your schedule is generated, the third stage will commence. (With few stations the per-slot cap and the precedence chains pull against each other, so a schedule that respects precedence may still overflow the slot capacity and vice versa.)

## Input
First line: four integers n, M, T, m. 
Each of the next m lines: two integers a b — job a must finish before job b starts.

## Output
Print `YES` then n integers slot[1..n] (the time slot of each job, in 1..T); otherwise `NO`.

## Example

**Input:**
```
4 2 3 3
1 2
1 3
2 4
```

**Output:**
```
YES
1 2 2 3
```
