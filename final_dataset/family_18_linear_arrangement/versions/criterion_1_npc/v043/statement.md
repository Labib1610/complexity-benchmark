# Problem A — Backbone Trenching for the Control Vault

Time limit: 5 s
Memory limit: 256 MB

## Description
A facility upgrade involves $n$ control modules and $m$ dedicated signal harnesses. Each harness must connect a specific pair of modules.

The installation site provides exactly $n$ mounting bays. These bays are arranged sequentially and numbered 1 through $n$ from one end of the sequence to the other. You must assign exactly one module to each bay, such that every module occupies a unique bay.

Once the modules are installed, the harnesses are routed. A harness connecting two modules must be laid by stepping from bay to adjacent bay directly along the sequence. Every time a harness transitions from one bay to an immediate neighbor, it consumes exactly one unit of cable. The cable cannot bypass any intermediate bays and must follow the sequence of bays between the two modules without detours.

The procurement department has authorised a maximum total cable allowance of $B$ units. This allowance applies to the grand total of the cable consumed by all $m$ required harnesses. There is no per-harness limit, only a strict constraint on the overall sum.

Your task is to determine if there exists a valid assignment of modules to bays such that the combined cable usage of all harnesses does not exceed the authorised allowance. If such an assignment is possible, output the bay number for each module. Otherwise, report that the installation cannot be completed within the budget.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that a signal harness must connect module $u$ and module $v$.

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ integers representing the bay numbers (from 1 to $n$) assigned to modules 1, 2, ..., $n$ respectively. If no such assignment exists, print `NO`.

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
