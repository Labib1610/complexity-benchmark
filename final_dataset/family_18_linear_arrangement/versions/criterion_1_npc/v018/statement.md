# Problem A — Backbone Trenching for the Control Vault

Time limit: 5 s
Memory limit: 256 MB

## Description
A facility upgrade involves $n$ control modules and $m$ dedicated signal harnesses. Each harness must physically connect a specific pair of modules. 

The physical installation site is a single straight trench divided into exactly $n$ consecutive mounting bays, numbered 1 through $n$. The installation process must assign exactly one module to each bay, such that every module occupies a unique bay.

When a harness connects two modules, it is laid in a continuous cable tray running parallel to the trench. The physical length of the harness is strictly determined by the separation of the bays housing the two modules: a harness connecting a bay at position $P$ and a bay at position $Q$ consumes exactly $|P - Q|$ units of cable. The specific routing hardware and signal directions do not affect this calculation.

The procurement department has authorised a maximum total cable allowance of $B$ units for the entire installation. This allowance applies to the grand total of the lengths of all $m$ required harnesses. There is no per-harness limit, only a strict constraint on the overall sum.

Your task is to determine if there exists a valid assignment of modules to mounting bays such that the combined length of all harnesses does not exceed the authorised allowance. If such an assignment is possible, output the bay position for each module. Otherwise, report that the installation cannot be completed within the budget.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that a signal harness must connect module $u$ and module $v$.

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ integers representing the bay positions (from 1 to $n$) assigned to modules 1, 2, ..., $n$ respectively. If no such assignment exists, print `NO`.

## Example

**Input:**
```
4 3 4
1 2
1 3
1 4
```

**Output:**
```
YES
2 1 3 4
```
