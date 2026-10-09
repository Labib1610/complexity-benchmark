# Problem A — Phase Alignment in Sparse Networks

Time limit: 2 s   Memory limit: 256 MB

## Description

A decentralized communication network consists of **n** independent data channels. To prevent interference, each channel must be configured with a phase shift, chosen from exactly two available modes: `1` (advanced) or `0` (delayed).

The network's stability is maintained by **m** local monitoring units. The architecture is highly sparse: each unit monitors a tiny localized footprint of exactly three channel connections. A connection is specified by a non-zero integer where the absolute value identifies the channel. The sign of the integer dictates the expected phase for that connection: a positive integer expects mode `1`, while a negative integer expects mode `0`.

Because the monitors are designed with broad fault tolerance, a unit will operate seamlessly as long as its local footprint is not entirely mismatched. Specifically, a monitor only fails if every single one of its three connections receives the opposite of its expected phase. If even a single connection receives its expected phase, the monitor remains completely stable. 

Given the localized nature of the monitors, most channels do not interact within any given unit. You must determine if there exists a global phase configuration for the **n** channels such that no monitor fails, and if so, provide one such configuration.

## Input
The first line provides two integers **n** and **m** (1 ≤ n ≤ 90, 0 ≤ m ≤ 400), representing the number of channels and the number of monitoring units, respectively.
The following **m** lines each contain three non-zero integers **c1 c2 c3** (|ci| ≤ n), detailing the footprint of one monitoring unit. For a unit to remain stable, at least one of its three connections must receive its expected phase.

## Output
If the network cannot be fully stabilized, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output **n** space-separated integers **p1 p2 … pn** (each either `0` or `1`), representing the phase shift for each channel. Any fully stable configuration is perfectly acceptable.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```

## Note
Each monitoring unit always lists exactly three connections. The same channel may be connected multiple times to the same unit.
