# Problem A — Uniform Batch Processing

Time limit: 5 s   Memory limit: 256 MB

## Description
A plant processes a batch of $n$ uniform tasks. The operation is highly standardized, which simplifies the logistical constraints significantly:
- Every task takes exactly one time slot to complete.
- There are $M$ completely identical processing stations.
- Stations are interchangeable; any task can be processed by any station.
- Setup times and changeover delays are zero.
- There is no penalty for leaving a station idle during a time slot.

Because all tasks are uniform, the only structural restriction on the schedule comes from workflow dependencies. Some tasks require the output of others. If task $b$ requires the output of task $a$, task $a$ must be assigned to a strictly earlier time slot than task $b$. Tasks assigned to the same time slot run concurrently, so they cannot depend on each other.

You have a total of $T$ time slots to process all $n$ tasks. In any given time slot, you can process up to $M$ tasks (one on each station). 

Given the completely uniform processing times and the identical nature of the stations, determine if it is possible to assign each task to a time slot between 1 and $T$ (inclusive) such that all workflow dependencies are satisfied and the capacity of $M$ tasks per time slot is never exceeded.

## Input
The first line provides four integers: $n$ (the number of tasks), $M$ (the number of identical stations), $T$ (the available time slots), and $m$ (the number of workflow dependencies).
The next $m$ lines each contain two integers $a$ and $b$, indicating that task $a$ must be assigned to a strictly earlier time slot than task $b$. Tasks are numbered 1 to $n$.

## Output
If all tasks can be scheduled within the $T$ time slots, print `YES` on the first line, then on the next line print $n$ integers: the time slot (from 1 to $T$) assigned to each task 1 through $n$. If it is impossible to schedule all tasks by the deadline, print `NO`.

## Example 1

**Input:**
```
5 2 3 4
1 2
1 3
2 4
3 5
```

**Output:**
```
YES
1 2 2 3 3
```
