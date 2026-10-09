# Problem A — Organizing the Process Steps

Time limit: 5 s   Memory limit: 256 MB

## Description
A system must organize a collection of items into a sequence of steps before a hard limit. All items are uniform — occupying one step each — and are processed subject to a fixed capacity. In any single step, the number of items assigned cannot exceed this capacity; there is no benefit to leaving capacity unused, but there is also no penalty beyond meeting the limit.

The items are not independent. Some items produce outputs required by others, giving rise to dependencies: whenever one item must be ready before another can be processed, the dependent item has to be placed in a strictly later step than the item it depends on — being in the same step is not enough, since an output generated in a step is only available from the next step onward. Item priorities and which specific position within a step an item takes are irrelevant; only the step it occupies matters.

The limit is expressed as a maximum number of steps. Assign every item a step within the limit so that all dependencies hold and no step is assigned more items than the capacity, or report that the collection cannot be organized within the limit. (With a small capacity, the per-step cap and the dependency chains pull against each other, so an arrangement that respects dependencies may still overflow the step capacity and vice versa.)

## Input
First line: four integers $n$, $M$, $T$, $m$. 
Each of the next $m$ lines: two integers $a$ and $b$ — item $a$ must be assigned to an earlier step than item $b$.

## Output
Print `YES` then $n$ integers step[1..n] (the step assigned to each item, in $1..T$); otherwise `NO`.

## Example

### Input
```text
4 2 3 3
1 2
1 3
2 4
```

### Output
```text
YES
1 2 2 3
```
