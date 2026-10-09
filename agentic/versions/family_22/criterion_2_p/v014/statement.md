# Problem B — Sequencing the Batch on One Station

Time limit: 2 s
Memory limit: 256 MB

## Description
A fabrication facility operates a single assembly point that processes a designated batch of operations. Each operation requires exactly one unit of processing time. The facility must execute these operations sequentially until the entire batch is completed.

Certain operations yield intermediate components that are strictly required as inputs for other operations. This creates strict prerequisites: if operation $a$ provides a component for operation $b$, the assembly point must complete $a$ at some point before initiating $b$. Because the facility has only one active assembly point, parallel execution is impossible. The schedule must be a strict linear sequence of all operations.

Factors such as equipment calibration, operational priorities, and delivery deadlines do not influence the acceptability of a schedule. The sole requirement for a valid sequence is that no operation is initiated before all of its prerequisites have been completed. Any complete execution order that satisfies every prerequisite simultaneously is acceptable.

You must construct such a sequence, or report if the prerequisites contradict one another—such as a configuration where a subset of operations mutually require each other's outputs to proceed, making it impossible to begin any of them.

## Input
The first line contains two integers $n$ and $m$, representing the total number of operations and the number of prerequisite rules, respectively. Operations are identified by integers from $1$ to $n$.
Each of the next $m$ lines contains two integers $a$ and $b$, indicating that operation $a$ must be completed before operation $b$ can begin.

## Output
If a valid sequence is possible, print `YES` followed by a space-separated permutation of the integers $1$ through $n$ representing the execution order. If no such sequence exists, print `NO`.

## Example 1

### Input
```
4 4
1 2
1 3
2 4
3 4
```

### Output
```
YES
1 2 3 4
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
