# Problem B — Sequencing the Batch on One Station

Time limit: 2 s   Memory limit: 256 MB

## Description
A single station must work through a batch of unit-time tasks, one after another, until the whole batch is done. Some tasks produce sub-assemblies that other tasks consume, which imposes ordering rules: whenever one task produces a sub-assembly for another, the first task has to appear earlier in the station's processing sequence than the second. Because there is only one station, exactly one task is in progress at any moment and the schedule is simply a single sequence of all the tasks.

Setup times, task priorities, due dates, and the physical nature of the sub-assemblies are all irrelevant to acceptance; the only thing that constrains the sequence is the collection of these rules between pairs of tasks. A valid answer is any complete arrangement of every task in the batch that honours all of these rules at once.

Produce such an arrangement, or report that the rules are mutually contradictory — for instance if a chain of rules loops back on itself, making it impossible to place every task after all the tasks that provide for it. (With several stations and a deadline this kind of planning requires different techniques; on a single station with no deadline, honouring the rules is all that is asked, and any arrangement that respects them is acceptable.)

## Input
First line: two integers $n$ and $m$, representing the number of tasks and the number of rules. 
Each of the next $m$ lines: two integers $a$ and $b$ — task $a$ must appear before task $b$.

## Output
Print `YES` then a sequence of $1..n$ containing each integer exactly once (a valid processing sequence); otherwise print `NO`.

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
