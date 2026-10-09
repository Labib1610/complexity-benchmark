# Problem B — Cluster Memory Allocation

Time limit: 2 s   Memory limit: 256 MB

## Description
A high-performance computing cluster contains $q$ processors (assigned identifiers $1$ through $q$) and $q$ memory banks (assigned identifiers $q+1$ through $2q$). 

Due to motherboard layout restrictions, direct data buses can only be routed between certain processor-memory pairs. The hardware specification provides a list of $t$ possible data buses. Each possible bus links one processor to one memory bank.

The cluster's hypervisor must activate a subset of these data buses to initialize the system. To ensure optimal load balancing, every processor must be assigned exactly one active data bus. To prevent memory bottlenecks, every memory bank must also be assigned exactly one active data bus. 

You are guaranteed the following properties about the hardware specification:
- For every possible data bus connecting a processor $a$ and a memory bank $b$, the sum of their identifiers satisfies $3 \le a + b \le 3q$.
- The total number of possible data buses connected across all processors is exactly equal to the total number of possible data buses connected across all memory banks.

Determine if a valid bus activation configuration exists using only the possible buses from the specification. If it is possible, output the buses to activate. If no such configuration exists, report that the cluster cannot be initialized.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of processors/memory banks and the number of possible data buses.
Each of the subsequent $t$ lines contains two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a possible data bus between processor $a$ and memory bank $b$.

## Output
If a valid activation configuration is possible, print `YES` on the first line. Then, print $q$ lines, each containing the two integers of an activated data bus. If multiple valid configurations exist, you may output any of them.
If no valid configuration is possible, print `NO`.

## Example 1

### Input
```text
3 4
1 4
2 5
3 6
1 5
```

### Output
```text
YES
1 4
2 5
3 6
```

## Example 2

### Input
```text
3 2
1 4
2 5
```

### Output
```text
NO
```
