# Single-Station Manufacturing Sequence

Time limit: 2 s   Memory limit: 256 MB

## Description
A single workstation must execute $n$ distinct manufacturing steps. The workstation handles only one step at a time, and every step must be executed exactly once.

The process is governed by $m$ strict conditions. Each condition is defined by a pair of steps, $a$ and $b$, and dictates that step $a$ must be fully executed at some position in the sequence prior to the initiation of step $b$. The amount of time or the number of intermediate steps between $a$ and $b$ does not matter, provided $a$ happens earlier.

You must arrange all $n$ steps into a single chronological sequence from first to last that satisfies all $m$ conditions simultaneously. If the given conditions logically contradict each other (for example, if they indirectly require a step to be executed before itself), no such sequence is possible.

Produce a valid sequence, or report that it is impossible. Any sequence of all $n$ steps that respects every condition is considered correct.

## Input
The first line contains two integers $n$ and $m$, representing the number of manufacturing steps and the number of conditions, respectively. The steps are identified by integers from $1$ to $n$.
Each of the following $m$ lines contains two integers $a$ and $b$, indicating that step $a$ must be executed before step $b$.

## Output
If a valid sequence is possible, output `YES` on the first line, followed by a second line containing a sequence of the integers $1$ through $n$ separated by spaces. If multiple valid sequences exist, you may output any of them.
If no valid sequence can be formed, output `NO`.

## Example
### Input
```
4 5
1 2
1 3
3 2
2 4
3 4
```

### Output
```
YES
1 3 2 4
```
