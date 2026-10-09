# Problem A — Surgical Program Scheduling

Time limit: 5 s   Memory limit: 256 MB

## Description

A hospital is planning a specialized surgical program that requires scheduling exactly **k** operations. The program involves **k** surgeons, **k** operating rooms, and **k** time slots, each identified by an integer from 1 to **k**.

Only **t** specific combinations of a surgeon, an operating room, and a time slot are clinically viable. 

The hospital administration must select exactly **k** of these viable combinations to form the final schedule. A schedule is valid if and only if it avoids all resource conflicts: no surgeon may be assigned to more than one operation, no operating room may host more than one operation, and no time slot may contain more than one operation. 

Because exactly **k** operations must be selected and each resource pool has size **k**, a valid schedule guarantees that every surgeon operates exactly once, every room is used exactly once, and every time slot is filled exactly once.

Determine whether a valid schedule can be formed from the viable combinations, and if so, report one such schedule.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of operations to schedule (which is also the number of available surgeons, rooms, and time slots) and the number of clinically viable combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a viable combination of surgeon **x**, operating room **y**, and time slot **z**. No combination is listed more than once in the input.

## Output

If a valid schedule of exactly **k** operations exists, print `YES` on the first line. Then, print **k** lines, each containing the three integers `x y z` of one selected combination. Any valid schedule is accepted, and the combinations may be printed in any order.

If no valid schedule exists, print `NO`.

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

In Example 2, both viable combinations require operating room 1. Any schedule of 2 operations would cause a resource conflict for this room, making a valid schedule impossible.
