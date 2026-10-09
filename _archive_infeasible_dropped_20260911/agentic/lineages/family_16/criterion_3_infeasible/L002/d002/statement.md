# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A chef is preparing a banquet featuring **j** special recipes, tracked in the kitchen's order system as `JOB`s. Every `JOB` must be processed in appliance 1 (the oven) and subsequently in appliance 2 (the broiler). For each `JOB` you are given the exact number of minutes it must occupy appliance 1, and the exact number of minutes it must occupy appliance 2. Each appliance can only accommodate one `JOB` at any given moment, and a `JOB` can only transition to appliance 2 after its appliance 1 phase is entirely complete.

The kitchen operates under a strict deadline: all processing for all `JOB`s must be completely finished by time **T**.

For every input in this problem, it is **guaranteed that the deadline cannot be met**, no matter how the chef schedules the processing. Your task is not to search for a schedule; it is to **prove** the deadline is impossible with a short certificate that can be checked directly against the input.

Exactly one of the following reasons is guaranteed to apply for every input. Print the certificate corresponding to the unique applicable reason:

- **A single recipe cannot fit the timeline.** For a specific recipe, if it begins in the oven at time 0, the time remaining before the deadline **T** after its oven phase concludes is strictly less than the minutes it requires in the broiler.
  Print: `JOB i` — where **i** (1-based) is such a recipe.

- **An appliance's available time is depleted.** Because appliances process non-concurrently, they have a maximum of **T** active minutes available. If you start with a budget of **T** minutes for the oven and sequentially deduct the oven minutes required by each recipe, the budget drops strictly below zero. The same failure mode can occur for the broiler.
  Print: `LOAD c` — where **c** is 1 (if the oven's budget is depleted strictly below zero) or 2 (if the broiler's budget is depleted strictly below zero).

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the required minutes of the `JOB` in appliance 1 and appliance 2.

## Output

Print a single line: `JOB i` (a `JOB` whose timeline check fails) or `LOAD c` (an appliance **c** whose time budget is depleted strictly below zero).

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

In Example 1, if `JOB` 1 starts at time 0, it finishes in the oven at time 70. The time remaining before the deadline is 100 - 70 = 30 minutes. This is strictly less than the 60 minutes it requires in the broiler, so `JOB 1` proves the deadline is impossible.

In Example 2, no single `JOB` fails the timeline check. However, if we sequentially deduct the oven minutes required by each recipe from the 150-minute budget of appliance 1, we get 150 - 50 - 50 - 50 - 50 = -50. Since the budget drops strictly below zero, the 150 time limit is impossible, so `LOAD 1` is the certificate.