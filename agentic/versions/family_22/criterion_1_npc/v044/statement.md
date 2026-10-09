# Problem A — Time-Aligned Manufacturing Assignments

Time limit: 5 s   Memory limit: 256 MB

## Description
A manufacturing facility must execute a set of operations before a strict global delivery cutoff. The environment is highly standardized: the facility contains a fixed number of identical processing bays, and every single operation requires exactly one uniform time interval to complete. Because all operations share this identical duration, time-slot fragmentation is impossible, allowing operations to be neatly packed into the available intervals. Furthermore, since the processing bays are perfectly interchangeable, any operation can be executed in any bay. The only parallelization limit is that the number of operations scheduled during the exact same time interval cannot exceed the total number of bays.

The operations follow a streamlined process where certain operations yield components required by others. These dependency rules simply enforce a strict chronological ordering: if an operation requires a component from a prerequisite operation, it must be scheduled in a time interval strictly after the interval of its prerequisite. The earliest available time interval is 1, and the final available interval is exactly the delivery cutoff.

Your task is to assign a specific time interval to each operation. The schedule must respect the maximum bay capacity during every interval and satisfy all dependency rules. If all operations cannot be accommodated before the cutoff under these conditions, you must report this failure.

## Input
The first line contains four integers $n$, $M$, $T$, and $m$: the total number of operations, the number of interchangeable processing bays, the global delivery cutoff, and the number of dependency rules. Operations are indexed from 1 to $n$.
The following $m$ lines each contain two integers $a$ and $b$, specifying that operation $a$ produces a component necessary for operation $b$ (meaning $b$ must occur in a later time interval than $a$).

## Output
If a valid schedule exists, print `YES` on the first line. On the second line, print $n$ space-separated integers, where the $i$-th integer is the time interval assigned to operation $i$.
If no such schedule is possible, print `NO`.

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
