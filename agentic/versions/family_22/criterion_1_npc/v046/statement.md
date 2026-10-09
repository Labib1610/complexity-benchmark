# Problem A — Degree Program Scheduling

Time limit: 5 s   Memory limit: 256 MB

## Description
A university is designing a degree program structured as a fixed sequence of academic terms. Students must complete all required modules to graduate. To ensure a manageable workload, the university enforces a strict cap on the maximum number of modules a student can enroll in during any single term. All modules within a term are taken concurrently, so their relative order within that term is irrelevant; only the term assignment matters.

The curriculum is bound by academic dependencies. If module $a$ is a prerequisite for module $b$, students must complete module $a$ in a term strictly prior to the term in which they take module $b$. Taking them in the same term is prohibited because the foundational knowledge from $a$ is required from the very first day of $b$.

Given the total number of modules, the term enrollment cap, the total number of terms available in the program, and the list of prerequisites, determine if it is possible to schedule all modules into the available terms without exceeding the enrollment cap or violating any prerequisites. If it is possible, provide a valid term assignment for each module. (With limited term capacity, satisfying all prerequisites might require squeezing too many modules into a single term, and resolving this overload might push modules past the final available term.)

## Input
First line: four integers $n, M, T, m$. 
Each of the next $m$ lines: two integers $a$ and $b$ — module $a$ must be completed in a term strictly before module $b$.

## Output
Print `YES` then $n$ integers (the term number assigned to each module, from $1$ to $T$); otherwise print `NO`.

### Example 1

**Input**
```text
4 2 3 3
1 2
1 3
2 4
```

**Output**
```text
YES
1 2 2 3
```
