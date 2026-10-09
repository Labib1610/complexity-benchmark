# Problem A — Meeting the Deadline Across Parallel Assembly Stations

Time limit: 5 s   Memory limit: 256 MB

## Description
A manufacturing facility must process a collection of assembly operations before a strict delivery cutoff. Each operation requires exactly one time interval to complete. The facility contains a fixed count of identical processing bays. During any given time interval, each bay can handle at most one operation. Consequently, the volume of operations that can be processed concurrently in the exact same time interval is physically constrained by the total bay count.

Certain operations yield components required by other operations. When such a dependency exists, the operation requiring the component can only be scheduled in a time interval strictly after the interval in which the prerequisite operation is scheduled. Operations can be processed in any bay; the only critical decision is the time interval assigned to each operation. 

You must assign a time interval to every operation. The earliest possible time interval is numbered 1, and the final available time interval is numbered exactly at the delivery cutoff. The schedule must ensure that no time interval is assigned a greater volume of operations than the facility's bay capacity, and all component dependencies are satisfied. If the facility cannot process the entire collection of operations within these physical and temporal limits, you must report this failure.

## Input
The first line provides four integers $n$, $M$, $T$, and $m$. These represent the total count of operations, the count of processing bays, the delivery cutoff, and the count of dependency rules, respectively. Operations are identified by integers from 1 to $n$.
Each of the subsequent $m$ lines contains two integers $a$ and $b$, indicating that operation $a$ produces a component required by operation $b$.

## Output
If a valid schedule can be formed, output `YES` on the first line, followed by a second line containing $n$ integers separated by spaces, where the $i$-th integer represents the time interval assigned to operation $i$. 
If it is impossible to schedule all operations within the limits, output `NO`.

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
