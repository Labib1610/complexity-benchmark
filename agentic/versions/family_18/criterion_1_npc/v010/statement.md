# Problem A — Backbone Trenching for the Control Vault

Time limit: 5 s
Memory limit: 256 MB

## Description
A new control vault requires $n$ modules to be installed along a single straight equipment trench. The trench is divided into $n$ consecutive mounting bays, numbered 1 through $n$ from one end to the other. Each module must be assigned to exactly one bay, and every bay must hold exactly one module.

The modules exchange signals over $m$ point-to-point harnesses. Whenever two modules communicate, a single harness is run between their respective bays through the trench's cable tray. Because the tray runs straight along the trench, the physical length of a harness is determined solely by how many bays separate the two modules it connects. For example, modules in adjacent bays require one unit of harness, modules separated by one intermediate bay require two units, and so on. The length of a harness is simply the absolute difference between the bay numbers of the two modules it connects.

Procurement has fixed a maximum budget of $B$ total units of harness for the entire job. You must calculate the sum of the lengths of all $m$ required harnesses. The combined length must not exceed $B$. There is no per-harness limit; only the grand total matters.

Determine whether the modules can be assigned to the bays so that the combined harness length stays within the budget. If so, provide a valid assignment; otherwise, report that it cannot be done. (An assignment that minimizes the length for some harnesses may overshoot the total budget because of others, so local good choices do not guarantee a feasible total.)

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that a harness must be run between module $u$ and module $v$.

## Output
If the modules can be installed such that the combined harness length is at most $B$, print `YES`. On the next line, print $n$ space-separated integers. The $i$-th integer must be the bay number (from 1 to $n$) assigned to module $i$. Every bay from 1 to $n$ must receive exactly one module.
If no such installation fits the budget, print `NO`.

## Examples

### Example 1
**Input:**
```
4 4 6
1 2
2 3
3 4
1 4
```

**Output:**
```
YES
1 2 3 4
```

### Example 2
**Input:**
```
4 4 5
1 2
2 3
3 4
1 4
```

**Output:**
```
NO
```
