# Problem B — Orbital Telemetry Synchronization

Time limit: 2 s   Memory limit: 256 MB

## Description
A space agency must download data from an orbital constellation. The infrastructure is divided into two distinct groups: $N_S$ orbiting satellites and $N_G$ terrestrial ground stations. The daily operations log lists multiple required data transfers. Each transfer establishes a dedicated radio link between one satellite and one ground station. Transfers are never made satellite-to-satellite or station-to-station.

Transfers occur during discrete, numbered time windows. Any number of transfers can happen concurrently in the same time window. However, because each asset has only one primary transceiver, a satellite cannot participate in more than one transfer per time window. By the same rule, a ground station can lock onto at most one satellite during any single time window.

The absolute minimum time needed to complete all operations depends on the single busiest asset. If we define $D$ as the highest number of transfers required by any one satellite or any one ground station, then that specific asset will be busy for $D$ different time windows. Consequently, finishing the entire daily log requires at least $D$ time windows.

You must design a schedule that finishes all transfers in exactly $D$ time windows. You will assign every transfer to a time window labeled from $1$ to $D$ such that no two transfers sharing a satellite or a ground station are assigned the same window. Because the network strictly connects satellites only to ground stations, a conflict-free schedule using exactly $D$ windows is always guaranteed to exist.

## Input
The first line contains three integers $N_S$, $N_G$, and $M$ ($1 \le N_S, N_G \le 100000$, $0 \le M \le 400000$).
The following $M$ lines each provide two integers $u$ and $v$ ($1 \le u \le N_S$, $1 \le v \le N_G$), representing a required transfer between satellite $u$ and ground station $v$.

## Output
Print `YES` on the first line. On the second line, print $M$ integers in the range $1 \dots D$. The $i$-th integer gives the time window assigned to the $i$-th transfer from the input. Any transfers that involve the same satellite or the same ground station must receive different time windows.

### Example

**Input**
```text
3 4 5
1 2
1 3
2 3
3 1
3 4
```

**Output**
```text
YES
1 2 1 1 2
```
