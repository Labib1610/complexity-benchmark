# Problem A — Memory Page Compaction

Time limit: 5 s   Memory limit: 256 MB

## Description
You are optimizing a memory controller that consolidates fragmented memory pages into larger blocks. There are exactly $3q$ active pages, numbered sequentially from $1$ to $3q$. The hardware requires that pages be consolidated in groups of exactly three.

The operating system has already performed an alignment check and generated a list of $t$ compatible triplets. Each compatible triplet consists of three pages $a, b,$ and $c$ (where $a < b < c$). 

To achieve full defragmentation, you must select exactly $q$ triplets from this list such that every page from $1$ to $3q$ is included in exactly one selected triplet. No page may be left out, and no page may be included in more than one consolidated block.

Because the pages are sequentially numbered and every compatible triplet is strictly ordered ($a < b < c$), the problem possesses a natural forward-directed structure. You can think of this as processing the active pages in ascending order: each unassigned page must eventually act as the lowest index of some triplet, pulling in two higher-indexed pages to complete the block. The high number of compatible triplets (up to 20,000) provides significant redundancy, meaning that local forward-branching choices often smoothly extend to a global defragmentation.

Your task is to determine if there is a valid selection of $q$ triplets that perfectly covers all $3q$ pages without overlaps, and if so, output those triplets.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$).
Each of the next $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$) representing a compatible triplet.

## Output
If a valid selection exists, print `YES` on the first line, then $q$ lines each containing the three pages of one selected triplet. 
If no valid selection exists, print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
