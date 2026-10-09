# Problem A — Backbone Trenching for the Control Vault

Time limit: 5 s   Memory limit: 256 MB

## Description
A new control vault is being commissioned, and its modules must be installed along a single straight equipment trench. The trench is divided into a fixed number of consecutive mounting bays, exactly one module per bay, and every module ends up in some bay; there are precisely as many bays as modules, so the installation is a one-to-one placement of modules onto bay positions numbered along the trench.

The modules exchange signals over point-to-point harnesses. Whenever two modules must exchange signals, a harness is run between their bays through the trench's cable tray. Because the tray runs the length of the trench, the physical length of a harness is determined solely by how many bay positions separate the two modules it connects — adjacent bays cost one unit of harness, bays two apart cost two units, and so on. The specific routing hardware, connector types, and signal directions are immaterial to this calculation; only the separation in bays matters. 

Because harness cost grows linearly with distance, it is generally advantageous to place heavily connected modules centrally and to group modules with shared peers near one another. Procurement has fixed a **total** harness budget for the job: summed over every required signal harness, the combined harness length must not exceed the given budget. There is no per-harness limit and no limit on how many harnesses share the tray — the only constraint that binds is the grand total.

Decide whether the modules can be placed one-per-bay so that the total harness length over all required connections stays within the budget, and if so output a placement; otherwise report that no placement fits the budget. (While clustering modules by their connection profiles might appear to yield an immediate optimal arrangement, a placement that is excellent for some connections may overshoot the total because of others, so local good choices do not guarantee a feasible total.)

## Input
First line: three integers $n$, $m$, and $B$. 
Each of the next $m$ lines: two integers $u$ and $v$ — indicating that a harness must connect module $u$ and module $v$.

## Output
Print `YES` then a line with $n$ integers — the position (from $1$ to $n$, forming a permutation) of module 1, 2, ..., $n$ — such that the total harness length is $\le B$. Otherwise print `NO`.

## Example
### Input
```text
4 3 4
1 4
4 2
2 3
```

### Output
```text
YES
1 3 4 2
```
