# Phase Two: Robotic Assembly Coordination

Time limit: 5 s   Memory limit: 256 MB

## Description
To fulfill a client's order, our manufacturing plant executes a strict three-phase workflow. In Phase One, raw materials are processed into basic components. This phase is already complete, and all components have been delivered to the factory floor. Following our work, the product will immediately enter Phase Three for quality assurance, packaging, and shipping. 

Your responsibility is exclusively to manage Phase Two: the primary assembly. The client has stipulated that Phase Three must begin no later than a specific time, meaning Phase Two must be fully completed within $T$ operational cycles. 

Our assembly floor is equipped with $M$ identical robotic arms. During any single cycle, each arm can execute exactly one assembly operation. Consequently, the maximum number of operations that can be performed concurrently in a single cycle cannot exceed the number of available arms. 

There are $n$ distinct operations to be completed in Phase Two. Because of the physical design of the product, certain operations are prerequisites for others. If operation $b$ requires the output of operation $a$, then $a$ must be fully completed in an earlier cycle before $b$ can be initiated. They cannot occur in the same cycle, as the output of an operation only becomes available at the start of the subsequent cycle. 

Determine a valid cycle assignment for all $n$ operations such that no cycle is assigned more than $M$ operations, all prerequisite conditions are satisfied, and all operations are completed within the $T$ available cycles. If it is impossible to meet these requirements, report that the schedule is unfeasible.

## Input
The first line contains four integers: $n$, $M$, $T$, and $m$. 
Each of the following $m$ lines contains two integers $a$ and $b$, indicating that operation $a$ is a prerequisite for operation $b$. Operations are numbered from 1 to $n$.

## Output
If a valid assignment exists, print `YES` followed by $n$ integers. The $i$-th integer must represent the cycle (from 1 to $T$) in which operation $i$ is executed. If no such assignment is possible, print `NO`.

## Example

**Input**
```
4 2 2 2
1 3
2 4
```

**Output**
```
YES
1 1 2 2
```
