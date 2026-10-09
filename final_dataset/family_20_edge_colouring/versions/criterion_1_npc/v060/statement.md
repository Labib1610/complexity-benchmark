# Problem A — Synchronization Phases in Decentralized Ledgers

Time limit: 5 s   Memory limit: 256 MB

## Description
A decentralized financial system operates across multiple data centers. The architecture of this system is strictly regulated: each data center maintains direct fiber links to exactly three other data centers.

To keep the ledger consistent without causing network congestion or I/O bottlenecks, the daily synchronization process is divided into three distinct transmission phases, designated as phase 1, phase 2, and phase 3. Every fiber link must be scheduled to operate in exactly one of these three phases. 

The hardware at each location can only handle one active synchronization at a time. Consequently, to prevent data collisions, the three fiber links connected to any single data center must always be assigned to three completely different phases. The physical distance between facilities and the overall layout do not alter this requirement; the only rule is that no data center can have two of its links active during the same phase.

Your task is to analyze the network's layout and assign a transmission phase (1, 2, or 3) to each fiber link so that the non-overlapping phase requirement is met everywhere. If the network's configuration makes it impossible to schedule the phases under these rules, you must report that the layout is invalid.

## Input
The first line contains two integers **n** and **m** (**n** is even, **m** = 3**n**/2, 2 ≤ **n** ≤ 2000), representing the number of data centers and the number of fiber links, respectively. Data centers are numbered from 1 to **n**.
Each of the following **m** lines contains two integers **u** and **v** (1 ≤ **u** < **v** ≤ **n**), indicating that a fiber link connects data center **u** and data center **v**.

## Output
If a valid phase schedule is possible, output `YES` on the first line. On the second line, output **m** integers in {1, 2, 3} — the phase chosen for link *i* in input order (links sharing a data center must differ). Otherwise, output `NO`.

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
