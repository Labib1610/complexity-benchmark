# Problem B — Sequencing the Batch on One Station

Time limit: 2 s   Memory limit: 256 MB

## Description
A single station must work through a batch of $n$ unit-time tasks, one after another, until the whole batch is done. Some tasks produce sub-assemblies that other tasks consume, which imposes a specific restriction: whenever one task must be completed before another can begin, the first task has to appear earlier in the station's processing sequence than the second. Because there is only one station, exactly one task is in progress at any moment and the schedule is simply a sequential arrangement of all the tasks.

Setup times, task priorities, due dates, and the physical nature of the sub-assemblies are all irrelevant to acceptance; the only thing that constrains the schedule is the collection of these completion-prerequisite rules between pairs of tasks. A valid answer is any complete arrangement of every task in the batch that satisfies all of these rules at once.

Produce such an arrangement, or report that the restrictions are mutually contradictory — for instance if a loop of prerequisites makes it impossible to place every task after all the tasks it requires. (With several stations and a deadline this kind of planning becomes genuinely hard; on a single station with no deadline, satisfying the completion-prerequisite rules is all that is asked, and any sequence that respects them is acceptable.)

## Input
First line: two integers $n$, $m$. Each of the next $m$ lines: two integers $a$ $b$ — task $a$ must be completed before task $b$.

## Output
Print `YES` then a space-separated list containing each integer from 1 to $n$ exactly once (a valid processing sequence); otherwise print `NO`.

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
