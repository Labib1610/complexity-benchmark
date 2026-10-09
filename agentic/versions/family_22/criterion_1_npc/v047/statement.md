# Problem A — Freight Dispatch Sequencing

Time limit: 5 s   Memory limit: 256 MB

## Description
You are managing the dispatch of $n$ identical freight containers over a planning horizon of $T$ consecutive days. Each day, a single transport vessel departs, possessing exactly $M$ container slots. The containers are entirely uniform in size and weight, meaning any container fits into any slot without preference.

Due to assembly requirements at the receiving facility, there are $m$ sequencing mandates. A mandate specifying container $u$ and container $v$ dictates that $u$ must depart on a strictly earlier day than $v$. 

To be approved, your dispatch plan must satisfy the following conditions:
- Every container is assigned to exactly one day between day 1 and day $T$, inclusive.
- No daily vessel exceeds its maximum load of $M$ containers.
- All $m$ sequencing mandates are strictly obeyed.
- The total number of unused container slots across all $T$ vessels must equal exactly $T \times M - n$.
- For any subset of days $S \subseteq \{1, \dots, T\}$, the total number of containers dispatched on the days in $S$ must not exceed $|S| \times M$.

Determine if an approved dispatch plan exists. If one does, provide the assigned departure day for each container. You do not need to optimize for cost or minimize the number of days used; any plan meeting all conditions is acceptable.

## Input
The first line contains four integers $n$, $M$, $T$, and $m$. 
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that container $u$ must be dispatched on a strictly earlier day than container $v$.

## Output
If a valid dispatch plan exists, print `YES` followed by $n$ space-separated integers representing the assigned departure day (from 1 to $T$) for containers 1 through $n$ respectively. If no such plan is possible, print `NO`.

## Example

**Input**
```text
4 2 2 3
1 3
1 4
2 4
```

**Output**
```text
YES
1 1 2 2
```
