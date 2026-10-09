# Fluidic Routing in Dual-Chamber Bioreactors

Time limit: 2 s   Memory limit: 256 MB

## Description
A modern bioreactor facility operates two distinct banks of equipment: a set of nutrient reservoirs and a set of filtration modules. The facility relies on a network of flexible micro-tubes. Each micro-tube establishes a direct flow path between exactly one nutrient reservoir and exactly one filtration module. Micro-tubes never connect two reservoirs together, nor do they connect two filtration modules together.

To prevent cross-contamination, the micro-tubes must undergo periodic sterilization. Sterilization is performed in distinct, numbered phases $1, 2, 3, \dots$ Sterilizing a micro-tube occupies it for an entire phase. The critical safety protocol dictates that if multiple micro-tubes are attached to the same nutrient reservoir or the same filtration module, they must be sterilized in completely different phases. Simultaneous sterilization at a shared endpoint would cause a catastrophic pressure failure.

The facility's "bottleneck rating" is defined as the maximum number of micro-tubes attached to any single piece of equipment (whether a reservoir or a module). Because all micro-tubes at the bottleneck must be sterilized in different phases, the facility requires at least that many phases. Your task is to schedule the sterilization phases for all micro-tubes such that the total number of phases used is **no more** than this unavoidable minimum — exactly the bottleneck rating. Assign every micro-tube a phase drawn from that many phases so that no piece of equipment ever has two of its micro-tubes scheduled in the same phase. (Due to the two-bank architecture, such a schedule is mathematically guaranteed to always exist without needing any phases beyond the bottleneck rating).

The bioreactor's piping network is certified under two operational guarantees:
- **Flow Conservation Guarantee**: The sum total of micro-tube endpoints connected to nutrient reservoirs, combined with the total number of micro-tube endpoints connected to filtration modules, will exactly equal double the total inventory of micro-tubes.
- **Peak Load Guarantee**: The bottleneck rating of the facility will never exceed the total inventory of micro-tubes.

## Input
The first line contains three integers $R$, $F$, and $T$ ($1 \le R, F \le 100000$, $0 \le T \le 400000$), representing the number of nutrient reservoirs, the number of filtration modules, and the total number of micro-tubes, respectively.
The next $T$ lines each contain two integers $u$ and $v$ ($1 \le u \le R$, $1 \le v \le F$), indicating a micro-tube connecting nutrient reservoir $u$ and filtration module $v$.

## Output
Print `YES`, then a line with $T$ integers in $1 \dots \Delta$ (where $\Delta$ is the bottleneck rating) — the phase assigned to micro-tube $i$ in input order. Micro-tubes meeting at any shared reservoir or filtration module must be assigned different phases.

## Example

### Input
```text
3 3 4
1 1
1 2
2 2
3 3
```

### Output
```text
YES
1 2 1 1
```
