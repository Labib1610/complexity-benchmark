# Problem B — Sequencing the Batch on One Station

Time limit: 2 s   Memory limit: 256 MB

## Description
A certain facility is equipped with a single processing unit. This unit is responsible for executing a batch of $n$ unit-time procedures, identified by integers from $1$ to $n$. Within this batch, there are $m$ strict chronological dependencies. Each dependency dictates that a specific procedure must be fully completed before another specific procedure is allowed to start. Since the processing unit lacks parallel capabilities, it will execute the procedures one by one, forming a single continuous sequence of all $n$ procedures. The physical nature of the procedures, their setup times, and any potential due dates are disregarded; the sequence is constrained exclusively by the $m$ dependencies.

You must find a full sequence of the $n$ procedures that strictly adheres to all given dependencies. Any sequence that achieves this is acceptable. If the dependencies form a contradiction—making it impossible to arrange the procedures without violating at least one dependency—you must indicate that no such arrangement can be formed.

## Input
The first line contains two integers $n$ and $m$.
Each of the subsequent $m$ lines contains two integers $a$ and $b$, indicating that procedure $a$ must be completed before procedure $b$ can start.

## Output
If a valid continuous sequence is possible, print `YES` followed by a permutation of the integers from $1$ to $n$ (separated by spaces) representing the execution order. If multiple valid sequences exist, any of them will be accepted. If no such sequence is possible, print `NO`.

## Example

### Input
4 4
1 2
2 3
1 4
4 3

### Output
YES
1 4 2 3
