# Problem B — Sequencing the Batch on One Station

Time limit: 2 s   Memory limit: 256 MB

## Description
A single station must work through a batch of unit-time tasks, one after another, until the whole batch is
done. Some tasks produce sub-assemblies that other tasks consume, which imposes precedence requirements:
whenever one task must finish before another can begin, the first task has to appear earlier in the
station's processing order than the second. Because there is only one station, exactly one task is in
progress at any moment and the schedule is simply a linear order of all the tasks.

Setup times, task priorities, due dates, and the physical nature of the sub-assemblies are all irrelevant
to acceptance; the only thing that constrains the order is the collection of "finish-before-start"
requirements between pairs of tasks. (You are guaranteed that the sum, over all tasks, of the number of tasks they directly wait for exactly equals $m$, and that no single task is involved in more than $m$ requirements in total.) A valid answer is any complete ordering of every task in the batch that honours all of these requirements at once.

Produce such an ordering, or report that the requirements are mutually contradictory — for instance if a
cycle of dependencies makes it impossible to place every task after all the tasks it depends on. (With
several stations and a deadline this kind of planning becomes genuinely hard; on a single station with no
deadline, honouring the finish-before-start requirements is all that is asked, and any order that respects
them is acceptable.)

## Input
First line: two integers n, m. Each of the next m lines: two integers a b — job a before job b.

## Output
Print `YES` then a permutation of 1..n (a valid processing order); otherwise `NO`.

## Example 1
### Input
```
3 2
1 2
2 3
```
### Output
```
YES
1 2 3
```

## Example 2
### Input
```
3 3
1 2
2 3
3 1
```
### Output
```
NO
```
