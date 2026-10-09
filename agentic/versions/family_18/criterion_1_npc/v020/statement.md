# Problem A — Documentary Narrative Arcs

Time limit: 5 s   Memory limit: 256 MB

## Description
A historical documentary series is being produced, consisting of exactly $n$ consecutive episodes. The producer has selected $n$ distinct historical events to feature. Each event must be the primary focus of exactly one episode, so ordering the events is equivalent to assigning each event to a unique episode number from 1 to $n$.

The series relies on $m$ narrative arcs to tie the history together. Each arc connects a specific pair of events. When an arc links two events, the audience must hold the context of the first event in their minds until the second event is shown. The "attention stretch" of a single narrative arc is measured as the absolute difference between the episode numbers of the two events it connects. For example, if one event is featured in episode 2 and the other in episode 5, the attention stretch for that arc is 3.

To ensure the series remains easy to follow, the producer has set a strict limit on the cognitive load. The sum of the attention stretches across all $m$ narrative arcs must not exceed a given budget $B$. There is no limit on the stretch of any individual arc, only on the grand total.

Determine whether it is possible to assign each event to a distinct episode such that the total attention stretch over all narrative arcs is at most $B$. If it is possible, provide a valid episode assignment. Otherwise, report that no such assignment exists. (An assignment that minimizes stretch for some arcs may cause the total to exceed the budget due to other arcs, so local optimization does not guarantee a feasible total.)

## Input
First line: three integers $n$, $m$, $B$.
Each of the next $m$ lines: two integers $u$ $v$ — a narrative arc between event $u$ and event $v$.

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ integers separated by spaces, where the $i$-th integer is the episode number (from 1 to $n$) assigned to event $i$. If multiple valid assignments exist, output any one.
Otherwise, print `NO`.

## Example 1

### Input
```text
4 3 4
1 2
1 3
1 4
```

### Output
```text
YES
2 1 3 4
```

## Example 2

### Input
```text
4 3 3
1 2
1 3
1 4
```

### Output
```text
NO
```
