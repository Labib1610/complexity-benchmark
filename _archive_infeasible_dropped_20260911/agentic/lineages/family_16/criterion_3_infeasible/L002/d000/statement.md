# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A chef is preparing a banquet featuring **j** special recipes, tracked in the kitchen's order system as `JOB`s. Every `JOB` must be baked in appliance 1 (the oven) first and then finished in appliance 2 (the broiler). For each `JOB` you are given its required time in appliance 1 and in appliance 2. Each appliance processes only one `JOB` at a time, and a `JOB` reaches appliance 2 only after finishing in appliance 1.

There is a strict time limit **T**: every `JOB` must be completely finished by time **T**.

For every input in this problem it is **guaranteed that the time limit cannot be met**, no matter how the chef orders the preparation. Your task is not to search for a schedule; it is to **prove** the time limit is impossible with a short certificate that can be checked directly against the input.

Exactly one of the following reasons always applies. Print the one that holds:

- **A single recipe is too long.** If some `JOB`'s two appliance times add up to more than **T**, that `JOB` alone (appliance 1 then appliance 2, in sequence) cannot finish by **T**.
  Print: `JOB i` — where **i** (1-based) is such a `JOB`.

- **An appliance is overloaded.** An appliance handles its `JOB`s one at a time, so it needs at least the sum of all its required times. If the total workload on appliance 1 (or appliance 2) exceeds **T**, the time limit is impossible.
  Print: `LOAD c` — where **c** is 1 or 2 and the total time on appliance **c** exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the required times of a `JOB` in appliance 1 and appliance 2.

## Output

Print a single line: `JOB i` (a `JOB` whose p1 + p2 exceeds T) or `LOAD c` (an appliance c whose total required time exceeds T).

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

In Example 1, `JOB` 1 needs 70 + 60 = 130 > 100 time units in sequence, so `JOB 1` proves the time limit is impossible. In Example 2 no single `JOB` exceeds 150, but appliance 1 must process 50+50+50+50 = 200 > 150 units of work in total, so `LOAD 1` is the certificate.
