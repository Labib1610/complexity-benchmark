# Problem B — Sequencing the Batch on One Station

Time limit: 2 s   Memory limit: 256 MB

## Description
Some tasks produce sub-assemblies that other tasks consume, which imposes precedence requirements: whenever one task must finish before another can begin, the first task has to appear earlier in a processing order than the second. A single station must work through a batch of these unit-time tasks, one after another, until the whole batch is done. Because there is only one station, exactly one task is in progress at any moment and the schedule is simply a linear order of all the tasks.

Setup times, task priorities, due dates, and the physical nature of the sub-assemblies are all irrelevant to acceptance; the only thing that constrains the order is the collection of "finish-before-start" requirements between pairs of tasks. (With several stations and a deadline this kind of planning becomes genuinely hard; on a single station with no deadline, honouring the finish-before-start requirements is all that is asked, and any order that respects them is acceptable.)

Produce a complete ordering of every task in the batch that honours all of these requirements at once, or report that the requirements are mutually contradictory — for instance if a cycle of dependencies makes it impossible to place every task after all the tasks it depends on.

## Input
First line: two integers $n$ and $m$, where $n$ is the number of tasks (numbered $1$ to $n$) and $m$ is the number of precedence requirements.
Each of the next $m$ lines: two integers $a$ and $b$ — task $a$ must finish before task $b$ starts.

## Output
Print `YES` then a permutation of $1 \ldots n$ (a valid processing order); otherwise print `NO`.

## Example 1

**Input:**
```text
3 2
1 2
2 3
```

**Output:**
```text
YES
1 2 3
```

## Example 2

**Input:**
```text
3 3
1 2
2 3
3 1
```

**Output:**
```text
NO
```
