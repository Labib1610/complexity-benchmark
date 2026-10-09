# Synthesis Phase Sequencing

Time limit: 5 s
Memory limit: 256 MB

## Description
A chemical facility must execute a synthesis procedure consisting of $n$ distinct operations. The facility has a single reactor bay, meaning the operations must be scheduled into exactly $n$ consecutive time slots. Every operation must be assigned to its own unique time slot, with no time slots left empty.

The procedure relies on $m$ specialized catalysts. Each catalyst is associated with exactly two specific operations. When a catalyst is utilized, it remains active in the reactor from the time slot of the earlier operation until the time slot of the later operation. The environmental exposure for a single catalyst is calculated as the absolute difference between the time slot numbers of its two associated operations.

Every unit of environmental exposure generates one unit of thermal waste. The total thermal waste produced by the whole procedure is the sum of the exposures of all $m$ catalysts. The reactor's cooling system is stocked with exactly $B$ single-use heat sinks. Each unit of thermal waste permanently consumes one heat sink. A schedule is only physically viable if it does not require more heat sinks than the cooling system possesses.

You must determine if there is a way to assign the $n$ operations to the $n$ time slots such that the procedure can safely run to completion. If such a schedule exists, you must provide it.

## Input
The first line provides three integers: the number of operations $n$, the number of catalysts $m$, and the initial number of heat sinks $B$.
The next $m$ lines each contain two integers $u$ and $v$ (where $1 \le u, v \le n$), indicating that operation $u$ and operation $v$ require the same catalyst. Operations are numbered from 1 to $n$.

## Output
If a viable schedule can be formed, print `YES` on the first line. On the second line, output $n$ space-separated integers, where the $i$-th integer represents the time slot (from 1 to $n$, forming a permutation) assigned to operation $i$.
If no schedule can operate within the available heat sinks, print `NO`.

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
