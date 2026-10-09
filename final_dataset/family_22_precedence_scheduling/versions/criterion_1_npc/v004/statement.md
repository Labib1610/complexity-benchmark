# Problem A — Meeting the Deadline Across Parallel Assembly Stations

Time limit: 5 s   Memory limit: 256 MB

## Description
A plant must complete a batch of highly uniform assembly tasks before a hard delivery deadline. Because the workload is perfectly regular—all tasks take exactly the same amount of time (one time slot each) and run on a homogenous bank of identical parallel stations—the scheduling process avoids the complexities of varying task lengths or station-specific affinities. In any single time slot, each station handles at most one task, so the number of tasks that can be in progress during any one slot is simply capped by the number of stations; there is no benefit to leaving a station idle, but there is also no penalty beyond the deadline.

The tasks share a straightforward dependency structure. Some tasks produce sub-assemblies consumed by others, giving rise to precedence requirements: whenever one task must finish before another can begin, the dependent task just has to be placed in a strictly later slot than the task it depends on—being in the same slot is not enough, since a sub-assembly finished in a slot is only available from the next slot onward. Setup times, task priorities, and which specific station runs a task are completely irrelevant; a task may run on any station, and only the slot it occupies matters.

The deadline is expressed as a maximum number of slots. Given this uniform setup, assign every task a slot within the deadline so that all precedence requirements hold and no slot is assigned more tasks than there are stations, or report that the batch cannot be finished by the deadline. (Even with perfect task uniformity, a schedule that respects precedence may still overflow the slot capacity and vice versa.)

## Input
The first line contains four integers $n$, $M$, $T$, and $m$: the number of tasks, the number of stations, the deadline in slots, and the number of dependencies. 
Each of the next $m$ lines contains two integers $a$ and $b$, indicating that task $a$ must finish before task $b$ starts.

## Output
Print `YES` followed by $n$ integers slot[1..n] (the time slot of each task, in the range 1..T); otherwise print `NO`.

## Example

### Input
```text
4 2 3 3
1 2
1 3
2 4
```

### Output
```text
YES
1 2 2 3
```
