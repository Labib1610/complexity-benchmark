# Problem B — Sequencing the Batch on One Station

Time limit: 2 s   Memory limit: 256 MB

## Description
A single station must work through a batch of unit-time tasks, one after another, until the whole batch is
done. Some tasks produce sub-assemblies that other tasks consume, which imposes a specific rule:
whenever one task produces what another needs, the first task has to appear earlier in the
station's processing sequence than the second. Because there is only one station, exactly one task is in
progress at any moment and the sequence is simply a linear arrangement of all the tasks.

Setup times, task priorities, due dates, and the physical nature of the sub-assemblies are all irrelevant
to acceptance; the only thing that constrains the arrangement is the collection of these relative ordering
rules between pairs of tasks. A valid answer is any complete arrangement of every task in the batch
that satisfies all of these rules at once.

Produce such an arrangement, or report that the rules cannot all be simultaneously satisfied — for instance if a
closed loop of requirements makes it impossible to place every task after all the tasks it requires. (With
several stations and a deadline this kind of planning becomes genuinely difficult; on a single station with no
deadline, satisfying the relative ordering rules is all that is asked, and any arrangement that respects
them is acceptable.)

## Input
First line: two integers $n$, $m$, representing the number of tasks (numbered $1$ to $n$) and the number of rules. 
Each of the next $m$ lines: two integers $a$ $b$ — task $a$ must appear earlier in the sequence than task $b$.

## Output
Print `YES` then a permutation of $1 \dots n$ (a valid processing sequence); otherwise print `NO`.

## Example 1

**Input**
```text
3 2
1 2
2 3
```

**Output**
```text
YES
1 2 3
```

## Example 2

**Input**
```text
3 3
1 2
2 3
3 1
```

**Output**
```text
NO
```
