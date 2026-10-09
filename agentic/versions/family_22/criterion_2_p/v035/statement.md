# Problem B — Sequencing the Batch on One Station

Time limit: 2 s   Memory limit: 256 MB

## Description
A single station must work through a batch of $n$ unit-time tasks, one after another, until the whole batch is done. There are $n!$ possible processing schedules to consider. Because there is only one station, exactly one task is in progress at any moment and the schedule is simply a linear sequence of all the tasks.

You must find a sequence in this vast configuration space that satisfies a given set of precedence requirements. Some tasks produce sub-assemblies that other tasks consume: whenever one task must finish before another can begin, the first task has to appear earlier in the station's processing sequence than the second. 

Setup times, task priorities, due dates, and the physical nature of the sub-assemblies are all irrelevant to acceptance; the only thing that constrains the order is the collection of "finish-before-start" requirements between pairs of tasks. A valid answer is any complete arrangement of every task in the batch that honours all of these requirements at once.

Search the space of permutations for such an ordering, or report that the requirements are mutually contradictory — meaning no valid configuration exists among all $n!$ possibilities. (With several stations and a deadline this kind of planning becomes genuinely hard; on a single station with no deadline, honouring the finish-before-start requirements is all that is asked, and any sequence from the search space that respects them is acceptable.)

## Input
First line: two integers $n$ and $m$. Each of the next $m$ lines contains two integers $a$ and $b$ — indicating that task $a$ must finish before task $b$ can start.

## Output
Print `YES` followed by a space-separated permutation of $1 \ldots n$ representing a valid processing order; otherwise print `NO`.

## Example 1
### Input
```
4 4
1 2
2 3
1 4
4 3
```
### Output
```
YES
1 2 4 3
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
