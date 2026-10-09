# Problem B — Protocol Decontamination

Time limit: 1 s   Memory limit: 256 MB

## Description

A research facility must decontaminate **j** field researchers through a strict two-step protocol. Every researcher must first complete a chemical wash, followed by a thermal bake. The facility has exactly one wash cabin and one bake cabin.

The process is governed by the following safety protocols:
- The wash cabin and the bake cabin can each hold at most one researcher at any given time.
- A researcher can only begin their thermal bake after their chemical wash is entirely complete.
- The researchers must form a single, strict queue. They enter the wash cabin in this queue's order, and they must enter the bake cabin in that exact same order.

You are provided with the required wash duration and bake duration for each researcher. You must determine the optimal queue order to minimize the total time required for all researchers to complete the entire decontamination protocol.

Determine the earliest possible time that the final researcher can finish their thermal bake.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the chemical wash duration and the thermal bake duration of a researcher.

## Output

Print a single integer: the minimum possible time at which all researchers have completed both steps of the decontamination protocol.

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

In Example 2 the single researcher takes 5 for the chemical wash then 3 for the thermal bake, finishing at time 8.
