# Problem A — Control Vault Sequential Layout

Time limit: 5 s
Memory limit: 256 MB

## Description
A new control vault is being commissioned, and its $n$ modules must be installed into a single, perfectly straight linear chassis. The chassis features exactly $n$ uniform slots arranged continuously in a single dimension. The installation process is highly regular: each module is assigned to exactly one slot, filling the chassis sequentially from end to end.

During operation, specific pairs of modules must exchange signals. To facilitate this, direct point-to-point wiring is run between them. Because the chassis is strictly one-dimensional and uniform, the physical length of any wire is simply the absolute difference between the slot indices of the two modules it connects. For example, if two communicating modules are placed in slot 3 and slot 7, their wire requires exactly 4 units of length. The routing hardware and signal directions are immaterial; only the absolute separation in slots matters.

Procurement has provided a fixed overall wiring budget of $B$ units. The one-dimensional design simplifies routing, as there are no restrictions on how wires overlap or share the conduit. The only requirement is that the combined length of all individual wires does not exceed $B$.

Given the straightforward nature of the linear chassis, your task is to determine if there is a sequential assignment of modules to slots that satisfies all required communications using at most $B$ total units of wire. If a valid direct mapping exists, output it; otherwise, report that the budget is too strict.

## Input
The first line contains three integers $n$, $m$, and $B$, representing the number of modules, the number of required communications, and the total wiring budget.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that a wire must be run between module $u$ and module $v$.

## Output
If the modules can be assigned to the slots within the budget, print `YES` on the first line. On the second line, print $n$ integers representing the assignment: the $i$-th integer gives the slot number (from 1 to $n$) where module $i$ is installed.
If no such assignment is possible, print `NO`.

## Example 1

### Input
```
3 2 2
1 2
1 3
```

### Output
```
YES
2 1 3
```
