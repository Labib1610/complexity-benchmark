# Concurrent Maintenance Selection

Time limit: 2 s   Memory limit: 256 MB

## Description

A cloud infrastructure contains **n** microservices (numbered 1 to **n**). Certain pairs of microservices share a mutable data volume and will cause data corruption if they execute their maintenance routines concurrently. 

The system architecture enforces a strict two-tier design: the microservices can be partitioned into two distinct tiers (which are not explicitly provided in the input) such that every shared volume is accessed by exactly one microservice from the first tier and one from the second tier. Microservices within the same tier never share a volume.

You must determine if it is possible to select exactly **k** microservices to run their maintenance routines concurrently without any risk of data corruption, and if so, identify them.

## Input

The first line provides three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
The next **m** lines each contain two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), indicating that microservices **u** and **v** share a data volume. No pair is listed more than once. The input is guaranteed to adhere to the two-tier architecture described above.

## Output

If a safe selection of **k** microservices exists, output `YES` on the first line. On the second line, output **k** distinct integers representing the IDs of the chosen microservices, separated by spaces. If multiple valid selections exist, any is acceptable.

If no such selection can be made, output `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
5 0 5
```

**Output**
```
YES
1 2 3 4 5
```

### Example 3

**Input**
```
4 4 3
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```
