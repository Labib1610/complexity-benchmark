# Protocol: Synchronization Cascade

Time limit: 1 s   Memory limit: 256 MB

## Description

A planetary rover is transmitting **j** distinct high-resolution telemetry blocks back to Earth. The transmission pipeline consists of exactly two sequential bottlenecks:
1. The Deep Space Network (DSN) dish must physically download the block.
2. The Cryptographic Core must decrypt the block.

Because of hardware limitations, the DSN dish can only download one block at a time, and the Cryptographic Core can only decrypt one block at a time. Furthermore, a block's decryption cannot begin until its download is completely finished. 

To prevent buffer desynchronization, the protocol enforces a strict ordering rule: you must establish a single master sequence of the **j** blocks. The DSN dish will download the blocks in this exact sequence, and the Cryptographic Core will subsequently decrypt the blocks in this identically matched sequence. 

The DSN dish works continuously on the sequence of blocks with no gaps between downloads. Downloaded blocks wait in an intermediate buffer if the Core is still busy decrypting a previous block. The Cryptographic Core will begin a block's decryption as early as possible—either exactly when the block finishes downloading, or when the Core finishes decrypting the previous block in the sequence, whichever is later.

You must select one master sequence from the **j**! possible permutations. The search space grows factorially, meaning an exhaustive search will vastly exceed the time limit. You must carefully evaluate how the choice of sequence influences the cascading idle times and bottlenecks across the pipeline. Your objective is to determine the optimal sequence that yields the absolute minimum time required for the Cryptographic Core to finish processing all **j** blocks, and report that minimum completion time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **d** and **c** (1 ≤ d, c ≤ 1000000): the time required to download the block, and the time required to decrypt the block, respectively.

## Output

Print a single integer: the earliest possible time the entire batch of **j** blocks can be fully decrypted.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 2, the single block takes 5 time units to download and then 3 time units to decrypt, finishing at time 8.
