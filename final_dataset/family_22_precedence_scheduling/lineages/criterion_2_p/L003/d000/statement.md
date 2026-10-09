# Problem B — Sequencing the Batch on One Station

Time limit: 2 s   Memory limit: 256 MB

## Description
A single station must work through a batch of unit-time tasks, one after another, until the whole batch is done. Some tasks produce sub-assemblies that other tasks consume, which imposes ordering rules: whenever one task must be completed before another can begin, the first task has to appear earlier in the station's processing sequence than the second. Because there is only one station, exactly one task is in progress at any moment and the schedule is simply a sequence of all the tasks.

Setup times, task priorities, due dates, and the physical nature of the sub-assemblies are all irrelevant to acceptance; the only thing that constrains the sequence is the collection of "must-precede" rules between pairs of tasks. A valid answer is any complete sequence of every task in the batch that honours all of these rules at once.

Produce such a sequence, or report that the rules are mutually contradictory — for instance if a chain of rules loops back to its starting point, making it impossible to place every task after all the tasks it must follow. (With several stations and a deadline this kind of planning involves scheduling across multiple parallel tracks; on a single station with no deadline, honouring the must-precede rules is all that is asked, and any sequence that respects them is acceptable.)

## Input
First line: two integers n, m. Each of the next m lines: two integers a b — task a before task b.

## Output
Print `YES` then a permutation of 1..n (a valid processing sequence); otherwise `NO`.

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
