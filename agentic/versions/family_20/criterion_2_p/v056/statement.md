# Problem B — Freight Logistics on a Divided Terminal

Time limit: 2 s   Memory limit: 256 MB

## Description
A logistics company is coordinating a series of bulk cargo transfers between a fleet of cargo vessels and a row of unloading docks. Each transfer operation connects exactly one vessel and exactly one dock. No transfers occur directly between two vessels or between two docks.

The schedule is divided into numbered days (1, 2, 3, ...). Each transfer takes one full day. To prevent logistical bottlenecks, no vessel can participate in more than one transfer on the same day, and no dock can process more than one transfer on the same day. 

Let the peak load $\Delta$ be the maximum number of transfers associated with any single vessel or dock. Because this busiest entity participates in $\Delta$ transfers and none of its transfers can occur on the same day, the operation must span at least $\Delta$ days. The logistical goal is to complete all transfers using exactly this unavoidable minimum number of days. Assign every transfer a day drawn from this minimum span such that no vessel and no dock is double-booked. (The strict separation between vessels and docks guarantees this minimum duration is always mathematically achievable; no extra days are ever required).

Furthermore, the port authority mandates two strict regulatory requirements for any valid schedule:
1. **Daily Capacity Limit**: The total number of simultaneous transfers scheduled on any single day cannot exceed the total number of vessels $n_V$, and cannot exceed the total number of docks $n_D$.
2. **Duration Cap**: The total number of days in the schedule ($\Delta$) must not exceed the total number of transfers $m$.

## Input
The first line contains three integers $n_V$, $n_D$, and $m$ ($1 \le n_V, n_D \le 100000$, $0 \le m \le 400000$), representing the number of vessels, the number of docks, and the total number of transfers.
The next $m$ lines each contain two integers $u$ and $v$ ($1 \le u \le n_V$, $1 \le v \le n_D$), indicating a transfer between vessel $u$ and dock $v$. 

## Output
Print `YES`, then on the next line print $m$ integers in the range $1 \dots \Delta$ (where $\Delta$ is the maximum number of transfers for any single vessel or dock). The $i$-th integer represents the scheduled day of the $i$-th transfer in input order. Two transfers sharing a vessel or a dock must be assigned different days. If there are multiple valid schedules, any one will be accepted.

## Example

### Input
```text
3 3 5
1 1
1 2
2 2
2 3
3 3
```

### Output
```text
YES
1 2 1 2 1
```
