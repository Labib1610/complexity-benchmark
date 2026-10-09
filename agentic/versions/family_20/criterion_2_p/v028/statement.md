# Problem B — Freight Logistics on a Divided Terminal

Time limit: 2 s   Memory limit: 256 MB

## Description
A shipping manifest outlines a set of bulk transfers between a fleet of cargo vessels and a row of unloading docks. Each transfer operation involves exactly one vessel and exactly one dock, and transfers never occur directly between two vessels or between two docks — the operation strictly moves goods across the vessel-dock divide. Different vessels and docks are involved in different numbers of transfers. The single busiest entity (whether that is a heavily-loaded vessel or a highly-demanded dock) dictates the scale of the entire operation.

The schedule is divided into numbered days 1, 2, 3, …, and completing a transfer consumes one full day. The absolute physical restriction is that no vessel can participate in more than one transfer on the same day, and no dock can process more than one transfer on the same day. Cargo types, vessel capacities, and dock sizes are irrelevant; the only constraint is preventing overlapping schedules for any single vessel or dock.

Because the busiest entity participates in some maximum number of transfers and none of its transfers can occur on the same day, the operation must span at least that many days. The logistical goal is to complete all transfers using **no more** days than this unavoidable minimum — exactly the busiest-entity count. Assign every transfer a day drawn from this minimum span such that no vessel and no dock is double-booked. (The strict separation between vessels and docks guarantees this minimum duration is always mathematically achievable; despite complex overlapping requirements, no extra days are ever required.)

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
