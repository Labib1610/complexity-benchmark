# Problem A — Workforce Synchronization Pipeline

Time limit: 5 s   Memory limit: 256 MB

## Description
You are implementing the middle stage of an automated scheduling pipeline for a specialized workforce. The pipeline operates in three consecutive stages:

**Stage 1: Workload Distribution (Pre-processing)**
An upstream module determines the team structure. Every project requires the joint effort of exactly two employees. The generator strictly balances the workload, guaranteeing that every employee is assigned to exactly three projects.

**Stage 2: Shift Allocation (Your Task)**
You must schedule each project into one of three available operational shifts (labeled 1, 2, and 3). 
For the schedule to be viable, no individual can be double-booked. This means an employee cannot work on multiple projects during the same shift. Because each employee is responsible for three projects and there are only three shifts available, every employee must have exactly one project scheduled in shift 1, one in shift 2, and one in shift 3.

**Stage 3: Execution (Post-processing)**
A downstream system takes the scheduled projects to finalize the company timetable. If you can find a valid shift allocation for all projects, you must output it so it can be passed to this system. If no such allocation exists, you must reject the workload distribution so the pipeline can discard it and request a new structure from Stage 1.

## Input
The first line contains two integers **n** and **m** (where **n** is even, **m** = 3**n**/2, and 2 ≤ **n** ≤ 2000), representing the number of employees and the total number of collaborative projects produced by Stage 1.
Each of the next **m** lines contains two integers *u* and *v* (1 ≤ *u* < *v* ≤ **n**), indicating a project that requires the collaboration of employee *u* and employee *v*.

## Output
If a valid shift allocation exists for Stage 3, output `YES` on the first line. On the second line, output **m** integers from the set {1, 2, 3}, representing the shift assigned to each project in the exact order they were given in the input. If multiple valid allocations exist, you may output any of them.
If no valid allocation is possible, output `NO`.

## Example
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
YES
1 2 3 3 2 1
```
