# Problem A — Coordinating Factory Procedures

Time limit: 5 s   Memory limit: 256 MB

## Description
A manufacturing facility must execute a specific batch of procedures. The facility is equipped with a fixed number of identical fabrication units. Work is divided into discrete production cycles. Every procedure occupies exactly one fabrication unit for the duration of exactly one cycle. A unit cannot handle more than one procedure during the same cycle, meaning the maximum number of procedures that can occur simultaneously in one cycle is limited by the physical count of fabrication units; leaving a unit idle provides no benefit, but there is no penalty beyond failing to finish the batch in time.

Certain procedures produce components that are strictly required by other procedures. If procedure $a$ provides a component for procedure $b$, procedure $b$ must be assigned to a cycle that occurs strictly after the cycle assigned to procedure $a$. It is impossible for them to occur in the same cycle, as the component is only ready for use once the providing cycle concludes. Setup times, procedure priorities, and which specific unit runs a procedure are irrelevant; a procedure may run on any unit, and only the cycle it occupies matters.

The facility has a strict cutoff, representing the maximum number of cycles available to complete the entire batch. Assign each procedure to a specific cycle such that all component dependencies hold and no cycle is assigned more procedures than there are fabrication units, or report that the batch cannot be finished before the cutoff. 

## Input
The first line contains four integers $n$, $M$, $T$, and $m$. These represent the total count of procedures, the physical count of fabrication units, the cutoff (the total number of available cycles), and the number of dependency relationships, respectively.
Each of the following $m$ lines contains two integers $a$ and $b$, indicating that procedure $a$ provides a component required by procedure $b$. Procedures are numbered from $1$ to $n$.

## Output
Print `YES` then $n$ integers (the cycle assigned to each procedure, expressed as an integer from the first cycle, $1$, up to the cutoff cycle, $T$); otherwise print `NO`.

## Example

### Input
```
5 2 3 4
1 3
2 3
3 4
3 5
```

### Output
```
YES
1 1 2 3 3
```
