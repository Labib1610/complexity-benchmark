# Problem A — Backbone Trenching for the Control Vault

Time limit: 5 s   Memory limit: 256 MB

## Description
The automated facility design pipeline consists of three stages. First, the schematic generator defines the required signal connections between a set of control modules. Second, the layout stage determines the physical placement of these modules. Finally, the installation team uses this layout to cut and route the physical wiring. Your task is to implement the second stage: the layout planner.

In this layout stage, the modules must be installed along a single straight equipment trench. The trench is divided into a fixed number of consecutive mounting bays, exactly one module per bay, and every module ends up in some bay; there are precisely as many bays as modules, so the installation is a one-to-one placement of modules onto bay positions numbered along the trench.

The modules exchange signals over point-to-point harnesses based on the schematic from the first stage. Whenever two modules must exchange signals, a harness is run between their bays through the trench's cable tray. Because the tray runs the length of the trench, the physical length of a harness is determined solely by how many bay positions separate the two modules it connects — adjacent bays cost one unit of harness, bays two apart cost two units, and so on. The specific routing hardware, connector types, and signal directions are immaterial to this calculation; only the separation in bays matters.

Before passing the layout to the third stage, you must verify it meets procurement constraints. Procurement has fixed a **total** harness budget for the job: summed over every required signal harness, the combined harness length must not exceed the given budget. There is no per-harness limit and no limit on how many harnesses share the tray — the only constraint that binds is the grand total.

Decide whether the layout stage can place the modules one-per-bay so that the total harness length over all required connections stays within the budget, and if so output a placement for the installation team; otherwise report that no placement fits the budget. (A placement that is excellent for some connections may overshoot the total because of others, so local good choices do not guarantee a feasible total.)

## Input
First line: three integers n, m, B. Each of the next m lines: two integers u v — a required signal connection from the schematic.

## Output
Print `YES` then a line with n integers — the position (1..n, a permutation) of module 1,2,...,n — such that the total stretch is <= B. Otherwise print `NO`.

## Example

### Input
```text
4 3 4
1 2
2 3
3 4
```

### Output
```text
YES
1 2 3 4
```
