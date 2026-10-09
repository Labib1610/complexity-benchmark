# Problem A — Sequential Memory Allocation

Time limit: 5 s
Memory limit: 256 MB

## Description
A database system is allocating storage for $n$ data blocks, numbered $1$ to $n$. These blocks must be placed into $n$ contiguous memory sectors, also numbered from $1$ to $n$. Each block must be assigned exactly one unique sector, establishing a one-to-one mapping between the $n$ blocks and the $n$ sectors.

Certain pairs of blocks are frequently accessed together. Whenever two such interacting blocks are accessed, the hardware incurs a latency penalty equal to the physical distance between them in memory. Because the memory sectors are perfectly contiguous, the distance between a block in sector $x$ and a block in sector $y$ is simply the absolute difference $|x - y|$. 

The total access latency of the system is the sum of these absolute differences over all interacting pairs. Procurement has specified a strict overall latency budget, $B$. 

Because every block must be mapped to exactly one sector, the set of assigned sectors is always exactly the sequence $1, 2, \dots, n$. This strict conservation of assigned values means the system's average sector position is securely anchored at $(n+1)/2$, and the maximum possible distance between any two blocks is strictly bounded. Such strong algebraic invariants, along with the uniform weight of all interactions, give the configuration space a highly regular geometry. One might initially assume that this uniform structure allows an optimal configuration to be found easily by sorting the blocks by their interaction frequencies and placing the most active blocks near the median sector. 

Regardless of the strategy used, your definitive task is to determine whether there exists any valid allocation of the $n$ blocks to the $n$ sectors such that the total access latency over all interacting pairs does not exceed $B$. If such an allocation exists, you must provide one.

## Input
The first line contains three integers $n$, $m$, and $B$, representing the number of data blocks, the number of interacting pairs, and the total latency budget, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that block $u$ and block $v$ interact. No pair is listed more than once.

## Output
If there is an allocation that satisfies the budget, print `YES` on the first line. On the second line, print $n$ integers separated by spaces, where the $i$-th integer represents the sector number (from $1$ to $n$) assigned to block $i$. This sequence of $n$ integers must be a permutation of $1, 2, \dots, n$.
If no such allocation exists, print `NO`.

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
