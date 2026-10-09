# Pipeline Configuration

Time limit: 1 s   Memory limit: 256 MB

## Description

A batch of **j** digital assets must be processed through an automated pipeline. Every asset requires a specific duration in the extraction phase, followed by a specific duration in the encoding phase. 

To configure the system, you must assign an ordering to the assets. The pipeline operates strictly under these mechanics:
- Starting at time 0, the extraction server processes the assets continuously, one by one, following your chosen ordering.
- The encoding server also processes the assets one by one, using that exact same ordering.
- The encoding server begins processing an asset at the earliest possible moment: as soon as the asset has finished extraction AND the encoding server has completed all prior assets in the sequence.

There are $j!$ valid ways to arrange the sequence of assets. Since any permutation is a valid configuration, your objective is to evaluate the arrangement space and determine the minimum possible global completion time—the exact moment when the final asset in your ordering finishes its encoding phase.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the extraction duration and the encoding duration for that asset.

## Output

Print a single integer: the earliest possible time at which all assets can be completely finished.

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

In Example 2, the single asset takes 5 for extraction and then 3 for encoding, finishing at time 8.
