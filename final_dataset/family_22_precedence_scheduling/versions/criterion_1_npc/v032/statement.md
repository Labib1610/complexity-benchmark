# Problem A — Uniform Curriculum Stratification

Time limit: 5 s
Memory limit: 256 MB

## Description
A certification authority is designing a standardized training program consisting of $n$ uniform modules. The program must be entirely completed within a limit of $T$ phases. 

To ensure a steady pace of learning, each module requires exactly one phase to complete. The authority has $M$ certified reviewers available per phase. Each reviewer can evaluate at most one module during a single phase, capping the total number of modules that can be assigned to any one phase at $M$. Because the system is highly regular and all modules share the exact same duration, any reviewer can handle any module, and only the phase assignment matters.

The knowledge required for the program is progressive. Certain modules serve as foundational prerequisites for others. Whenever module $a$ is a prerequisite for module $b$, module $b$ must be assigned to a strictly later phase than module $a$ (being in the same phase is not sufficient, as the foundational knowledge is only available from the next phase onward). 

Given the uniform length of all modules and the interchangeable nature of the reviewers, determine if it is possible to assign each module to exactly one phase (from 1 to $T$) such that all prerequisite conditions are strictly satisfied and no phase is assigned more than $M$ modules. If it is possible, output a valid phase assignment.

## Input
First line: four integers $n$, $M$, $T$, $m$.
Each of the next $m$ lines: two integers $a$ and $b$ — module $a$ must be assigned to a phase strictly earlier than module $b$.

## Output
Print `YES` then $n$ integers (the phase assigned to each module 1 through $n$, taking values in 1..$T$); otherwise print `NO`.

## Example

**Input**
```text
5 2 3 4
1 3
2 3
3 4
3 5
```

**Output**
```text
YES
1 1 2 3 3
```
