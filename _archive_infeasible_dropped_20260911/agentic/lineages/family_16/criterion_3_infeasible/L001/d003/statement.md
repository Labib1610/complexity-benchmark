# Problem C — Impossibility Certificate

Time limit: 2 s   Memory limit: 256 MB

## Description

A factory is tasked with completing **j** distinct manufactured items. The production of each item requires sequential processing through two specialized stages: stage 1 must be fully completed for an item before its stage 2 processing can begin. You are provided with the required processing time in stage 1 and stage 2 for every item. Neither stage can process more than one item simultaneously.

The factory operates under a strict global deadline **T**. All operations across both stages for all items must be finalized by this time.

In this specific problem, **no valid schedule exists** that can meet the deadline **T** for the given inputs. Instead of attempting to schedule the items, your task is to output a simple proof (a certificate) demonstrating why the deadline is structurally impossible to meet. 

It is guaranteed that the impossibility in each test case is caused by exactly one of the two bottleneck categories defined below. You must determine which category applies and output a valid certificate for it. If the applicable category offers multiple valid certificates, any single one is acceptable.

- **Item Span Violation:** A single item **i** requires a combined processing time across both stages that strictly exceeds the deadline **T**. 
  Output format: `JOB i` (where **i** is the 1-based index of the item).

- **Stage Overload:** The aggregate processing time required by all **j** items in a single stage **c** (**c** $\in \{1, 2\}$) strictly exceeds the deadline **T**.
  Output format: `LOAD c` (where **c** is the stage number, either 1 or 2).

## Input

The first line specifies two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
The subsequent **j** lines each provide two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing the processing time required for that item in stage 1 and stage 2, respectively.

## Output

Output exactly one line containing a valid certificate from the applicable bottleneck category: either `JOB i` or `LOAD c`.

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, the first item needs 70 time units in stage 1 and 60 in stage 2. Because these stages must occur sequentially for the item, its absolute minimum completion time is 130. This strictly exceeds the deadline of 100 on its own, so `JOB 1` correctly certifies the impossibility.
In Example 2, no individual item's span exceeds 150. However, stage 1 is required to do 200 total units of work (50 for each of the 4 items). Since a stage processes one item at a time, stage 1 cannot finish its workload within the 150 deadline, making `LOAD 1` a valid certificate.