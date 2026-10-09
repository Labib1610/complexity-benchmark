# Problem B — Control Panel Selection

Time limit: 2 s   Memory limit: 256 MB

## Description

A social media platform is conducting a multi-stage user study. The workflow operates in three distinct phases:

**Phase 1: Interaction Auditing.** The platform selects **n** users (numbered 1 to **n**) and logs **m** direct connections between them. During this phase, the analytics engine guarantees that the chosen population strictly divides into two demographic cohorts, and every logged connection exclusively bridges a user from one cohort to a user in the other. (The cohort assignments themselves are not saved in the logs, but this structural guarantee is absolute).

**Phase 2: Panel Extraction (Your Task).** The researchers must isolate a control panel of exactly **k** users from the audited pool. To prevent cross-contamination of survey results, the chosen panel must be completely mutually disconnected—meaning no two users in the panel share a logged connection.

**Phase 3: Deployment.** The isolated panel of **k** users is automatically passed to the messaging microservice for simultaneous survey delivery.

Your program is responsible for executing Phase 2. Given the network size **n**, the number of logged connections **m**, the target panel size **k**, and the list of connections from Phase 1, determine if a valid control panel can be formed. If successful, output the members of the panel so they can be utilized in Phase 3.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
The following **m** lines each contain two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a logged connection between user **u** and user **v**.

No connection appears more than once. The input is guaranteed to satisfy the Phase 1 condition: the users can be partitioned into two cohorts such that every connection runs between different cohorts.

## Output

If it is possible to extract a valid control panel of exactly **k** users, print `YES` on the first line. On the second line, print the **k** distinct user numbers that make up the panel, separated by spaces. If multiple valid panels exist, any of them will be accepted by the Phase 3 microservice.

If no such panel can be formed, print `NO`.

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
