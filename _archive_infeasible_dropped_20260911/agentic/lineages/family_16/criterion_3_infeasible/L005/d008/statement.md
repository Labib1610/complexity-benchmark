# Problem C — Schedule Diagnostics

Time limit: 2 s   Memory limit: 256 MB

## Description

A manufacturing plant must process **j** items through two sequential stages. A schedule assigns each item **k** a start time $S_{1,k}$ on facility 1 and a start time $S_{2,k}$ on facility 2.
Any valid schedule must satisfy the following constraints:
1. **Earliest start:** $S_{1,k} \ge 1$ and $S_{2,k} \ge 1$ for all **k**.
2. **Sequential flow:** $S_{2,k} \ge S_{1,k} + p_{1,k}$ for all **k** (stage 2 cannot start until stage 1 finishes).
3. **Completion times:** The completion time of item **k** on stage 1 is $C_{1,k} = S_{1,k} + p_{1,k}$, and on stage 2 is $C_{2,k} = S_{2,k} + p_{2,k}$.
4. **No overlap on facility 1:** For any two distinct items **k** and **m**, their processing intervals on facility 1, $[S_{1,k}, C_{1,k})$, do not intersect.
5. **No overlap on facility 2:** For any two distinct items **k** and **m**, their processing intervals on facility 2, $[S_{2,k}, C_{2,k})$, do not intersect.

The plant is given a time parameter **T**. A schedule is successful if $C_{2,k} \le T + 1$ for all items **k**.

For every given input, it is guaranteed that no successful schedule exists. You must provide a short certificate proving this impossibility. Exactly one of the following two structural bottlenecks will apply, and you must output the corresponding certificate:

- `JOB i` (where **i** is the 1-based index of the item): This certificate is valid if item **i** is inherently impossible to complete by $T + 1$. Specifically, if you consider a relaxed scenario where item **i** is the only item in the plant (ignoring constraints 4 and 5), it is still impossible to assign start times that satisfy constraints 1, 2, and 3 while keeping $C_{2,i} \le T + 1$. If multiple items fit this description, you may output any one of them.
- `LOAD c` (where **c** is 1 or 2): This certificate is valid if facility **c** is overloaded. Specifically, if you consider a relaxed scenario where the sequential flow constraint (2) and all constraints regarding the other facility are ignored, it is still impossible to schedule all items on facility **c** (satisfying constraints 1, 3, and the no-overlap constraint for facility **c**) such that every item finishes on facility **c** at or before $T + 1$. If both facilities fit this description, you may output either one.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the following **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the processing duration of an item at stage 1 and stage 2, respectively.

## Output

Print a single line containing the certificate: either `JOB i` or `LOAD c`.

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

In Example 1, **T** = 100, meaning all items must finish stage 2 before or at time 101. Item 1 has durations 70 and 60. Even if item 1 is the only item in the plant, any valid start times satisfying earliest start and sequential flow will result in its stage 2 completion strictly exceeding 101. Thus, `JOB 1` is a valid certificate.

In Example 2, **T** = 150, meaning all items must finish stage 2 before or at time 151. No single item fails the isolated check. However, if we evaluate facility 1 in isolation (ignoring sequential flow and facility 2), we have 4 items each requiring 50 units of time on facility 1. Even without facility 2 constraints, scheduling these 4 items on facility 1 without overlap, starting no earlier than time 1, guarantees that at least one item finishes facility 1 strictly after time 151. Thus, `LOAD 1` is a valid certificate.