# Problem B — Pallet Routing Quota

Time limit: 2 s
Memory limit: 256 MB

## Description
A logistics company must route a specific daily quota of identical pallets from a central warehouse to a retail center through a network of transfer yards. The yards are connected by one-way transport corridors.

Each corridor has a strict daily limit on the number of pallets it can handle, dictated by the available vehicle fleet. Because the intermediate transfer yards lack overnight storage facilities and do not produce goods, the total number of pallets arriving at any intermediate yard must exactly equal the total number departing. The net number of pallets departing the central warehouse (total departures minus total arrivals) must exactly equal the required daily quota, and the net number arriving at the retail center (total arrivals minus total departures) must equal this same quota. Pallets cannot be split; all assignments must be non-negative whole numbers.

You must determine how many pallets to send down each corridor to meet the daily quota without exceeding any corridor's limit. If it is impossible to route the full quota under these restrictions, you must report this.

## Input
The first line contains three integers: `n` (the number of yards), `m` (the number of corridors), and `1` (indicating a single pallet type).
The second line contains three integers: `s` (the central warehouse yard ID), `t` (the retail center yard ID), and `d` (the daily quota).
The next `m` lines each contain three integers `u`, `v`, and `cap`, indicating that a one-way corridor runs from yard `u` to yard `v` with a daily limit of `cap` pallets.

## Output
If the quota can be met, print `YES` on the first line. On the second line, print `m` integers representing the number of pallets assigned to each corridor, in the exact order the corridors were listed in the input.
If the quota cannot be met, print `NO`.

## Example

### Input
```
4 5 1
1 4 10
1 2 10
1 3 10
2 3 5
2 4 5
3 4 5
```

### Output
```
YES
5 5 0 5 5
```
