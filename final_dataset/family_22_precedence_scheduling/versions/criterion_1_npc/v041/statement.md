# Problem A — Meeting the Dispatch Limit Across Fabrication Bays

Time limit: 5 s   Memory limit: 256 MB

## Description
A manufacturing facility needs to execute a batch of fabrication steps before a final dispatch limit. Each step requires exactly one production phase to complete. The facility is equipped with a fixed number of identical active bays. During any single phase, each bay can process at most one step, which places a firm cap on how many steps can be executed concurrently in any given phase; there is no benefit to leaving a bay idle, but there is also no penalty beyond the dispatch limit.

The steps are not independent. Certain steps yield intermediate components required by others. If step $a$ provides a component for step $b$, step $a$ must be assigned to a strictly earlier phase than step $b$ (being in the same phase is not viable, as components only become available at the start of the next phase). Setup times, step priorities, and specific bay assignments are irrelevant; a step may occur in any bay, and only the phase it occupies matters.

The dispatch limit is given as a maximum number of phases. You must assign each step to a phase so that all component requirements hold and the concurrent step count in any phase fits within the bay limit, or report that the batch cannot be finished by the dispatch limit. (With few bays, the per-phase limit and the component chains pull against each other, so an arrangement that respects components may still overflow the bay capacity and vice versa.)

## Input
First line: four integers $n$, $M$, $T$, $m$ (the number of steps, the physical limit of available bays, the dispatch limit, and the number of component requirements). 
Each of the next $m$ lines: two integers $a$ and $b$ — step $a$ must be completed in a strictly earlier phase than step $b$.

## Output
Print `YES` then $n$ integers phase[1..n] (the phase of each step, ranging from the first phase up to the dispatch limit); otherwise `NO`.

## Example
### Input
```
4 2 3 3
1 2
1 3
2 4
```
### Output
```
YES
1 2 2 3
```
