# Problem B — Configuration State Search

Time limit: 1 s   Memory limit: 256 MB

## Description

The central control matrix for a new facility contains $n$ independent two-way toggles. When preparing the facility for operation, engineers must select a single configuration from the $2^n$ possible global states.

Because the toggles control interacting subsystems, the chosen configuration must pass a rigorous safety audit consisting of $m$ distinct clearance criteria. The audit is strict: all $m$ criteria must be satisfied simultaneously. The sheer volume of the $2^n$ state space makes exhaustive validation of all potential configurations impossible, yet a globally safe state must be found if one exists.

During the audit, the safety system evaluates a series of conditions. A clearance criterion is defined by a list of toggle requirements (a requirement being a particular toggle and its expected position, either ON or OFF). To limit the complexity of individual checks, the engineers restricted each criterion to monitor precisely two such requirements. A criterion is considered cleared as long as the global configuration fulfills at least one of its monitored requirements.

Your task is to determine whether there exists a configuration in the immense state space that simultaneously clears all $m$ criteria, and if so, output it.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of toggles and the number of clearance criteria.

Each of the following $m$ lines contains two non-zero integers $l_1$ and $l_2$ ($-n \le l_i \le n$, $l_i \neq 0$). These represent the requirements for that criterion. The absolute value $|l_i|$ identifies the toggle. A positive value means the requirement is for the toggle to be ON, while a negative value means the requirement is for the toggle to be OFF.

## Output
If no configuration in the state space clears all criteria, print a single line `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$) representing the valid configuration (1 for ON, 0 for OFF).

## Example 1
**Input:**
```
2 2
1 2
-1 -2
```
**Output:**
```
YES
1 0
```

## Example 2
**Input:**
```
1 2
1 1
-1 -1
```
**Output:**
```
NO
```

## Note
Multiple valid configurations may exist; any one is accepted. The same toggle may appear in multiple criteria.
