# Problem B — Sequencing the Batch on One Station

Time limit: 2 s   Memory limit: 256 MB

## Description
A single station must work through a batch of $n$ unit-time tasks, one after another, until the whole batch is done. There are $n!$ potential permutations of the tasks to consider. Some tasks produce sub-assemblies that other tasks consume, which imposes precedence requirements: whenever one task must finish before another can begin, the first task has to appear earlier in the station's processing order than the second. Because there is only one station, exactly one task is in progress at any moment and the schedule is simply a linear order of all the tasks.

To find an acceptable arrangement from the vast number of potential schedules, you must ensure your chosen sequence satisfies all constraints simultaneously. Setup times, task priorities, due dates, and the physical nature of the sub-assemblies are all irrelevant to acceptance; the only thing that constrains the order is the collection of "finish-before-start" requirements between pairs of tasks. A valid answer is any complete ordering of every task in the batch that honours all of these requirements at once.

Search the space of permutations to produce such an ordering, or report that the requirements are mutually contradictory — for instance if a cycle of dependencies makes it impossible to place every task after all the tasks it depends on. (While scheduling typically requires exploring an enormous configuration space to meet deadlines across several stations, on a single station with no deadline, finding any order that respects the finish-before-start requirements is all that is asked.)

## Input
First line: two integers $n, m$. Each of the next $m$ lines: two integers $a$ and $b$ — job $a$ before job $b$.

## Output
Print `YES` then a permutation of $1..n$ (a valid processing order); otherwise `NO`.

## Example

### Input
```
4 4
1 2
1 3
2 4
3 4
```

### Output
```
YES
1 2 3 4
```
