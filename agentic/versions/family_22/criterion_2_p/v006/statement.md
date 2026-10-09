# Problem B — Executing the Migration Batch on One Server

Time limit: 2 s   Memory limit: 256 MB

## Description
A single database server must work through a batch of unit-time migration scripts, one after another, until the whole batch is applied. Some scripts create tables that other scripts modify, which imposes precedence requirements: whenever one script must finish before another can begin, the first script has to appear earlier in the server's execution order than the second. Because there is only one server, exactly one script is in progress at any moment and the schedule is simply a linear order of all the scripts.

Setup times, script priorities, due dates, and the specific SQL commands are all irrelevant to acceptance; the only thing that constrains the order is the collection of "finish-before-start" requirements between pairs of scripts. A valid answer is any complete ordering of every script in the batch that honours all of these requirements at once.

Produce such an ordering, or report that the requirements are mutually contradictory — for instance if a cycle of dependencies makes it impossible to place every script after all the scripts it depends on. (With several servers and a deadline this kind of planning becomes genuinely hard; on a single server with no deadline, honouring the finish-before-start requirements is all that is asked, and any order that respects them is acceptable.)

## Input
First line: two integers $n, m$. 
Each of the next $m$ lines: two integers $a$ $b$ — script $a$ must execute before script $b$.

## Output
Print `YES` then a permutation of $1..n$ (a valid execution order); otherwise `NO`.

## Example 1

### Input
```text
3 2
1 2
2 3
```

### Output
```text
YES
1 2 3
```

## Example 2

### Input
```text
3 3
1 2
2 3
3 1
```

### Output
```text
NO
```
