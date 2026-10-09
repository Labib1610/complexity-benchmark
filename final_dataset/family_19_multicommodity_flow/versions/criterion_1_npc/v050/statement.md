# Problem A — Distribution System Allocation

Time limit: 5 s
Memory limit: 256 MB

## Description
A distribution system operates `n` checkpoints connected by `m` one-way conduits. To maintain stability, the system operates in discrete cycles. Each conduit can process a strict maximum of `cap` total units per cycle.

Currently, the system must fulfill `k` separate delivery mandates. Mandate `i` dictates that exactly `d_i` units belonging to that mandate must travel from starting checkpoint `s_i` to ending checkpoint `t_i`.

All units are physically identical and share the conduits. A conduit's limit restricts the combined number of units from all mandates passing through it. However, units for different mandates are tracked separately and must reach their specified ending checkpoints.

The movement of units for any single mandate must adhere to the following conditions:
- At any checkpoint that is neither the starting nor ending point for that mandate, the amount of arriving units must perfectly match the amount of departing units.
- At the starting checkpoint for a mandate, the number of departing units minus the number of arriving units must equal exactly `d_i`.
- At the ending checkpoint for a mandate, the number of arriving units minus the number of departing units must equal exactly `d_i`.
- Units cannot be divided; the amount of units assigned to any mandate on any conduit must be a non-negative integer.

Your task is to determine if all `k` mandates can be fulfilled in a single cycle without exceeding the limit of any conduit. If a valid allocation exists, you must provide the exact number of units assigned to each mandate on each conduit.

## Input
The first line contains three integers: `n`, `m`, and `k`.
The next `k` lines each contain three integers `s_i`, `t_i`, and `d_i`, representing the starting checkpoint, ending checkpoint, and the required number of units for mandate `i`.
The next `m` lines each contain three integers `u`, `v`, and `cap`, representing a one-way conduit from checkpoint `u` to checkpoint `v` with a maximum limit of `cap` units per cycle.

## Output
If the allocation is possible, print `YES` on the first line. Then, print `k` lines. The `i`-th of these lines should contain `m` space-separated integers, representing the number of units of mandate `i` assigned to each of the `m` conduits (in the exact order the conduits were given in the input).
If it is impossible to fulfill all mandates together, print `NO`.

## Example

**Input:**
```
4 5 2
1 4 1
2 3 1
1 2 1
1 3 1
2 4 1
3 4 1
2 3 1
```

**Output:**
```
YES
1 0 1 0 0
0 0 0 0 1
```
