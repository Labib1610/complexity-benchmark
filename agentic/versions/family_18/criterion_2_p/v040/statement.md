# Problem B — Linear Slot Assignment for Integrated Logic

Time limit: 5 s
Memory limit: 256 MB

## Description
The schematic capture tool has completed the first phase of processing an integrated design. It has identified $n$ logic blocks and $m$ bidirectional signal wires connecting them. The schematic is minimally continuous: there are exactly $m = n-1$ wires, and every block can exchange signals with every other block through a sequence of these wires.

As the physical layout synthesizer, your task is the second phase. You must map these $n$ logic blocks onto a single linear rail of mounting slots. There are exactly $n$ slots, numbered $1$ through $n$, and each block must be assigned to exactly one unique slot.

When a wire connects a block assigned to slot $x$ and a block assigned to slot $y$, the length of the wire is exactly $|x - y|$. The total copper usage of the layout is the sum of the lengths of all $m$ wires. You are given a maximum copper allowance $B$.

You must determine a slot assignment that keeps the total copper usage less than or equal to $B$, or report that no such assignment exists.

If you successfully find an assignment, the design will pass to the third phase, where the fabrication scheduler will assign non-interfering depth channels to overlapping wires. You do not need to compute depth channels; your only responsibility is finding a valid slot assignment that satisfies the copper allowance.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating a wire between block $u$ and block $v$.
(It is guaranteed that $m = n - 1$, and all blocks are linked into a single contiguous system.)

## Output
If the layout cannot be achieved within the allowance, print `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers. The $i$-th integer must be the slot position ($1$ to $n$, forming a permutation) assigned to logic block $i$.

## Example
### Input
```
5 4 5
1 2
1 3
3 4
3 5
```

### Output
```
YES
4 5 2 1 3
```
