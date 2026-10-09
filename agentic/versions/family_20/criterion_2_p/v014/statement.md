# Problem B — Cargo Phases at a Logistics Hub

Time limit: 2 s   Memory limit: 256 MB

## Description
A logistics hub transfers cargo between a row of inbound arrival bays and a row of outbound departure bays. Every documented cargo transfer moves items from exactly one arrival bay to exactly one departure bay. Transfers never happen between two bays of the same type—the facility is strictly segregated. 

Different bays handle different total counts of transfers. The busiest bay across the entire hub (whether arrival or departure) dictates the duration of the daily operation cycle. 

Each transfer must be assigned to a specific dispatch phase, numbered 1, 2, 3, and so on. A phase handles one transfer at a time per bay. The strict operational constraint is that no bay can participate in more than one transfer during the same phase, because a bay's dock cannot be occupied by two vehicles simultaneously. Cargo weights, priority classes, and bay locations are all irrelevant; only which transfers share a bay matters.

Since the busiest bay handles some maximum number of transfers—let's call this peak volume $V$—the hub must operate for at least $V$ phases, as none of its transfers can share a phase. The facility manager requires a schedule that uses **no more** phases than this unavoidable minimum. You must assign every transfer a phase from 1 to $V$ such that the single-bay constraint is never violated. (Because transfers only go between arrival and departure bays, it is always possible to fit the schedule exactly into $V$ phases without needing any extras.)

## Input
First line: three integers $A$, $D$, and $T$. The facility's architectural blueprint provides a maximum capacity of 100,000 arrival bays and 100,000 departure bays, meaning $A$ and $D$ will never exceed these totals, though there is always at least one operational bay of each type. The automated sorting system has a hard daily limit of 400,000 transfers, meaning $T$ cannot exceed this number, though a completely idle day with zero transfers is possible.
Next $T$ lines: two integers $u$ and $v$ (with $u$ from 1 to $A$ inclusive, and $v$ from 1 to $D$ inclusive), indicating a transfer from arrival bay $u$ to departure bay $v$.

## Output
Print `YES` on the first line.
On the second line, print $T$ integers, each between 1 and $V$, representing the phase assigned to each transfer in the order they appeared in the input. If multiple transfers share any bay, their assigned phases must differ.

## Example
**Input:**
```
3 3 4
1 1
1 2
2 1
3 3
```

**Output:**
```
YES
1 2 2 1
```
