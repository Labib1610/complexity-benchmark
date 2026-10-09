# Problem B — Sequence Generation Stage

Time limit: 2 s   Memory limit: 256 MB

## Description
In the automated manufacturing pipeline, processing a batch of unit-time tasks is divided into three stages: requirements gathering, sequence generation, and execution. You are responsible only for the middle step: sequence generation.

The preceding requirements gathering stage has already analyzed the batch and produced a list of precedence requirements. These occur because some tasks produce sub-assemblies that other tasks consume: whenever one task must finish before another can begin, the first task has to appear earlier in the station's processing order than the second. Because the subsequent execution stage uses only one station, exactly one task is in progress at any moment and the schedule is simply a linear order of all the tasks.

Setup times, task priorities, due dates, and the physical nature of the sub-assemblies are handled elsewhere and are irrelevant to this step's acceptance; the only thing that constrains your order is the collection of "finish-before-start" requirements between pairs of tasks. A valid answer is any complete ordering of every task in the batch that honours all of these requirements at once, which will then be passed to the execution stage.

Produce such an ordering, or report that the requirements are mutually contradictory — for instance if a cycle of dependencies makes it impossible to place every task after all the tasks it depends on. (With several stations and a deadline this kind of planning becomes genuinely hard; on a single station with no deadline, honouring the finish-before-start requirements is all that is asked, and any order that respects them is acceptable.)

## Input
First line: two integers n, m. Each of the next m lines: two integers a b — job a before job b.

## Output
Print `YES` then a permutation of 1..n (a valid processing order); otherwise `NO`.

## Example

### Input
```text
4 4
1 2
1 3
2 4
3 4
```

### Output
```text
YES
1 2 3 4
```
