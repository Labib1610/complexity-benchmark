# Memory Reconstruction

Time limit: 2 s
Memory limit: 256 MB

## Description
An artificial consciousness has been fragmented into $n$ memory blocks, numbered 1 to $n$. To restore the consciousness, these blocks must be reassembled into a single continuous linear sequence.

During the recovery process, $m$ synaptic links were extracted. Each synaptic link connects two memory blocks, indicating a direct temporal progression: the thought process from block $a$ strictly preceded the thought process in block $b$. Therefore, in the final reconstructed sequence, block $a$ must be placed at some position before block $b$.

The extraction tool provides the following structural guarantees about the recovered data:
1. **Global Balance:** If you calculate the total number of outgoing links across all memory blocks, and the total number of incoming links across all memory blocks, these two totals are guaranteed to be perfectly balanced. Both totals will always exactly equal $m$.
2. **Capacity Bound:** The number of memory blocks that act as the destination for strictly more than $m$ synaptic links is guaranteed to be exactly zero.

Your task is to find a complete linear sequence of all $n$ memory blocks that satisfies every extracted synaptic link. If the synaptic links form a logical paradox (for example, implying a block must temporally precede itself due to a chain of links), the reconstruction is impossible. 

## Input
First line: two integers $n$ and $m$. 
Each of the next $m$ lines: two integers $a$ and $b$ — meaning memory block $a$ must appear before memory block $b$ in the sequence.

## Output
Print `YES` then a permutation of the integers 1 to $n$ (representing a valid sequence of the memory blocks). If there are multiple valid sequences, any one is acceptable. If no valid sequence exists due to a paradox, print `NO`.

## Example
**Input:**
4 4
1 2
2 3
1 3
4 1

**Output:**
YES
4 1 2 3
