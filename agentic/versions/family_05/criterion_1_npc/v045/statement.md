# Problem A — Assembly Line Setup

Time limit: 5 s   Memory limit: 256 MB

## Description

A manufacturing plant is setting up its daily operations. The plant has three pools of assets: engineers, robotic arms, and maintenance windows. There are exactly **k** assets in each pool, and within a pool, each asset is assigned a unique ID from 1 to **k**.

To activate a production line, you must pair one engineer, one robotic arm, and one maintenance window. However, due to certification restrictions, only certain specific groupings of an engineer, an arm, and a window are authorized for use.

Your task is to activate exactly **k** production lines. To do this, you must select **k** authorized groupings such that each engineer is assigned to exactly one line, each robotic arm is used on exactly one line, and each maintenance window is scheduled for exactly one line.

Determine whether the daily operations can be successfully set up, and if so, report one valid selection of groupings.

## Input

The first line provides two integers, **k** and **t**. The plant employs a positive number of engineers, **k**, which cannot exceed the 22 safety harnesses available in the facility. The value **t** indicates the number of authorized groupings provided in the input; this count can be anything from zero up to the theoretical maximum where every possible combination of engineer, arm, and window is certified.

The subsequent **t** lines each contain three integers **x**, **y**, and **z**. These represent an authorized grouping of engineer **x**, robotic arm **y**, and maintenance window **z**. Each ID naturally ranges from 1 up to the total number of assets in its pool (**k**). No grouping is repeated in the input.

## Output

If it is possible to activate **k** lines such that every asset is utilized exactly once, output `YES` on the first line. Then, output **k** lines, each containing the three IDs **x** **y** **z** of an activated grouping. Any valid selection is accepted, and the groupings may be printed in any order.

If no such setup is possible, output `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 1 2
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

## Note

In Example 2, both authorized groupings require robotic arm 1, meaning robotic arm 2 can never be utilized.
