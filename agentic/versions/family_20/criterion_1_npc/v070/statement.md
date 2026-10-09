# Problem A — Diagnostic Phase Assignment

Time limit: 5 s   Memory limit: 256 MB

## Description
In a newly deployed data center, the network engineering team must conduct latency diagnostics. The hardware units are connected by a series of bidirectional fiber links. The facility's physical architecture follows a strict redundancy rule: every hardware unit is equipped with exactly three network interface ports, and every single port is actively occupied by a link connecting it to another hardware unit. There are no unused ports, and no unit has any other connections.

The diagnostic protocol requires configuring each link to operate in one of three distinct states, designated 1, 2, and 3. To prevent signal cross-talk during the test, a hardware unit cannot process data from multiple links in the same state simultaneously. Consequently, the three links connected to any single hardware unit must each be configured to a different state, ensuring that all three states are perfectly distributed at every unit.

Your task is to process the wiring manifest and determine whether it is possible to assign a state to each link such that this non-interference condition is satisfied across the entire facility. If a valid configuration exists, you must provide it. If no such configuration can be achieved without causing cross-talk at some unit, you must report that it is impossible.

## Input
The first line contains two integers **n** and **m** (**n** even, **m** = 3**n**/2, 2 ≤ **n** ≤ 2000), representing the number of hardware units and the number of fiber links, respectively. Hardware units are numbered from 1 to **n**.
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ **u** < **v** ≤ **n**), specifying that a fiber link connects hardware unit **u** and hardware unit **v**.

## Output
If a valid state assignment exists, print `YES`, followed by a line with **m** integers in {1, 2, 3} — the state assigned to link *i* in input order. Otherwise, print `NO`.

## Example
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
YES
1 2 3 3 2 1
```
