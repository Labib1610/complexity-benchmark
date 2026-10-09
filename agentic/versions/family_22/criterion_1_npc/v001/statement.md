# Problem A — Arranging Steps within a Phase Limit

Time limit: 5 s   Memory limit: 256 MB

## Description
A plant must complete a batch of steps before a strict phase limit. All steps take the same amount of effort — one phase each — and are carried out subject to a simultaneous capacity limit. In any single phase, the number of steps that can be in progress is capped by this capacity limit; there is no benefit to leaving capacity unused, but there is also no penalty beyond the phase limit.

The steps are not independent. Some steps produce intermediate results consumed by others, giving rise to prerequisites: whenever one step must finish before another can begin, the dependent step has to be placed in a strictly later phase than the step it depends on — being in the same phase is not enough, since a result finished in a phase is only available from the next phase onward. Setup effort, step priorities, and which specific unit runs a step are irrelevant; a step may run anywhere in the facility, and only the phase it occupies matters.

The limit is expressed as a maximum number of phases. Assign every step a phase within the limit so that all prerequisites hold and no phase is assigned more steps than the capacity limit, or report that the batch cannot be finished within the limit. (With low capacity the per-phase cap and the prerequisite chains pull against each other, so an arrangement that respects prerequisites may still overflow the phase capacity and vice versa.)

## Input
First line: four integers n, M, T, m. Each of the next m lines: two integers a b — step a must finish before step b starts.

## Output
Print `YES` then n integers phase[1..n] (the phase of each step, in 1..T); otherwise `NO`.

## Example

**Input**
```
4 2 3 3
1 2
1 3
2 4
```

**Output**
```
YES
1 2 2 3
```
